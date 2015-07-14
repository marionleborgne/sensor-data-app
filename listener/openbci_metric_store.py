__author__ = 'mleborgne'

from cassandra.cluster import Cluster
import time
import pika
import json
import importlib

from nupic.frameworks.opf.modelfactory import ModelFactory

# to get the anomaly likelihood
from nupic.algorithms import anomaly_likelihood 
anomalyLikelihood = anomaly_likelihood.AnomalyLikelihood()

MODEL_NAME = 'acc' # TODO: change this
SENSOR = 'openbci'
METRICS = ['channel_0', 'channel_1', 'channel_2', 'channel_3', 'channel_4', 'channel_5', 'channel_6', 'channel_7']
COLUMNS = ['metric_value', 'prediction', 'anomaly_score', 'anomaly_likelihood']
SENSOR_ID = 'openbci_marion'


# configure cassandra cluster
cluster = Cluster()
session = cluster.connect('openbci')

# configure and connect RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
  host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange=SENSOR,
                         type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange=SENSOR,
                   queue=queue_name)

def getModelParamsFromName(metric_name):
  importName = "model_params.%s" % metric_name
  print "Importing model params from %s" % importName
  try:
    importedModelParams = importlib.import_module(importName).MODEL_PARAMS
  except ImportError:
    raise Exception("No model params exist for '%s'." % metric_name)
  return importedModelParams


def callback(ch, method, properties, body):
  messages = json.loads(body)
  
  for data in messages:
    for metric in METRICS:
      timestamp = data['timestamp']
      metric_value = data[metric]
      (metric_value, prediction, anomalyScore, anomalyLikelihood) = run_model(metric, metric_value)
      store_data(timestamp, metric, metric_value, prediction, anomalyScore, anomalyLikelihood)
      #print "t: %s - (%s,%s)" %(timestamp, metric, metric_value)


def run_model(timestamp, metric_value):
  metric_value = float(metric_value)
  
  """
  result = model.run({
    "metric_value": metric_value
  })

  prediction = result.inferences["multiStepBestPredictions"][1]
  anomalyScore = result.inferences["anomalyScore"]
  
  likelihood = anomalyLikelihood.anomalyProbability(
     metric_value, anomalyScore
  )
  
  
  """
  prediction = 0
  likelihood = 0
  anomalyScore = 0
  
  return metric_value, prediction, anomalyScore, likelihood


      

def store_data(timestamp, metric, metric_value, prediction, anomalyScore, anomalyLikelihood):
  column_values = "'%s', %s, %s, %s, %s, %s" % (SENSOR_ID, timestamp, metric_value, prediction, anomalyScore, anomalyLikelihood)

  column_family = "%s" % metric
  columns = "sensor_id, timestamp, %s" %','.join(COLUMNS)
  cql_insert = "INSERT INTO %s (%s) VALUES (%s);" % (column_family, columns, column_values)
  #print cql_insert

  try:
    session.execute(cql_insert)
    #print cql_insert
  except:
    print "DEBUG: CQL insert: %s" % cql_insert
      

  

# configure nupic model
model = ModelFactory.create(getModelParamsFromName(MODEL_NAME))
model.enableInference({"predictedField": "metric_value"})

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

print "waiting for data on exchange '%s' ..." % SENSOR
