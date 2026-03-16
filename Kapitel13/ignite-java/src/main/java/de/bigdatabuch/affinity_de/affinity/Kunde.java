package de.bigdatabuch.affinity_de.affinity;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

import java.io.Serializable;

public class Kunde implements Serializable {
    @QuerySqlField(index = true)
    private final String kundenId; // Schlüssel, der für die Partitionierung verwendet wird
    @QuerySqlField(index = true)
    private String email;

    public Kunde(String kundenId, String email) {
        this.kundenId = kundenId;
        this.email = email;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getKundenId() {
        return kundenId;
    }
}