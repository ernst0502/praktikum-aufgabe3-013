# Aufgabe: Temperaturmessreihe auswerten
# Name: Schueler_013
# Letzte Änderung: 2026-10-22
# Zweck: Einlesen von sechs Temperaturwerten, Berechnung des Mittelwerts und Zählen der Werte ab 35 °C.
# Eingaben: Sechs Temperaturwerte (Gleitkommazahlen oder ganze Zahlen)
# Ausgaben: Berechneter Mittelwert und Anzahl der Temperaturen >= 35 °C
# Verwendete Konzepte: Variablen, while-Schleife, Verzweigungen (if/else), Rechenoperationen, Eingabe/Ausgabe
# PAP-Datei: aufgabe3_pap.docx
# GitHub-Repository: python-uebung-3

# Ab hier beginnt das Programm.

# Initialisierung der Variablen für Summe, Zähler und Schleifendurchläufe
summe = 0
anzahl_35 = 0
zaehler = 0

while zaehler < 6:
    # Temperatur einlesen (Eingabe) und in eine Kommazahl umwandeln
    temp = float(input("Gib eine Temperatur ein: "))
    
    # Zähler und Summe innerhalb der Schleife erhöhen (Vorgang)
    zaehler = zaehler + 1
    summe = summe + temp
    
    # Prüfen, ob die Temperatur mindestens 35 °C beträgt (Entscheidung)
    if temp >= 35:
        anzahl_35 = anzahl_35 + 1

# Mittelwert nach Ende der Schleife berechnen (Vorgang)
mittelwert = summe / 6

# Ergebnisse ausgeben (Ausgabe)
print("Der Mittelwert der Temperaturen beträgt:", mittelwert)
print("Anzahl der Messwerte >= 35 °C:", anzahl_35)