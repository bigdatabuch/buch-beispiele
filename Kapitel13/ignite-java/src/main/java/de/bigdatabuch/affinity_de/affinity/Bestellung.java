package de.bigdatabuch.affinity_de.affinity;

import org.apache.ignite.cache.affinity.AffinityKeyMapped;
import org.apache.ignite.cache.query.annotations.QuerySqlField;

import java.io.Serializable;
import java.util.Date;

public class Bestellung implements Serializable {
    @QuerySqlField(index = true)
    private final String bestellungId; // Eigener Schlüssel

    @AffinityKeyMapped // wichtige Annotation!
    @QuerySqlField(index = true)
    private final String kundenId; // Schlüssel, der für die Partitionierung verwendet wird

    @QuerySqlField
    private final double betrag;
    @QuerySqlField
    private final Date bestellDatum;

    public Bestellung(String bestellungId, String kundenId, double betrag, Date bestellDatum) {
        this.bestellungId = bestellungId;
        this.kundenId = kundenId;
        this.betrag = betrag;
        this.bestellDatum = bestellDatum;
    }

    public String getBestellungId() {
        return bestellungId;
    }

    public String getKundenId() {
        return kundenId;
    }

    public double getBetrag() {
        return betrag;
    }

    public Date getBestellDatum() {
        return bestellDatum;
    }
}