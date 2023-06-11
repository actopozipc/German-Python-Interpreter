importiere mathe

def berechne_wurzel(n, genauigkeit=0.0001):
    schätzung = n / 2  # Starte mit einer Schätzung der Wurzel
    solange Wahr:
        nächste_schätzung = (schätzung + (n / schätzung)) / 2
        wenn abs(nächste_schätzung - schätzung) < genauigkeit:
            Rückkehr nächste_schätzung
        schätzung = nächste_schätzung

# Zahl
zahl = 2147483647  

# Berechnung der Wurzel
wurzel = berechne_wurzel(zahl)

# Ausgabe der Ergebnisse
drucke("Die Wurzel von", zahl, "ist:", wurzel)
vergleich = mathe.Wurzel(zahl)
drucke("Vergleich mit mathe.Wurzel:", vergleich)
