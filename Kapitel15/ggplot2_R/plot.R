# Benötigte Pakete laden (ggf. zuerst installieren mit install.packages("tidyverse"))
library(dplyr)
library(ggplot2)

# 1. & 2. Data Frame (in R "tibble") erstellen und transformieren
sales_data <- tibble(
  Datum = as.Date(c('2023-11-01', '2023-11-02', '2023-11-03', '2023-11-04',
                    '2023-11-05', '2023-11-06', '2023-11-07')),
  Verkaeufe = c(150, 175, 160, 210, 205, 180, 195)
)

# 3. Visualisierung
# Die Grafik wird durch das Hinzufügen von "Schichten" (layers) aufgebaut.
plot <- ggplot(data = sales_data, aes(x = Datum, y = Verkaeufe)) +
  geom_line(color = "steelblue") +  # Fügt die Linie hinzu
  geom_point(color = "steelblue") + # Fügt die Punkte hinzu
  labs(                               # Fügt Titel und Achsenbeschriftungen hinzu
    title = "Tägliche Verkäufe im November 2023",
    x = "Datum",
    y = "Anzahl der Verkäufe"
  ) +
  theme_minimal() # Wendet ein sauberes, minimalistisches Design an

ggsave(
  filename = "line.png", # Dateiname und -typ
  width = 10, # Breite des Bildes
  height = 5, # Hoehe des Bildes
  plot = plot, # Das zu speichernde Plot-Objekt
)