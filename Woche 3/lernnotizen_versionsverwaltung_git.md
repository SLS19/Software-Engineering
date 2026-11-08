# Lernnotizen: Versionsverwaltung mit Git

## 1. Ziel der Aufgabe

In dieser Aufgabe wurden grundlegende Konzepte der Versionsverwaltung behandelt. Im Mittelpunkt standen:

- Gründe für den Einsatz eines Versionsverwaltungssystems
- der konzeptionelle Unterschied zwischen Git und Apache Subversion (SVN)
- wichtige Git-Befehle für den alltäglichen Entwicklungsablauf

Das übergeordnete Lernziel ist, nicht nur einzelne Befehle auswendig zu kennen, sondern zu verstehen, wie Änderungen in Git von der Arbeitskopie bis zum Remote Repository gelangen.

---

## 2. Aufgabe 1: Warum Versionsverwaltung?

### Das Problem

Bei der Softwareentwicklung verändern sich Dateien ständig. Ohne Versionsverwaltung wird es schwierig,

- ältere Entwicklungsstände wiederherzustellen,
- nachzuvollziehen, wer welche Änderung vorgenommen hat,
- Fehler auf bestimmte Änderungen zurückzuführen,
- mehrere Entwicklungsarbeiten zusammenzuführen,
- parallel an unterschiedlichen Funktionen zu arbeiten.

Man könnte Dateien zwar manuell kopieren und beispielsweise `projekt_alt`, `projekt_neu` und `projekt_neu_final` nennen. Das wird allerdings schnell unübersichtlich und ist keine zuverlässige Versionsverwaltung.

### Lösung: Versionsverwaltungssystem

Ein Versionsverwaltungssystem wie Git speichert Änderungen in nachvollziehbaren Versionen. Eine gespeicherte Version heißt in Git **Commit**.

Wichtige Vorteile:

1. **Nachvollziehbarkeit:** Änderungen und ihre Entwicklungsgeschichte können untersucht werden.
2. **Wiederherstellung:** Frühere Entwicklungsstände können wiederhergestellt werden.
3. **Zusammenarbeit:** Mehrere Entwickler können an einem Projekt arbeiten und Änderungen zusammenführen.
4. **Parallele Entwicklung:** Branches ermöglichen unabhängige Entwicklungszweige.
5. **Schutz vor versehentlichem Verlust:** Frühere Commits bleiben als Entwicklungsgeschichte erhalten.

### Was du lernen solltest

Versionsverwaltung ist nicht bloß ein Backup. Sie dokumentiert die Entwicklung eines Projekts und unterstützt die Zusammenarbeit. Ein Commit ist dabei ein gespeicherter Zustand beziehungsweise Änderungssatz in der Versionshistorie.

---

## 3. Aufgabe 2: Git und SVN

### Das Problem

Git und SVN erfüllen einen ähnlichen Zweck: Sie verwalten Änderungen an Dateien und ermöglichen es, frühere Versionen nachzuvollziehen. Der grundlegende Unterschied liegt darin, **wo und wie die Versionshistorie verwaltet wird**.

### Git: Verteilte Versionsverwaltung

Git ist ein *Distributed Version Control System* (DVCS).

- Jeder Entwickler besitzt nach dem Klonen eine vollständige lokale Kopie des Repositorys.
- Dazu gehört auch die Versionshistorie.
- Commits können lokal erstellt werden, ohne mit einem Server verbunden zu sein.
- Über einen Remote-Server können Entwickler ihre Änderungen später austauschen.

### SVN: Zentralisierte Versionsverwaltung

Apache Subversion (SVN) ist ein *Centralized Version Control System* (CVCS).

- Die zentrale Versionshistorie liegt auf einem Server.
- Entwickler arbeiten normalerweise mit einer lokalen Arbeitskopie der Dateien.
- Für zentrale Versionsverwaltungsvorgänge wird mit dem Server kommuniziert.

### Der konzeptionelle Unterschied

