package de.bigdatabuch;

import java.io.Serializable;

public class SensorReading implements Serializable {
    private final int id;
    private final String city;
    private final double temperature;

    public SensorReading(int id, String city, double temperature) {
        this.id = id;
        this.city = city;
        this.temperature = temperature;
    }

    public int getId() { return id; }
    public String getCity() { return city; }
    public double getTemperature() { return temperature; }
}
