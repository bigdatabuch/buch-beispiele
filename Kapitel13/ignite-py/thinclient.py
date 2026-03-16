from pyignite import Client

# Setzt voraus dass wir den Java Cluster (ignite-java) gestartet haben. Siehe Klasse IgniteSensorPythonThinClient.java
client = Client()
client.connect('127.0.0.1', 10800)

# Alle Caches anzeigen
result = client.get_cache_names()
# Sensor Cache
sensor_cache = client.get_or_create_cache('sensorCacheSql')

sql = "SELECT AVG(temperature) FROM SensorReadingSQL WHERE city = ?"
result = client.sql(sql, query_args=['Mannheim'])

for row in result:
    print(f"Durchschnitt: {row[0]}")

client.close()