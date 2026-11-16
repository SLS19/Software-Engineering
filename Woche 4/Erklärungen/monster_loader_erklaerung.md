# Monster-Loader: So hättest Du die Aufgabe selbst gelöst

## 1. Was ist das Ziel?

Du sollst eine Textdatei einlesen und daraus `Monster`-Objekte bauen. Das ist ein typisches **Parsing-Problem**: Text rein, strukturierte Objekte raus. Das brauchst Du später ständig, z. B. bei Konfigurationsdateien, Spielständen oder CSV-Daten.

Die Aufgabe hat drei Kernanforderungen:

1. Datei öffnen und Zeile für Zeile lesen
2. Jeden Eintrag **prüfen**, bevor ein Objekt gebaut wird
3. Fehler **abfangen**, damit ein kaputter Eintrag nicht das ganze Programm stoppt

---

## 2. Das Dateiformat verstehen

```
Monster
name Kunibert
maxHP 80
attack 15
weight 10.0
multi 1.0
```

Ein Eintrag besteht aus **6 Zeilen**:

| Zeile | Inhalt | Typ |
|-------|--------|-----|
| 1 | `Monster` (Startmarke) | – |
| 2 | `name ...` | `str` |
| 3 | `maxHP ...` | `int` |
| 4 | `attack ...` | `int` |
| 5 | `weight ...` | `float` |
| 6 | `multi ...` | `float` |

Jede Wertzeile hat die Form **`Schlüssel Wert`**. Der Schlüssel muss genau stimmen, und die Reihenfolge ebenfalls.

**Wichtig:** Der Name kann Leerzeichen enthalten (`Kunibert der Heiler`). Du darfst die Zeile also nur beim **ersten** Leerzeichen teilen.

---

## 3. Die Bausteine

### 3.1 Datei lesen

```python
with open(file_path, "r", encoding="utf-8") as f:
    lines = [raw.strip() for raw in f if raw.strip()]
```

- `with open(...)` schließt die Datei automatisch, auch bei Fehlern.
- `strip()` entfernt Leerzeichen und Zeilenumbrüche am Rand.
- `if raw.strip()` wirft leere Zeilen weg. Danach hast Du nur noch Zeilen mit Inhalt.

### 3.2 Zeile in Schlüssel und Wert teilen

```python
parts = line.split(" ", 1)   # "name Kunibert der Heiler" -> ["name", "Kunibert der Heiler"]
```

Das `1` bedeutet: höchstens **einmal** teilen. Ohne die `1` würde der Name in mehrere Teile zerfallen.

### 3.3 Typen umwandeln

```python
int("80")       # 80
float("10.0")   # 10.0
int("120.0")    # ValueError!
```

Der letzte Fall ist wichtig. In `monster_fail.txt` steht `maxHP 120.0`. Das soll **abgelehnt** werden, und genau das erledigt `int()` für Dich, indem es eine Exception wirft. Du musst dafür nichts Zusätzliches prüfen.

### 3.4 Exceptions abfangen

```python
try:
    ...                 # etwas, das schiefgehen kann
except Exception:
    pass                # fangen, aber nichts damit tun
```

Die Aufgabe sagt: *„Exceptions müssen gecatched werden (aber nicht behandelt)."* Das heißt: `try/except` benutzen, im `except` aber nichts Besonderes tun (kein Programmabbruch, keine Fehlermeldung nötig).

---

## 4. Der Algorithmus Schritt für Schritt

1. **Leere Liste anlegen.** So gibst Du auch dann eine leere Liste zurück, wenn nichts geladen werden kann.
2. **Datei lesen** (in `try/except`, falls das Öffnen fehlschlägt).
3. **Durch die Zeilen laufen** mit einem Index `i`.
4. Steht an Position `i` **nicht** `Monster`, gehe eine Zeile weiter.
5. Steht dort `Monster`, nimm die **nächsten 5 Zeilen** als Block.
6. Hat der Block **keine 5 Zeilen**, ist der Eintrag unvollständig und wird übersprungen.
7. Prüfe pro Zeile, ob der **Schlüssel** zur erwarteten Position passt (`name`, `maxHP`, `attack`, `weight`, `multi`).
8. Wandle die Werte mit `int()` bzw. `float()` um.
9. Baue das `Monster` und hänge es an die Liste an.
10. Bei jedem Fehler in 6 bis 9 wird der Eintrag verworfen, und es geht mit dem nächsten weiter.

