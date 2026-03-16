# Kapitel 15: R (ggplot2)

Dieses Verzeichnis enthält ein Beispiel für die Erstellung von Visualisierungen mit R und ggplot2.

## Beispiel: Liniendiagramm mit täglichen Verkaufszahlen

Das Skript `plot.R` zeigt, wie man mit `ggplot2` ein Liniendiagramm für tägliche Verkaufszahlen erstellt.

### Voraussetzungen

Installieren Sie die benötigten R-Pakete:

```r
install.packages(c("dplyr", "ggplot2"))
```

### Ausführen

```bash
Rscript plot.R
```

Das Skript erzeugt eine PNG-Datei `line.png` mit dem Diagramm.

### Details

Das Beispiel basiert auf dem deklarativen Ansatz der Grammar of Graphics von ggplot2. Die Visualisierung wird Schicht für Schicht aufgebaut:

- Basisschicht (`ggplot`) definiert die Daten und Ästhetik
- `geom_line()` fügt die Linie hinzu
- `geom_point()` fügt die Punkte hinzu
- `labs()` fügt Titel und Achsenbeschriftungen hinzu
- `theme_minimal()` wendet ein sauberes Design an

Weitere Informationen finden Sie im Buch.
