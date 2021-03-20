# Bürger:innen-Daten-Finder
Dies ist ein proof of concpet, dass man ämterübergreifend protokollieren kann, welches Amt über welche Daten zu einer Person (Bürger:in) verfügt. Randbedingung ist, dass Ämter die Daten nicht zentral in einer Datenbank zusammenführen dürfen.

In der Datenbank wird dabei nur ein Hash aus Namen und Datumstyp (Telefonnummer, E-Mail, etc) gespeichert, sowie der Name des Amts und das Aktualisierungsdatum. Das bedeutet, dass in der zentralen Datenbank der Name und der Datentyp nicht direkt gespeichert werden. Die Sicherheit kann erhöht werden, indem beispielsweise noch ein Geburtsdatum oder eine Bürger:innen-ID mit zufälligem Anteil in den Hash mit einfließen.

Folgende weitere Funktionen wären leicht einzubauen:
* Jedem Hash einen weiteren zufälligen Wert (Salt) hinzufügen, um Hashes vor Brute Force Angriffen zu sichern. Dabei könnte es sich um einen Code handeln, den nur die Bürger:in speichert, und der nur für solche Anfragen temporär verarbeitet werden darf.
* Umstellung des Hashes auf Argon2id mit hohen Rechenzeiten.
* Bei jeder Suchanfrage eine Begründung abfragen und protokolliern.
