# Version Control II – Vorgehensweise

## 1. Git installieren
Git ist bereits installiert; die Version prüfe ich mit:

```bash
git --version
```

Falls es nicht installiert ist:
- Linux (Debian/Ubuntu): `sudo apt install git`
- macOS: `brew install git`
- Windows: Installer von https://git-scm.com

## 2. Repository klonen

```bash
git clone https://github.com/Thomas-Wilde/SE_IT-PM.git
cd SE_IT-PM
```

## 3. Repository-Struktur analysieren

```bash
git branch -a      # main, origin/java, origin/python
git log --oneline  # 2 Commits auf main
```

Struktur auf `main`:

```
SE_IT-PM/
├── README.md        <- Anleitung
├── .gitignore
└── task01/
    ├── c++/         <- C++-Lösung (relevant)
    │   ├── CMakeLists.txt
    │   ├── main.cc
    │   ├── logger.cc / logger.hh
    │   ├── load_stb.hh
    │   └── stb_image_write.h   (Bibliothek zum Schreiben von PNGs)
    ├── java/.keep   <- leer, Code liegt auf Branch "java"
    └── python/.keep <- leer, Code liegt auf Branch "python"
```

Erkenntnisse aus der README und dem Code:
- Das Programm erzeugt aus `data.dat` ein indiziertes Bild und schreibt `image.png`.
- `data.dat` wird über das E-Learning-System bereitgestellt und muss im **Ausführungsordner** liegen. Sie ist nicht im Repository enthalten.
- Das Format der Datei: Zeile 1 `indeximage`, dann Breite, Höhe, Anzahl der Farben, die Farbpalette (RGB) und zuletzt die Indizes der Pixel zeilenweise.
- Abhängigkeiten: C++17-Compiler (z. B. g++), optional CMake. `stb_image_write.h` liegt bereits im Ordner, es muss nichts nachinstalliert werden.

## 4. Projekt bauen

Variante A – mit CMake:

```bash
cd task01/c++
mkdir build && cd build
cmake ..
cmake --build .
```

Variante B – direkt mit g++ (ohne CMake):

```bash
cd task01/c++
mkdir build
g++ -std=c++17 -Wall main.cc logger.cc -o build/ImageGenerator
```

Das Projekt wurde ohne Fehler und ohne Warnungen kompiliert.

## 5. Programm ausführen

`data.dat` ins Build-Verzeichnis kopieren (dort wird das Programm gestartet) und ausführen:

```bash
cp /pfad/zu/data.dat build/
cd build
./ImageGenerator
```

Erwartete Ausgabe:

```
SE & IT-PM: Image generator -- C++ Version
==========================================
open file: successful
check filetype: correct
reading image size: successful
reading color palette: successful
write data to image... successful
```

Danach liegt `image.png` im Ordner `build/`.

## 6. Probleme
- Ohne `data.dat` bricht das Programm mit `open file: failed` ab. Die Datei muss im aktuellen Arbeitsverzeichnis liegen, nicht im Quellordner.
