# Lernnotizen: Git-Aufgabe "Version Control II"

Zum Nachschlagen: Was war die Aufgabe, was haben wir gemacht, was solltest du daraus mitnehmen?

---

## 1. Worum ging es?

**Ziel der Aufgabe:** Mit Git praktisch arbeiten und ein fremdes, bereits bestehendes Projekt in Betrieb nehmen. So läuft es im Alltag der Softwareentwicklung oft ab: Man bekommt ein Repository, versteht es und bringt es zum Laufen.

**Die zwei Lernziele aus der Aufgabe:**

| Lernziel | Was das konkret hieß |
|---|---|
| **Anwenden** | Git benutzen (klonen, Branches ansehen, Historie lesen) und das Projekt kompilieren und ausführen |
| **Analysieren** | Die Repository-Struktur untersuchen, die README lesen und herausfinden, was das Projekt braucht (Abhängigkeiten, Eingabedatei) |

**Abgabe:** `image.png` (vom Programm erzeugt) und `version_control_ii.md` (kurze Beschreibung der Vorgehensweise).

---

## 2. Was haben wir gemacht? (Schritt für Schritt)

### Schritt 1: Git prüfen
```bash
git --version
```
Zeigt, ob Git installiert ist (bei uns Version 2.43.0).

### Schritt 2: Repository klonen
```bash
git clone https://github.com/Thomas-Wilde/SE_IT-PM.git
```
`clone` lädt das **komplette** Repository herunter: alle Dateien, die gesamte Historie und alle Branches. Es entsteht ein lokaler Ordner `SE_IT-PM`.

### Schritt 3: Struktur analysieren, bevor man etwas baut
```bash
git branch -a      # alle Branches anzeigen (lokal und remote)
git log --oneline  # Commit-Historie kurz anzeigen
```
Ergebnis:
- Branches: `main`, `origin/java`, `origin/python`
- Nur 2 Commits auf `main` (`.gitignore` und die Dateien für Task 01)
- Der Code für Java und Python liegt **nicht** auf `main`. Dort gibt es nur leere `.keep`-Dateien. Die README zeigt in der ToDo-Liste, dass das Mergen noch offen ist.

### Schritt 4: README lesen
Die README sagt:
- Das Programm erzeugt aus einer Datendatei ein **indiziertes Bild**.
- `data.dat` muss im **Ausführungsordner** liegen.
- Es gibt drei Versionen (C++, Java, Python). Wir haben die **C++-Version** genommen, weil sie auf `main` liegt und die Aufgabe sie verlangt.

### Schritt 5: Code ansehen und Abhängigkeiten finden
Im Ordner `task01/c++/`:

| Datei | Zweck |
|---|---|
| `CMakeLists.txt` | Build-Beschreibung für CMake (Projektname, Quelldateien, C++17) |
| `main.cc` | Hauptlogik: Datei einlesen, Bild erzeugen |
| `logger.cc` / `logger.hh` | Kleine Hilfsklasse für Konsolenausgaben |
| `stb_image_write.h` | Fertige Bibliothek zum Schreiben von PNG-Dateien (liegt schon im Projekt) |
| `load_stb.hh` | Bindet die stb-Bibliothek ein |

Abhängigkeiten: nur ein C++17-Compiler. CMake ist optional.

### Schritt 6: Kompilieren
Ich hatte kein CMake zur Verfügung, deshalb direkt mit dem Compiler:
```bash
g++ -std=c++17 -Wall main.cc logger.cc -o build/ImageGenerator
```
Das macht dasselbe wie die `CMakeLists.txt`: C++17, Warnungen an (`-Wall`) und die beiden `.cc`-Dateien kompilieren.
Mit CMake wäre es:
```bash
mkdir build && cd build
cmake ..
cmake --build .
```

### Schritt 7: Ausführen
```bash
cp data.dat build/
cd build
./ImageGenerator
```
Wichtig: Das Programm sucht `data.dat` im **aktuellen Arbeitsverzeichnis** (dort, wo man es startet).

Zuerst ohne `data.dat`: `open file: failed`. Danach mit `data.dat`: alle Schritte "successful", und `image.png` (500×500 Pixel) war da.

---

## 3. Wie funktioniert das Programm?

Die Datei `data.dat` hat dieses Format:

```
indeximage        <- Dateityp (wird geprüft)
500               <- Breite
500               <- Höhe
16                <- Anzahl Farben in der Palette
50 53 80          <- Farbe 0 (R G B)
...               <- weitere Farben
0 3 3 7 ...       <- Pixel-Zeilen: je Pixel ein Index in die Palette
```

**Indiziertes Bild:** Statt für jeden Pixel die RGB-Farbe zu speichern, speichert man nur eine kleine Zahl (Index). Die echten Farben stehen einmal in einer Palette. Das spart Speicher.

