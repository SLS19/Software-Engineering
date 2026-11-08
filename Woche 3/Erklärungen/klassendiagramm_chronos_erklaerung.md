# Klassendiagramm "Das Auge des Chronos" – Zum Nachschauen

Dieses Dokument fasst zusammen, was die Aufgabe war, wie wir sie gelöst haben und was du daraus mitnehmen solltest.

---

## 1. Ziel der Aufgabe

Du solltest ein **unvollständiges Klassendiagramm** (Makroebene) anhand einer **Textbeschreibung** vervollständigen:

- Assoziationen
- Aggregationen
- Kompositionen
- Vererbungen
- Multiplizitäten

**Lernziele:**

| Ebene | Was du können sollst |
|---|---|
| Verstehen | Die Beziehungstypen (Assoziation, Aggregation, Komposition, Vererbung) erklären können |
| Anwenden | Eine Textbeschreibung in korrekte UML-Beziehungen und Multiplizitäten übersetzen |
| Analysieren | Zusammenhänge zwischen Objekten erkennen und als strukturelle Beziehungen darstellen |

**Abgabe:** eine SVG-Datei (`class_chronos_loesung.svg`), erstellt auf Basis der Vorlage.

---

## 2. Die Beziehungstypen im Überblick

| Typ | Darstellung | Bedeutung | Merksatz |
|---|---|---|---|
| **Assoziation** | einfache Linie | Klassen kennen einander / arbeiten zusammen | "A hat etwas mit B zu tun" |
| **Gerichtete Assoziation** | Linie mit Pfeil | Nur eine Seite kennt die andere | "A kennt B, B kennt A nicht" |
| **Aggregation** | **leere** Raute am Ganzen | "Besteht aus", aber die Teile können **ohne** das Ganze existieren | Teile sind austauschbar / unabhängig |
| **Komposition** | **gefüllte** Raute am Ganzen | "Besteht aus", die Teile **leben und sterben** mit dem Ganzen | Ganzes weg → Teil weg |
| **Vererbung** | Linie mit **leerem Dreieck** an der Oberklasse | "ist ein" | Feuergefecht *ist eine* Konfrontation |

**Wichtig:** Die Raute (und das Dreieck) steht immer auf der Seite des **Ganzen** bzw. der **Oberklasse**.

### Multiplizitäten

Die Multiplizität steht am Linienende bei der Klasse, auf die sie sich bezieht. Sie beantwortet die Frage: *"Wie viele Objekte dieser Klasse gehören zu einem Objekt der anderen Klasse?"*

| Schreibweise | Bedeutung |
|---|---|
| `1` | genau eins |
| `0..1` | keins oder eins (optional) |
| `0..*` | beliebig viele, auch keins |
| `1..*` | mindestens eins |
| `2..5` | zwischen zwei und fünf |

**Trick zum Lesen:** Stell dir immer ein Objekt der einen Klasse vor und frag: "Wie viele von der anderen Klasse hat es?"
Beispiel: *Eine Mission hat 1 bis 3 Spezialeinheiten* → `1..3` steht an der Spezialeinheit.

---

## 3. Wie wir vorgegangen sind

### Schritt 1: Text in Sätze zerlegen
Jeder Satz der Beschreibung enthält meist **eine Beziehung**. Wir haben den Text Satz für Satz durchgegangen und gefragt:
1. Welche zwei Klassen sind beteiligt?
2. Was für eine Beziehung ist das (kennt, besteht aus, ist ein)?
3. Wie viele Objekte stehen auf jeder Seite?

### Schritt 2: Signalwörter erkennen

| Im Text steht... | Heißt wahrscheinlich... |
|---|---|
| "Zusammenschluss aus", "besteht aus" | Aggregation oder Komposition |
| "kann auch ohne ... existieren", "wechseln" | Aggregation (Teile sind unabhängig) |
| "gehört nur zu", "existiert nur mit" | Komposition |
| "kann ein ... sein", "z.B. A, B oder C" | Vererbung |
| "arbeitet mit", "setzt ein", "beteiligt" | Assoziation |
| "mindestens", "bis zu", "genau" | Multiplizität |

