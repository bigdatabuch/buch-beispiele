package de.bigdatabuch;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.configuration.IgniteConfiguration;

import javax.cache.Cache;

public class IgniteSensorLangsamLokal {
    public static void main(String[] args) {
        // Startet einen Ignite-Knoten und tritt einem Cluster bei (anhand gegebener Konfiguration, deklarativ per XML oder programmatisch)
        try (Ignite ignite = Ignition.start(new IgniteConfiguration())) {
            // Erstellt einen verteilten Cache (oder holt ihn, wenn er schon existiert).
            // Verwendbar wie eine verteilte HashMap
            IgniteCache<Integer, SensorReading> sensorCache = ignite.getOrCreateCache("sensorCache");

            // 1. Daten in den Cache legen
            sensorCache.put(1, new SensorReading(1, "Mannheim", 22.5));
            sensorCache.put(2, new SensorReading( 2, "Würzburg", 24.1));
            sensorCache.put(3, new SensorReading( 3, "Ingolstadt", 25.2));

            // 2. Daten aus dem Cache lesen
            SensorReading maReading = sensorCache.get(1);
            System.out.println("Sensorwert: " + maReading.getTemperature());

            // lokales aggregrieren (langsam)
            double lAvg = lokalesAggregieren(sensorCache);
            System.out.println("Lokales aggregieren: " + lAvg);
        }
    }

    static double lokalesAggregieren(IgniteCache<Integer, SensorReading> sensorCache) {
        int totalTemp = 0;
        int count = 0;
        // Client holt alle Einträge über das Netzwerk von allen teilnehmenden Maschinen!
        for (Cache.Entry<Integer, SensorReading> entry : sensorCache) {
            if ("Mannheim".equals(entry.getValue().getCity())) {
                totalTemp += entry.getValue().getTemperature();
                count++;
            }
        }
        double average = totalTemp / count;

        return average;
    }
}
