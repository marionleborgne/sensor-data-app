
DROP KEYSPACE openbci;
CREATE KEYSPACE openbci WITH  replication = {'class': 'SimpleStrategy', 'replication_factor': 3 };
USE openbci;
CREATE TABLE channel_0 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_1 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_2 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_3 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_4 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_5 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_6 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
CREATE TABLE channel_7 (sensor_id text, timestamp timestamp, metric_value double, prediction double, anomaly_score double, anomaly_likelihood double, PRIMARY KEY (sensor_id, timestamp)); 