### Warum ein Index statt `for line in lines`?

Weil Du **vor- und zurückspringen** musst:

- Bei einem **gültigen** Eintrag springst Du 5 Zeilen weiter.
- Bei einem **ungültigen** Eintrag gehst Du nur eine Zeile weiter und suchst das nächste `Monster`. So wird ein kaputter Eintrag nie mit dem nächsten verwechselt.

---

## 5. Typische Stolperfallen

**Reihenfolge der Konstruktor-Parameter.** In der Datei steht `attack` vor `weight`, im Konstruktor von `Monster` steht aber `weight` **vor** `base_atk`:

```python
Monster(name, max_health, weight, base_atk, multiplier)
```

Wer die Werte einfach in Dateireihenfolge übergibt, vertauscht Gewicht und Angriff. Das wirft keinen Fehler, die Werte sind dann aber falsch. Lies deshalb immer die Signatur der Klasse.

**Negativer Angriff.** `attack -5` ist **gültig** (siehe `monster_ok.txt`). Der Heiler ist absichtlich so definiert. Prüfe also nicht auf `attack > 0`.

**Verdrehte Reihenfolge.** Im Fehlerbeispiel steht `attack` vor `maxHP`. Weil Du Zeile für Zeile den erwarteten Schlüssel vergleichst, wird das erkannt.

**Fehlende Werte.** `name` ohne Wert führt dazu, dass `split` nur ein Element liefert. Deshalb prüfst Du `len(parts) < 2`.

**Fehlende Datei-Ende-Zeilen.** Der letzte Eintrag hat evtl. keine Leerzeile danach. Weil Du leere Zeilen ohnehin entfernst, spielt das keine Rolle.

---

## 6. Die komplette Lösung

```python
from typing import List
from monster import Monster


class MonsterLoader:
    @staticmethod
    def load_monster_file(file_path: str) -> List[Monster]:
        monsters: List[Monster] = []
        keys = ["name", "maxHP", "attack", "weight", "multi"]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = [raw.strip() for raw in f if raw.strip()]
        except Exception:
            return monsters

        i = 0
        while i < len(lines):
            if lines[i] != "Monster":
                i += 1
                continue
            i += 1
            block = lines[i:i + 5]
            try:
                if len(block) != 5:
                    continue
                values = []
                for key, line in zip(keys, block):
                    parts = line.split(" ", 1)
                    if parts[0] != key or len(parts) < 2 or not parts[1].strip():
                        raise ValueError
                    values.append(parts[1].strip())
                monsters.append(
                    Monster(values[0], int(values[1]), float(values[3]),
                            int(values[2]), float(values[4]))
                )
                i += 5
            except Exception:
                pass
        return monsters
```

---

## 7. Konzepte, die Du mitnehmen solltest

- **Defensives Programmieren:** Eingaben von außen sind unzuverlässig. Prüfe sie, bevor Du sie benutzt.
- **Fail-soft:** Ein kaputter Eintrag soll nicht alles zerstören. Verwirf ihn und mach weiter.
- **Exceptions als Prüfwerkzeug:** `int("120.0")` ist ein einfacher Typ-Check, ohne dass Du selbst etwas schreiben musst.
- **`with`-Statement:** sicherer Umgang mit Ressourcen wie Dateien.
- **Lesbare Namen:** Der Flake8-Fehler E741 verbietet Namen wie `l`, weil sie leicht mit `1` oder `I` verwechselt werden.
- **`@staticmethod`:** Eine Methode, die keine Instanz (`self`) braucht, kann direkt über die Klasse aufgerufen werden.

---

## 8. Übungen zum Selbermachen

1. Schreibe eigene Testdateien mit weiteren Fehlern: doppelter Schlüssel, zusätzliche Zeile in einem Eintrag, leere Datei.
2. Ändere den Loader so, dass er bei verworfenen Einträgen eine Warnung mit der Zeilennummer ausgibt.
3. Schreibe das Gegenstück `save_monster_file`, das eine Liste von Monstern wieder in dieses Format schreibt.
4. Lade dieselben Daten aus **JSON** statt aus dem eigenen Textformat (Modul `json`) und vergleiche den Aufwand.
5. Baue einen Test mit `pytest`, der prüft, dass `monster_fail.txt` genau 3 Monster liefert.
