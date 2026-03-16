package de.bigdatabuch.thinclient;

import de.bigdatabuch.SensorReadingSQL;
import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;

public class IgniteSensorPythonThinClient {
    public static void main(String[] args) throws InterruptedException {
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

            // 2. Cluster lauschen lassen
            while(true) {
                Thread.sleep(2 * 1000L);
            }
        }
    }
}
