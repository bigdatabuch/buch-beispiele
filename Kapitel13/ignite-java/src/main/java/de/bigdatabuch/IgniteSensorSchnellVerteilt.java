package de.bigdatabuch;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;

import java.util.List;

public class IgniteSensorSchnellVerteilt {
    public static void main(String[] args) {
        // Startet einen Ignite-Knoten und tritt einem Cluster bei (anhand gegebener Konfiguration, deklarativ per XML oder programmatisch)
        try (Ignite ignite = Ignition.start(new IgniteConfiguration())) {
            // Erstellt einen verteilten Cache (oder holt ihn, wenn er schon existiert).
            // Cache Konfiguration für SQL anpassen (d.h. SQL aktivieren -- benötigt Annotationen, s. SensorReadingSQL)
            CacheConfiguration<Integer, SensorReadingSQL> cacheCfg = new CacheConfiguration<>();
            cacheCfg.setName("sensorCacheSql");
            cacheCfg.setCacheMode(CacheMode.REPLICATED);
            cacheCfg.setIndexedTypes(Integer.class, SensorReadingSQL.class);
            cacheCfg.setSqlSchema("PUBLIC");
            // Verwendbar wie eine verteilte HashMap
            IgniteCache<Integer, SensorReadingSQL> sensorCache = ignite.getOrCreateCache(cacheCfg);

            // 1. Daten in den Cache legen
            sensorCache.put(1, new SensorReadingSQL(1, "Mannheim", 22.5));
            sensorCache.put(2, new SensorReadingSQL(2, "Würzburg", 24.1));
            sensorCache.put(3, new SensorReadingSQL(3, "Ingolstadt", 25.2));

            // 2. Daten aus dem Cache lesen
            SensorReadingSQL mannheimReading = sensorCache.get(1);
            System.out.println("Sensorwert: " + mannheimReading.getTemperature());

            // verteiltes (schnell)
            double sAvg = verteiltesAggregieren(sensorCache);
            System.out.println("Verteiltes aggregieren: " + sAvg);
        }
    }

    static double verteiltesAggregieren(IgniteCache<Integer, SensorReadingSQL> sensorCache) {
        // Eine SQL Anfrage wird an den Cluster gesendet
        String sql = "SELECT AVG(temperature) FROM SensorReadingSQL WHERE city = ?";
        SqlFieldsQuery query = new SqlFieldsQuery(sql).setArgs("Mannheim");

        // Nur das Endergebnis (ein double-Wert) wird zurückgesendet
        List<List<?>> result = sensorCache.query(query).getAll();
        double average = (Double) result.get(0).get(0);

        return average;
    }
}
