from datetime import datetime, timedelta
import random
import math

def generate_line_protocol():
    city = "Ingolstadt"
    station = "Muenchener_Strasse"
    measurement = "air_quality"
    base_time = datetime.now()

    with open("air_quality.lp", "w", newline="\n", encoding="utf-8") as f:
        for i in range(24 * 60):  # 24 Stunden, jede Minute
            timestamp = base_time - timedelta(minutes=i)
            ts_ns = int(timestamp.timestamp() * 1e9)
            hour = timestamp.hour + timestamp.minute / 60.0

            # Tagesverlauf mit grob realistischen Mustern
            rush_hour = (
                math.exp(-((hour - 8) ** 2) / 4) +
                math.exp(-((hour - 17) ** 2) / 4)
            )
            daytime = math.exp(-((hour - 14) ** 2) / 18)

            no2 = round(20 + 25 * rush_hour + random.uniform(-3, 3), 1)
            pm10 = round(12 + 18 * rush_hour + random.uniform(-4, 4), 1)
            pm25 = round(8 + 10 * rush_hour + random.uniform(-2, 2), 1)
            ozon = round(30 + 45 * daytime + random.uniform(-5, 5), 1)

            # Negative Werte vermeiden
            no2 = max(no2, 0.0)
            pm10 = max(pm10, 0.0)
            pm25 = max(pm25, 0.0)
            ozon = max(ozon, 0.0)

            line = (
                f"{measurement},city={city},station={station} "
                f"NO2={no2},PM10={pm10},PM2_5={pm25},Ozon={ozon} {ts_ns}"
            )
            f.write(line + "\n")

            if i == 0:
                print("Beispielzeile:", line)

if __name__ == "__main__":
    generate_line_protocol()