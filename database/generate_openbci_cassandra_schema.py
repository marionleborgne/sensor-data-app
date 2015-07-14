__author__ = 'mleborgne'

# column family names and the associated number of columns per family
SENSOR = 'openbci'
KEYSPACE = SENSOR
METRICS = ['channel_0', 'channel_1', 'channel_2', 'channel_3', 'channel_4', 'channel_5', 'channel_6', 'channel_7']
COLUMNS = ['metric_value', 'prediction', 'anomaly_score', 'anomaly_likelihood']
SENSOR_ID = 'openbci_marion'
FILE_NAME = '%s_cassandra_schema.cql' % SENSOR_ID

# templates for column family creation
create_column_family_template = "CREATE TABLE %s (%s, PRIMARY KEY (sensor_id, timestamp)); \n"

f = open(FILE_NAME, 'w')


setup = """
DROP KEYSPACE %s;
CREATE KEYSPACE %s WITH  replication = {'class': 'SimpleStrategy', 'replication_factor': 3 };
USE %s;
""" % (KEYSPACE, KEYSPACE, KEYSPACE)

f.write(setup)



for metric in METRICS:
  column_family_name = '%s' % (metric)

  columns = 'sensor_id text, timestamp timestamp'
  for column in COLUMNS:
      columns += ', %s double' % column
  create_column_family = create_column_family_template % (column_family_name, columns)
  print create_column_family
  f.write(create_column_family)

f.close()

print "\n==> Output written to file '%s'" % FILE_NAME
