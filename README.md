# Store_MQTT_Data_in_Database

For detailed instruction please refer to the following link  -

https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/

Fork:
Modified version to store data produced by a rpi python program. More details soon.

Instructions:

Load the virtual environment:

```
$ source ~/Code/python/HillarMQTT/01/bin/activate
```

Run the scripts:

To initialize the DB
```
(01) $ python initialize_DB_Tables.py
```

To publish random data in the topics
```
(01) $ python mqtt_Publish_Dummy_Data.py
```

In a new terminal

```
$ source ~/Code/python/HillarMQTT/01/bin/activate
```
and run the Listener script

```
(01) $ python mqtt_Listen_Sensor_Data.py
```