| Git | SVN |
|---|---|
| Verteiltes Versionsverwaltungssystem | Zentralisiertes Versionsverwaltungssystem |
| Jeder Klon enthält ein vollständiges Repository samt Historie | Die zentrale Historie liegt auf dem Server |
| Lokale Commits sind ohne Serververbindung möglich | Zentrale Versionsverwaltung ist stärker an den Server gebunden |

**Merksatz:** Git verteilt die vollständige Versionsverwaltung auf die Entwickler. SVN verwaltet die Versionshistorie zentral auf einem Server.

### Was du lernen solltest

Der Unterschied ist nicht einfach „Git ist lokal und SVN ist online“. Auch Git kann mit einem zentralen Remote Repository arbeiten. Entscheidend ist: Ein Git-Klon enthält die vollständige Historie und ermöglicht eigenständige lokale Commits. Eine SVN-Arbeitskopie ist dagegen kein vollständiges Abbild des zentralen Repositorys.

---

## 4. Aufgabe 3: Wichtige Git-Befehle

### 4.1 Neues lokales Repository erstellen

```bash
git init
```

Initialisiert im aktuellen Verzeichnis ein neues Git-Repository. Git legt dazu unter anderem das interne Verzeichnis `.git` an.

### 4.2 Bestehendes Repository als Arbeitskopie erstellen

```bash
git clone <repository-url>
```

Kopiert ein bestehendes Repository einschließlich seiner Versionshistorie auf den eigenen Rechner.

`<repository-url>` steht für die Adresse des Repositorys. Die spitzen Klammern sind Platzhalter und werden nicht wörtlich eingegeben.

### 4.3 Änderungen für einen Commit erfassen

```bash
git add .
```

Fügt Änderungen aus dem aktuellen Verzeichnis und seinen Unterverzeichnissen zur sogenannten **Staging Area** hinzu.

Wichtig: `git add` erstellt noch keinen Commit. Es bereitet Änderungen für den nächsten Commit vor. Einzelne Dateien lassen sich gezielt hinzufügen:

```bash
git add dateiname
```

### 4.4 Änderungen an den Main-Branch des Remote Repository senden

```bash
git push origin main
```

Überträgt lokale Commits des Branches `main` zum Remote Repository `origin`.

Voraussetzung ist, dass das Remote Repository eingerichtet ist und der lokale Branch die entsprechenden Commits enthält.

### 4.5 Neue Änderungen aus dem Remote Repository übernehmen

```bash
git pull origin main
```

Ruft Änderungen vom Remote Repository `origin` aus dessen Branch `main` ab und integriert sie in den aktuell ausgecheckten lokalen Branch.

`git pull` entspricht im üblichen Ablauf einem `git fetch` und anschließendem Zusammenführen beziehungsweise Integrieren der abgerufenen Änderungen.

### 4.6 Branch `other` erstellen und zu ihm wechseln

```bash
git switch -c other
```

Erstellt den Branch `other` und wechselt direkt zu diesem Branch.

Die ältere, ebenfalls verbreitete Schreibweise lautet:

```bash
git checkout -b other
```

### 4.7 Branch `other` in `main` zusammenführen

Zuerst muss man sich auf `main` befinden:

```bash
git switch main
```

Danach wird `other` in den aktuell ausgecheckten Branch `main` integriert:

```bash
git merge other
```

Wichtig: `git merge other` führt den Branch `other` in den Branch zusammen, auf dem man sich gerade befindet. Deshalb muss `main` vorher ausgecheckt sein.

### 4.8 Neue Datei `new_file` zur Versionsverwaltung hinzufügen

```bash
git add new_file
```

Fügt die neue Datei zur Staging Area hinzu. Damit wird sie für den nächsten Commit vorgemerkt.

Erst mit einem anschließenden Commit wird die Datei Bestandteil der gespeicherten Versionshistorie:

```bash
git commit -m "Neue Datei hinzufügen"
```

### 4.9 Status geänderter und neuer Dateien anzeigen

```bash
git status
```

Zeigt den Zustand der Arbeitskopie und der Staging Area. Dabei werden unter anderem angezeigt:

- geänderte, aber noch nicht gestagte Dateien,
- neue, noch nicht versionierte Dateien,
- bereits gestagte Änderungen,
- Änderungen, die noch nicht committed wurden.

