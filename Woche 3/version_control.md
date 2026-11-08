Lösung: Versionsverwaltung mit Git
Aufgabe 1 – Warum sollte man ein Versionsverwaltungssystem benutzen?
Ein Versionsverwaltungssystem wie Git bietet mehrere wichtige Vorteile:
1. Nachvollziehbarkeit von Änderungen: Es dokumentiert, welche Änderungen vorgenommen wurden und wie sich ein Projekt entwickelt hat.
2. Wiederherstellung älterer Versionen: Wenn eine Änderung Fehler verursacht, kann man auf einen früheren Entwicklungsstand zurückgreifen.
3. Zusammenarbeit im Team: Mehrere Entwickler können gleichzeitig an einem Projekt arbeiten und ihre Änderungen später zusammenführen.
4. Parallele Entwicklung: Mit Branches können neue Funktionen unabhängig vom Hauptentwicklungszweig entwickelt und getestet werden.
5. Schutz vor versehentlichem Verlust: Frühere Entwicklungsstände bleiben in der Versionshistorie erhalten.
Zusammenfassung: Versionsverwaltung macht die Softwareentwicklung nachvollziehbarer, sicherer und erleichtert die Zusammenarbeit. Sie ermöglicht es, Änderungen zu dokumentieren, ältere Zustände wiederherzustellen und parallel an verschiedenen Funktionen zu arbeiten.
Aufgabe 2 – Git vs. Apache Subversion (SVN)
Der wesentliche konzeptionelle Unterschied liegt darin, wie die beiden Systeme ihre Versionsverwaltung organisieren:
- Git ist ein verteiltes Versionsverwaltungssystem (Distributed Version Control System, DVCS). Jeder Entwickler besitzt eine vollständige lokale Kopie des Repositorys einschließlich der Versionshistorie. Änderungen können lokal vorgenommen und committed werden, ohne dass eine Verbindung zum Server erforderlich ist. Später können die Änderungen mit einem Remote Repository ausgetauscht werden.
- Apache Subversion (SVN) ist ein zentralisiertes Versionsverwaltungssystem (Centralized Version Control System, CVCS). Die zentrale Versionshistorie wird auf einem Server verwaltet. Entwickler arbeiten normalerweise mit einer lokalen Arbeitskopie der Dateien und greifen für zentrale Versionsverwaltungsvorgänge auf den Server zu.
Zusammenfassung: Git verteilt die vollständige Versionsverwaltung auf die Entwickler. SVN verwaltet die Versionshistorie zentral auf einem Server.
Aufgabe 3 – Git-Befehle
1. Ein neues lokales Repository erstellen
git init
Initialisiert im aktuellen Verzeichnis ein neues Git-Repository.
2. Eine Arbeitskopie eines bestehenden Repositorys erstellen
git clone <repository-url>
Kopiert ein bestehendes Repository einschließlich seiner Versionshistorie auf den eigenen Rechner.
3. Veränderte Dateien für einen Commit erfassen
git add .
Fügt Änderungen im aktuellen Verzeichnis und seinen Unterverzeichnissen zur Staging Area hinzu. Die Änderungen sind damit für den nächsten Commit vorgemerkt, aber noch nicht committed.
4. Erfasste Änderungen an den Main-Branch des Remote Repository schicken
git push origin main
Überträgt lokale Commits des Branches main zum Remote Repository origin.
5. Neue Änderungen aus dem Remote Repository in die Arbeitskopie übernehmen
git pull origin main
Ruft Änderungen vom Remote Repository origin aus dessen Branch main ab und integriert sie in den aktuell ausgecheckten lokalen Branch.
6. Einen neuen Branch namens other erstellen und zu diesem wechseln
git switch -c other
Erstellt den Branch other und wechselt direkt zu diesem Branch.
7. Den Branch other mit dem Branch main zusammenführen
Zuerst auf den Branch main wechseln:
git switch main
Anschließend den Branch other in main integrieren:
git merge other
Wichtig: git merge other führt other in den aktuell ausgecheckten Branch zusammen. Deshalb muss man sich vorher auf main befinden.
8. Eine neue Datei new_file zur Versionsverwaltung hinzufügen
git add new_file
Fügt die neue Datei zur Staging Area hinzu. Damit ist sie für den nächsten Commit vorgemerkt. Erst ein anschließender Commit nimmt sie in die gespeicherte Versionshistorie auf.
9. Eine Übersicht geänderter oder neu erstellter Dateien anzeigen, die noch nicht committed oder hinzugefügt sind
git status
Zeigt den aktuellen Zustand des Arbeitsverzeichnisses und der Staging Area. Dazu gehören unter anderem geänderte Dateien, neue und noch nicht versionierte Dateien sowie bereits vorgemerkte Änderungen.
Kurzübersicht
Nr.	Aufgabe	Git-Befehl
1	Neues lokales Repository erstellen	git init
2	Bestehendes Repository kopieren	git clone <repository-url>
3	Änderungen für einen Commit erfassen	git add .
4	Änderungen an Remote-Main senden	git push origin main
5	Änderungen vom Remote-Main übernehmen	git pull origin main
6	Branch other erstellen und wechseln	git switch -c other
7	other in main zusammenführen	git merge other
8	Neue Datei hinzufügen	git add new_file
9	Status der Dateien anzeigen	git status