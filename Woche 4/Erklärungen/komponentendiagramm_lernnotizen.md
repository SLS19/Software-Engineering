# Komponentendiagramm – Lernnotizen zur Aufgabe „Mischpult“

Diese Notizen fassen zusammen, was du beim Selberlösen der Aufgabe hättest lernen und verstehen sollen.

---

## 1. Worum geht es in der Aufgabe?

Ein Komponentendiagramm (UML) zeigt, **aus welchen Bausteinen ein System besteht** und **wie diese Bausteine über Schnittstellen (Interfaces) zusammenarbeiten**.

Im Vergleich zum Klassendiagramm:

| Klassendiagramm | Komponentendiagramm |
|---|---|
| Zeigt Klassen, Attribute, Methoden | Zeigt große Bausteine (Komponenten) |
| Detailebene: Code-Struktur | Architekturebene: Zusammenspiel |
| Beziehungen: Vererbung, Assoziation | Beziehungen: Schnittstellen (bereitgestellt/benötigt) |

**Lernziel der Aufgabe:** Zwischen *Komponenten*, *bereitgestellten Interfaces* und *benötigten Interfaces* sicher unterscheiden.

---

## 2. Die Grundbausteine der Notation

### Komponente
Ein Rechteck mit dem Stereotyp `«component»` und dem kleinen Komponenten-Symbol oben rechts.

### Bereitgestelltes Interface (Provided Interface, „Lollipop“)
Ein **Kreis** am Ende einer kurzen Linie. Die Komponente **bietet** diese Schnittstelle an.

### Benötigtes Interface (Required Interface, „Socket“)
Ein **Halbkreis**. Die Komponente **braucht** diese Schnittstelle von einer anderen Komponente.

### Assembly-Konnektor („Ball-and-Socket“)
Passt ein Halbkreis um einen Kreis, sind zwei Komponenten über das Interface **verbunden**.

```
  Anbieter ──○)── Nutzer
   (Kreis)  (Halbkreis)
```

### Verschachtelung
Komponenten können **innerhalb** anderer Komponenten liegen (Teil-von-Beziehung).

### Externe Elemente
Dinge außerhalb des Systems (z. B. ein fremder Computer oder ein externer Sensor) werden außerhalb der Systemgrenze gezeichnet, oft gestrichelt oder mit `«extern»` / `«device»` markiert.

---

## 3. Lösungsweg Schritt für Schritt

### Schritt 1: Komponenten aus dem Text herausschreiben
Markiere alle Substantive, die Bausteine sind:

- Mixer
- Mikrofon
- Musik-App (auf einem externen Computer)
- Soundsystem
  - Lautsprecher
  - Subwoofer
- dB Sensor (extern)

### Schritt 2: Interfaces herausschreiben
- **Input** (Eingabe in den Mixer)
- **SoundChange** (Weitergabe an das Soundsystem)

### Schritt 3: Für jedes Interface klären, wer anbietet und wer nutzt

Der Trick: Frage dich immer, **in welche Richtung die Daten bzw. Anfragen fließen**.

| Interface | Bietet an (Kreis) | Braucht (Halbkreis) |
|---|---|---|
| **Input** | Mixer | Mikrofon, Musik-App |
| **SoundChange** | Soundsystem | Mixer, dB Sensor |

Begründung:
- Mikrofon und Musik-App **liefern** Sound an den Mixer, also brauchen sie dessen Eingang.
- Der Mixer **gibt** den bearbeiteten Sound ans Soundsystem weiter, also braucht er dessen Schnittstelle.
- Der dB Sensor **meldet** Lautstärke an das Soundsystem, also braucht er ebenfalls *SoundChange*.

### Schritt 4: Struktur zeichnen
1. Mixer, Mikrofon, Musik-App, dB Sensor als einzelne Komponenten.
2. Soundsystem als größere Komponente mit Lautsprecher und Subwoofer **darin**.
3. Musik-App in einen Kasten „Externer Computer“ setzen.
4. dB Sensor als extern kennzeichnen.
5. Interfaces mit Kreis und Halbkreis verbinden und beschriften.

---

## 4. Die Stolperfalle: uneindeutige Formulierung

Der Aufgabentext verwendet die Wörter **uneinheitlich**:

- „bereitstellen“ / „anbieten“ → meint den **Kreis**
- „implementieren“ / „zugreifen“ → meint hier den **Halbkreis**

In der strengen UML-Sprache bedeutet „implementiert“ eigentlich „bietet an“. Der Text nutzt es aber für die **nutzende** Seite. Wörtlich genommen würde das Mikrofon *Input* anbieten, obwohl der Mixer das Interface bereitstellt. Das wäre ein Widerspruch.

**Was du daraus mitnehmen sollst:**
- Wenn der Text mehrdeutig ist, entscheidet die **Logik des Szenarios** (Datenfluss, wer „stellt bereit“, wer „greift zu“).
- Prüfe, ob deine Lösung **in sich stimmig** ist: Jedes Interface braucht genau einen Anbieter und mindestens einen Nutzer.

---

## 5. Typische Fehler

| Fehler | Warum falsch |
|---|---|
| Kreis und Halbkreis vertauschen | Dann stimmen Anbieter und Nutzer nicht mehr |
| Komponenten direkt per Pfeil verbinden, ohne Interface | Im Komponentendiagramm läuft die Kommunikation über Schnittstellen |
| Lautsprecher und Subwoofer neben das Soundsystem statt hinein | Sie sind Teil des Soundsystems |
| Externe Elemente (Musik-App, dB Sensor) ohne Kennzeichnung | Die Systemgrenze ist wichtig |
| Interface ohne Namen | Jede Schnittstelle muss beschriftet sein |

---

## 6. Kontrollfragen zum Selbsttest

1. Was ist der Unterschied zwischen einem bereitgestellten und einem benötigten Interface?
2. Wie sieht ein Assembly-Konnektor aus und was sagt er aus?
3. Warum liegen Lautsprecher und Subwoofer *innerhalb* des Soundsystems?
4. Warum braucht der Mixer das Interface *SoundChange*, bietet aber *Input* an?
5. Wie erkennst du im Text, welche Komponente ein Interface anbietet und welche es nutzt?
6. Wozu dient die Kennzeichnung „extern“?
7. Wie unterscheidet sich das Komponentendiagramm vom Klassendiagramm?

<details>
<summary>Kurze Antworten</summary>

1. Bereitgestellt = Kreis, die Komponente bietet die Schnittstelle an. Benötigt = Halbkreis, die Komponente braucht sie.
2. Ein Halbkreis, der einen Kreis umschließt. Er zeigt, dass eine Komponente das Interface einer anderen nutzt.
3. Sie sind Teile des Soundsystems (Verschachtelung).
4. Der Mixer nimmt Eingaben entgegen (bietet *Input* an) und gibt sie ans Soundsystem weiter (braucht *SoundChange*).
5. Am Datenfluss und an Formulierungen wie „stellt bereit“ (Anbieter) und „greift zu“ (Nutzer).
6. Sie grenzt Elemente außerhalb des betrachteten Systems ab.
7. Es zeigt Bausteine und Schnittstellen statt Klassen und deren Innenleben.

</details>

---

## 7. Merksatz

> **Kreis = ich biete an. Halbkreis = ich brauche.**
> Wo beide ineinanderpassen, arbeiten zwei Komponenten zusammen.