Eine kompaktere Ausgabe erhält man mit:

```bash
git status --short
```

---

## 5. Das zentrale Git-Modell: Vom Bearbeiten zum Commit

Ein besonders wichtiges Konzept ist die Unterscheidung zwischen Arbeitsverzeichnis, Staging Area und Repository.

1. **Working Directory (Arbeitsverzeichnis):** Hier bearbeitest und erstellst du Dateien.
2. **Staging Area (Index):** Hier legst du fest, welche Änderungen in den nächsten Commit aufgenommen werden sollen.
3. **Local Repository:** Hier werden die Änderungen durch einen Commit dauerhaft in der lokalen Versionshistorie gespeichert.
4. **Remote Repository:** Hierhin können Commits übertragen werden, damit andere Entwickler sie erhalten.

Der typische Ablauf sieht so aus:

```text
Datei bearbeiten
      |
      v
git add .
      |
      v
Staging Area
      |
      v
git commit -m "Beschreibung"
      |
      v
Lokales Repository
      |
      v
git push origin main
      |
      v
Remote Repository
```

### Die wichtigsten Unterschiede

| Befehl | Aufgabe |
|---|---|
| `git add` | Änderungen für den nächsten Commit vormerken |
| `git commit` | Vorgemerkte Änderungen lokal speichern |
| `git push` | Lokale Commits zum Remote Repository übertragen |
| `git pull` | Änderungen vom Remote Repository abrufen und integrieren |
| `git status` | Zustand von Arbeitsverzeichnis und Staging Area anzeigen |

**Merke:** `add` ist nicht dasselbe wie `commit`. `commit` ist nicht dasselbe wie `push`.

---

## 6. Was du aus der Aufgabe mitnehmen solltest

Wenn du nur die wichtigsten Erkenntnisse behalten möchtest, dann diese:

- Ein Versionsverwaltungssystem dokumentiert Änderungen und ermöglicht die Wiederherstellung älterer Entwicklungsstände.
- Git ist verteilt, SVN zentralisiert.
- `git init` erstellt ein neues Repository.
- `git clone` kopiert ein bestehendes Repository.
- `git add` nimmt Änderungen in die Staging Area auf.
- `git commit` speichert diese Änderungen in der lokalen Historie.
- `git push` überträgt lokale Commits zum Remote Repository.
- `git pull` holt Änderungen vom Remote Repository und integriert sie.
- `git switch -c` erstellt einen Branch und wechselt zu ihm.
- `git merge` führt einen anderen Branch in den aktuell ausgecheckten Branch zusammen.
- `git status` zeigt den aktuellen Zustand der Dateien.

## 7. Typische Fehler und Stolperfallen

1. **`git add` mit `git commit` verwechseln:** `add` staged Änderungen nur. Erst `commit` speichert sie in der lokalen Versionshistorie.
2. **`git push` ohne Commit erwarten:** Nicht committete Änderungen werden durch `push` nicht übertragen.
3. **Beim Mergen auf dem falschen Branch stehen:** `git merge other` integriert `other` in den aktuell ausgecheckten Branch. Für die Aufgabe muss das also `main` sein.
4. **`git pull` mit `git push` verwechseln:** `pull` holt Änderungen, `push` sendet eigene Commits.
5. **`git add .` unüberlegt verwenden:** Der Befehl kann alle Änderungen im aktuellen Verzeichnisbereich stagen. Mit `git add dateiname` lässt sich gezielter arbeiten.

---

## 8. Kompakte Befehlsübersicht

| Ziel | Git-Befehl |
|---|---|
| Neues Repository erstellen | `git init` |
| Repository klonen | `git clone <repository-url>` |
| Änderungen stagen | `git add .` |
| Commit erstellen | `git commit -m "Nachricht"` |
| Commits übertragen | `git push origin main` |
| Änderungen abrufen und integrieren | `git pull origin main` |
| Branch erstellen und wechseln | `git switch -c other` |
| Branch wechseln | `git switch main` |
| Branch zusammenführen | `git merge other` |
| Neue Datei stagen | `git add new_file` |
| Status anzeigen | `git status` |