### Schritt 3: Vorlage prüfen
Die Vorlage hatte schon elf Klassen. Die Vererbungen brauchten **zusätzliche Kästen** (Feuergefecht, Hackangriff, Täuschung, Kriegerische und Friedliche Fraktion), weil der Text diese Unterarten nennt.

### Schritt 4: SVG erstellen
Die Datei wurde direkt als SVG-Code geschrieben (Kästen, Linien, Rauten, Dreiecke, Beschriftungen). Du kannst sie in Inkscape oder DrawIO öffnen und anpassen.

---

## 4. Die Lösung im Detail

| Nr. | Klasse A | Mult. A | Beziehung | Mult. B | Klasse B |
|---|---|---|---|---|---|
| 1 | Weltraum-Allianz | 0..1 | Aggregation | 2..* | Auftraggeber |
| 2 | Auftraggeber | 2 | Assoziation "initiiert" | 0..* | Mission |
| 3 | Mission | 1 | Komposition | 0..3 | Geheimes Ziel |
| 4 | Mission | 1 | Aggregation | 1..3 | Spezialeinheit |
| 5 | Spezialeinheit | 1 | Aggregation | 2..5 | Agent |
| 6 | Agent | 1 | Komposition | 1 | Geheimes Profil |
| 7 | Mission | 1..* | Assoziation "spielt an" | 1..* | Schauplatz |
| 8 | Schauplatz | 1 | Komposition | 1..* | Konfrontation |
| 9 | Konfrontation | 0..* | Assoziation "beteiligt" | 2..* | Kriegerische Fraktion |
| 10 | Fraktion | 1 | Gerichtete Assoziation "entwickelt" | 0..* | Ausrüstung |
| 11 | Fraktion | 0..* | Gerichtete Assoziation "nutzt" | 0..* | Ausrüstung |
| 12 | Konfrontation | 0..* | Gerichtete Assoziation "setzt ein" | 0..* | Ausrüstung |
| 13 | Feuergefecht, Hackangriff, Täuschung | – | Vererbung | – | Konfrontation |
| 14 | Kriegerische Fraktion, Friedliche Fraktion | – | Vererbung | – | Fraktion |

### Begründungen zu den wichtigsten Entscheidungen

**1 – Allianz → Auftraggeber (Aggregation, 0..1 und 2..\*)**
Die Allianz ist ein "Zusammenschluss", die Auftraggeber gibt es aber auch ohne sie → Aggregation. Ein Mitglied darf keine zweite Allianz eingehen → höchstens eine (`0..1`). Eine Mission braucht zwei Auftraggeber aus der Allianz → mindestens zwei (`2..*`).

**2 – Auftraggeber ↔ Mission (2 und 0..\*)**
"Eine Mission wird immer von zwei Auftraggebern initiiert" → auf der Auftraggeber-Seite steht `2`. Auftraggeber können gleichzeitig an mehreren Missionen arbeiten → auf der Mission-Seite `0..*`.

**3 – Mission → Geheimes Ziel (Komposition, 0..3)**
Das *primäre* Ziel ist ein Attribut der Mission. Die *alternativen* Ziele (bis zu drei) sind das Geheime Ziel. "Nicht davon auszugehen, dass mehrere Missionen das gleiche Ziel verfolgen" → ein Ziel gehört zu genau einer Mission und existiert nicht ohne sie → Komposition.

**4 – Mission → Spezialeinheit (Aggregation, 1..3)**
"Eine bis drei Spezialeinheiten" wird für eine Mission rekrutiert. Die Einheit könnte auch ohne die Mission weiterbestehen → Aggregation.

**5 – Spezialeinheit → Agent (Aggregation, 2..5)**
"Zwei bis fünf Agenten". Ein Agent hat schon in verschiedenen Einheiten gedient → er existiert unabhängig → Aggregation. Zu jedem Zeitpunkt gehört er aber genau einer Einheit an → auf der Einheit-Seite `1`.

**6 – Agent → Geheimes Profil (Komposition, 1)**
Das Profil (Deckname, wahre Loyalität, Spezialfähigkeiten) gibt es nur zusammen mit dem Agenten. Name und Rang sind öffentlich und daher Attribute von Agent selbst.

