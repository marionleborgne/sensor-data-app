__author__ = 'mleborgne'

import json
import time
import datetime
import random
from flask import Flask, request, current_app
from functools import wraps

from settings import SENSOR_ID, METRICS, ANOMALY_LIKELIHOOD_THRESHOLD, DATE_FORMAT

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f()) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function


@app.route('/data', methods=['GET'])
@support_jsonp
def data():
  # Get the parsed contents of the form data
  start = int(time.time()) - 5

  try:
    data = []
    for i in xrange(5):
      sensor_id = SENSOR_ID
      timestamp = (start+i) * 1000 #.strftime(DATE_FORMAT)
      anomaly = False
      if i == 3:
        anomaly = True
      
      anomaly_score = random.random()
      metric_value = random.random() * 10
      prediction = random.random() * 10
      data.append({'sensor_id': sensor_id,
                   'timestamp': timestamp,
                   'anomaly': anomaly,
                   'anomaly_likelihood': anomaly_score,
                   'metric_value': metric_value,
                   'prediction': prediction})
      

    return json.dumps(data)
  except Exception, e:
    error = "[ERROR] Internal server error."
    print e 
    return error, 500
  
  
@app.route('/sensor', methods=['GET'])
@support_jsonp
def sensor():
  """
  Data returned:
    {
      timestamp: <long>, 
      sensor_id: <string>,
      x: {metric_value: <float>, anomaly_likelihood: <float>, anomaly: <boolean>},
      y: {metric_value: <float>, anomaly_likelihood: <float>, anomaly: <boolean>},
      y: {metric_value: <float>, anomaly_likelihood: <float>, anomaly: <boolean>}
    }

  
  :return: The last datapoint this sensor.
  """

  timestamp = datetime.datetime.fromtimestamp(int(time.time())).strftime(DATE_FORMAT)  
  
  result = {'sensor_id': SENSOR_ID}
  for metric in METRICS:
    anomaly_likelihood = random.random()
    if anomaly_likelihood > ANOMALY_LIKELIHOOD_THRESHOLD:
      anomaly = True
    else:
      anomaly = False
    
    metric_value = random.random() * 10
    result[metric] = {'metric_value': metric_value,
                      'anomaly_likelihood' : anomaly_likelihood,
                      'anomaly': anomaly}
  result['timestamp'] = timestamp    


  #return [{"name":"golfers"},{"data":[random.random(),random.random(),random.random(),random.random(),random.random(),random.random()]}]
  return json.dumps(result)


if __name__ == '__main__':
  app.run('0.0.0.0', 5050)