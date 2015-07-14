__author__ = 'mleborgne'

# column family names and the associated number of columns per family
SENSORS = ['acc', 'mag', 'gyr']
METRICS = ['x', 'y', 'z']
COLUMNS = ['metric_value', 'prediction', 'anomaly_score', 'anomaly_likelihood']
SENSOR_ID = '869102e418344394a63ee6e00a989c36'
FILE_NAME = 'cassandra_schema.cql'

# templates for column family creation
create_column_family_template = "CREATE TABLE %s (%s, PRIMARY KEY (sensor_id, timestamp)); \n"

f = open(FILE_NAME, 'w')


setup = """
DROP KEYSPACE sensordata;
CREATE KEYSPACE sensordata WITH  replication = {'class': 'SimpleStrategy', 'replication_factor': 3 };
USE sensordata;
"""

f.write(setup)


for sensor in SENSORS:
  for metric in METRICS:
    column_family_name = '%s_%s' % (sensor, metric)

    columns = 'sensor_id text, timestamp timestamp'
    for column in COLUMNS:
        columns += ', %s double' % column
    create_column_family = create_column_family_template % (column_family_name, columns)
    print create_column_family
    f.write(create_column_family)

f.close()

print "\n==> Output written to file '%s'" % FILE_NAME
