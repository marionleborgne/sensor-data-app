## TI SensorTag Sample App

### Dependencies
* rabbit.js
* async
* sensortag
* cassandra-driver
* blist
* pika
* flask

### Install
* Install RabbitMQ
* Install Cassandra
* Install `node` and `npm`
* `npm install rabbit.js`
* `npm install async`
* `npm install sensortag`
* `sudo pip install cassandra-driver`
* `sudo pip install blist`
* `sudo pip install pika`
* `sudo pip install flask`

### Run the App


#### Start RabbitMQ
* Get RabbitMQ.
* Change to your RabbitMQ directory. 
* Start RabbitMQ: `sh sbin/rabbit-server start`

#### Start the SensorTag Connector
* Make sure your bluetooth connection is on and the TI SensorTag is discoverable.
* Change to `connector` and start the connector with `node sensortag-server.js`

#### Start Cassandra
* Get Cassandra.
* Change to your Cassandra directory.
* Start Cassandra: `sh bin/cassandra start`
* Generate Cassandra schema: `python database/generate_cassandra_schema.py`
* Execute schema: `bin/cqlsh -f <path_to_cassandra_schema>/cassandra_schema.cql`


#### Run MetricStore
* `python listener/metric_store.py`

#### Start the REST API
* Run `python api/web_api.py`

#### Start the UI
* Open `ui/chart.html` in your browser. You should see a live chart with real-time anomalies.