Ablauf im Code (`generateImage()` in `main.cc`):
1. `openFile`: `data.dat` öffnen
2. `checkFileType`: erste Zeile muss `indeximage` sein
3. `loadSize`: Breite und Höhe lesen
4. `loadColorPalette`: Palette lesen
5. `createImage`: für jeden Pixel den Index nachschlagen, RGB-Werte in ein Array schreiben und mit `stbi_write_png` als `image.png` speichern

---

## 4. Wichtige Git-Begriffe (Mini-Glossar)

| Begriff | Bedeutung |
|---|---|
| **Repository (Repo)** | Projektordner samt gesamter Versionshistorie |
| **Clone** | Lokale Kopie eines Remote-Repos anlegen |
| **Commit** | Gespeicherter Stand der Dateien mit Nachricht und Autor |
| **Branch** | Eigene Entwicklungslinie (hier: `main`, `java`, `python`) |
| **Remote / origin** | Das Repo auf dem Server (hier GitHub). `origin` ist der Standardname dafür |
| **Merge** | Zwei Branches zusammenführen |
| **`.gitignore`** | Liste von Dateien, die Git ignorieren soll (z. B. Build-Ordner) |
| **`.keep`** | Leere Platzhalterdatei, damit Git einen leeren Ordner speichert (Git speichert keine leeren Ordner) |

## 5. Nützliche Befehle zum Merken

```bash
git clone <url>          # Repo herunterladen
git status               # Was hat sich geändert?
git branch -a            # Alle Branches anzeigen
git checkout java        # Zu einem anderen Branch wechseln (oder: git switch java)
git log --oneline        # Kurze Historie
git pull                 # Neue Änderungen vom Remote holen
git add <datei>          # Änderung für den nächsten Commit vormerken
git commit -m "Nachricht"  # Commit erstellen
git push                 # Commits zum Remote hochladen
```

---

## 6. Was du daraus mitnehmen solltest

1. **Erst verstehen, dann bauen:** Struktur, README und `CMakeLists.txt` lesen, bevor man etwas kompiliert. Daraus erfährt man Abhängigkeiten und Voraussetzungen.
2. **README ist die erste Anlaufstelle** bei jedem fremden Projekt.
3. **Git speichert mehr als den aktuellen Stand:** Historie, Branches und Autoren. Mit `git branch -a` und `git log` sieht man, wo was liegt.
4. **Nicht alles liegt auf `main`:** Hier sind Java und Python in eigenen Branches.
5. **Eingabedateien und Arbeitsverzeichnis zählen:** Das Programm fand `data.dat` nur, weil sie im Startordner lag.
6. **Build-Systeme (CMake) vs. Compiler direkt:** CMake beschreibt den Build plattformunabhängig. `g++` direkt aufzurufen ist die Handarbeit dahinter.
7. **Fehlermeldungen lesen:** `open file: failed` war ein klarer Hinweis auf die fehlende Datei.

---

## 7. Beobachtung am Rande

Im erzeugten Bild sind feine Streifen und einzelne falsche Pixel zu sehen. Die Ursache liegt sehr wahrscheinlich im Code zum Einlesen der Pixelzeilen in `createImage`. Dort wird `substr(p0, p1)` benutzt, aber das zweite Argument von `substr` ist die **Länge** und nicht die Endposition. Das ist ein typischer Fehler und ein gutes Beispiel dafür, dass fremder Code Fehler enthalten kann. Für die Aufgabe musst du nichts ändern. Ändern würdest du so etwas in der Praxis auf einem eigenen Branch und schickst es per Pull Request.

---

## 8. Kleiner Selbsttest

1. Was macht `git clone` genau?
2. Wie findest du heraus, welche Branches es gibt?
3. Warum liegt `data.dat` nicht im Repository, und wohin muss sie?
4. Was ist ein indiziertes Bild und welchen Vorteil hat es?
5. Welchen Zweck hat die `CMakeLists.txt`?
6. Warum gibt es `.keep`-Dateien in `java/` und `python/`?

**Antworten (kurz):**
1. Lädt das ganze Repo samt Historie und Branches lokal herunter.
2. `git branch -a`
3. Sie wird über das E-Learning-System bereitgestellt. Sie muss ins Arbeitsverzeichnis, aus dem das Programm gestartet wird.
4. Pixel speichern nur einen Index in eine Farbpalette, das spart Speicher.
5. Sie beschreibt, wie das Projekt gebaut wird (Quelldateien, C++-Standard, Compiler-Optionen).
6. Git speichert keine leeren Ordner. Die leere Datei sorgt dafür, dass der Ordner existiert.
