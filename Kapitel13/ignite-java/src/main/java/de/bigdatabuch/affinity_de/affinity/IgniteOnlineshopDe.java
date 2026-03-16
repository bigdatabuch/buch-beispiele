package de.bigdatabuch.affinity_de.affinity;

import org.apache.ignite.Ignite;
import org.apache.ignite.IgniteCache;
import org.apache.ignite.Ignition;
import org.apache.ignite.cache.CacheMode;
import org.apache.ignite.cache.query.SqlFieldsQuery;
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.configuration.IgniteConfiguration;

import java.util.Date;

public class IgniteOnlineshopDe {
    public static void main(String[] args) {
        // Startet einen Ignite-Knoten und tritt einem Cluster bei (anhand gegebener Konfiguration, deklarativ per XML oder programmatisch)
        try (Ignite ignite = Ignition.start(new IgniteConfiguration())) {
            // Erstellt einen verteilten Cache (oder holt ihn, wenn er schon existiert).
            // Caches für Customer und Order konfigurieren
            CacheConfiguration<String, Kunde> cuCacheCfg = new CacheConfiguration<>();
            cuCacheCfg.setName("customerCache");
            cuCacheCfg.setCacheMode(CacheMode.REPLICATED);
            cuCacheCfg.setIndexedTypes(String.class, Kunde.class);
            cuCacheCfg.setSqlSchema("PUBLIC");

            CacheConfiguration<String, Bestellung> orCacheCfg = new CacheConfiguration<>();
            orCacheCfg.setName("orderCache");
            orCacheCfg.setCacheMode(CacheMode.REPLICATED);
            orCacheCfg.setIndexedTypes(String.class, Bestellung.class);
            orCacheCfg.setSqlSchema("PUBLIC");

            IgniteCache<String, Kunde> customerCache = ignite.getOrCreateCache(cuCacheCfg);
            IgniteCache<String, Bestellung> orderCache = ignite.getOrCreateCache(orCacheCfg);

            customerCache.put("K-1234", new Kunde("K-1234", "max.mustermann@musterhausen.de"));
            orderCache.put("B6789", new Bestellung("B6789", "K-1234", 10.99d, new Date()));
            orderCache.put("B8789", new Bestellung("B8789", "K-1234", 5.99d, new Date()));

            // SQL Abfrage
            colocatedSQL(customerCache, orderCache);
        }
    }

    static void colocatedSQL(IgniteCache<String, Kunde> customerCache, IgniteCache<String, Bestellung> orderCache) {
        // ACHTUNG: "ORDER" ist ein reserviertes Keyword in SQL
        SqlFieldsQuery totalQuery = new SqlFieldsQuery(
                "SELECT k.kundenId, COUNT(b.bestellungId), SUM(b.betrag) " +
                        "FROM Kunde k " +
                        "JOIN Bestellung b ON k.kundenId = b.kundenId " +
                        "GROUP BY k.kundenId"
        ).setCollocated(true);

        orderCache.query(totalQuery).getAll().forEach(row -> {
            String customerId = (String) row.get(0);
            Long orderCount = (Long) row.get(1);
            Double totalSpent = (Double) row.get(2);

            System.out.printf("%s: %d Bestellungen, Summe: €%.2f%n",
                    customerId, orderCount, totalSpent);
        });
    }
}
