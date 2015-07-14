
DROP KEYSPACE sensordata;
CREATE KEYSPACE sensordata WITH  replication = {'class': 'SimpleStrategy', 'replication_factor': 3 };
USE sensordata;
CREATE TABLE acc_x (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE acc_y (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE acc_z (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE mag_x (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE mag_y (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE mag_z (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE gyr_x (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE gyr_y (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE gyr_z (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