**7 – Mission ↔ Schauplatz (1..\* und 1..\*)**
Beide Richtungen sind "viele": eine Mission an mehreren Schauplätzen, ein Schauplatz in mehreren Missionen. Eine reine Assoziation, weil keiner dem anderen "gehört".

**8 – Schauplatz → Konfrontation (Komposition, 1..\*)**
An jedem Schauplatz gibt es mindestens eine Konfrontation. Eine Konfrontation findet an genau einem Ort statt und gehört nur dorthin.

**9 – Konfrontation ↔ Kriegerische Fraktion (2..\*)**
Mindestens zwei Fraktionen sind beteiligt. Friedliche Fraktionen gehen Konfrontationen aus dem Weg, deshalb hängt die Beziehung nur an der Unterklasse *Kriegerische Fraktion*.

**10 und 11 – Fraktion ↔ Ausrüstung**
Zwei verschiedene Beziehungen zwischen denselben Klassen:
- *entwickelt*: Jede Ausrüstung wird von genau einer Fraktion entwickelt (`1`).
- *nutzt*: Ausrüstung kann erbeutet werden und landet dann bei einer anderen Fraktion (`0..*` auf beiden Seiten).

**12 – Konfrontation → Ausrüstung**
Die Fraktionen setzen ihre Ausrüstung in der Konfrontation ein.

**13 und 14 – Vererbung**
Der Text nennt "ein Feuergefecht, ein Hackangriff oder eine Täuschung" → drei Unterklassen von Konfrontation. Außerdem gibt es kriegerische und friedliche Fraktionen → zwei Unterklassen von Fraktion.

---

## 5. Aggregation oder Komposition? – Der typische Stolperstein

Das ist der Punkt, der am häufigsten Diskussionen auslöst. Die Faustregel:

> **Kann das Teil ohne das Ganze existieren?**
> Ja → Aggregation (leere Raute)
> Nein → Komposition (gefüllte Raute)

Bei **Spezialeinheit → Agent** und **Mission → Spezialeinheit** ist beides vertretbar. Wichtig ist, dass du deine Wahl in der Abgabe **kurz begründest** (z. B. "Agenten wechseln die Einheit, deshalb Aggregation").

---

## 6. Typische Fehler (zum Vermeiden)

- **Raute auf der falschen Seite:** Sie gehört immer zum Ganzen.
- **Multiplizität auf der falschen Seite:** Sie steht bei der Klasse, die gezählt wird.
- **Vererbungsdreieck an der Unterklasse:** Es zeigt auf die Oberklasse.
- **Attribute als Klassen:** Name, Rang und das primäre Ziel sind Attribute, keine eigenen Klassen.
- **Alle Beziehungen als einfache Assoziation:** Die Aufgabe will, dass du die Typen unterscheidest.
- **Text wörtlich nehmen ohne nachzudenken:** "Mindestens zwei" heißt `2..*`, nicht `2`.

---

## 7. Checkliste für die nächste Aufgabe

1. Text in Sätze zerlegen, pro Satz eine Beziehung suchen.
2. Klassen und Attribute trennen (Was hat eigene Identität? Was ist nur ein Wert?).
3. Beziehungstyp bestimmen (kennt / besteht aus / ist ein).
4. Bei "besteht aus": Teil-Unabhängigkeit prüfen → Aggregation oder Komposition.
5. Multiplizität in **beide** Richtungen prüfen.
6. Oberklassen und Unterklassen aus Aufzählungen ("z. B. A, B oder C") ableiten.
7. Am Ende den Text noch einmal lesen und jeden Satz im Diagramm wiederfinden.

---

## 8. Dateien

- `class_chronos_loesung.svg` – das fertige Diagramm zur Abgabe
- `klassendiagramm_chronos_erklaerung.md` – dieses Dokument

**Tipp zur SVG-Datei:** Öffne sie in Inkscape oder DrawIO, wenn du Linien verschieben oder das Layout verschönern willst. Zwei Linien (nutzt, entwickelt) kreuzen die Linie "beteiligt", das ist inhaltlich in Ordnung.
