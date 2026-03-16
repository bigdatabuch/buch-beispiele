package de.bigdatabuch;

import org.apache.ignite.cache.query.annotations.QuerySqlField;

import java.io.Serializable;

public class SensorReadingSQL implements Serializable {
    @QuerySqlField(index = true)
    private final int id;
    @QuerySqlField(index = true)
    private final String city;
    @QuerySqlField
    private final double temperature;

    public SensorReadingSQL(int id, String city, double temperature) {
        this.id = id;
        this.city = city;
        this.temperature = temperature;
    }

    public int getId() { return id; }
    public String getCity() { return city; }
    public double getTemperature() { return temperature; }
}
