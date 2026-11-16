# Architekturmuster in der freien Wildbahn: Microservices bei Netflix

## 1. Lösung zur Aufgabe

### Das Muster in Kürze

Bei einer **Microservices-Architektur** wird eine Anwendung nicht als ein großer Block (Monolith) gebaut, sondern als Sammlung vieler kleiner, eigenständiger Dienste. Jeder Dienst:

- ist für **genau einen fachlichen Bereich** zuständig,
- hat **seine eigene Datenhaltung**,
- wird **unabhängig gebaut, getestet, deployed und skaliert**,
- spricht mit anderen Diensten nur über **klar definierte Schnittstellen** (z. B. REST, gRPC, Messaging).

### Das Beispiel: Netflix

Netflix hat seine Plattform von einem Monolithen auf Microservices umgestellt. Auslöser war 2008 ein schwerer Datenbankausfall, der den DVD-Versand tagelang lahmlegte. Danach wurde schrittweise auf eine verteilte Architektur in der Cloud (AWS) migriert. Typische Dienste sind zum Beispiel:

| Dienst | Aufgabe |
|---|---|
| Benutzerverwaltung | Accounts, Profile, Abos |
| Empfehlungssystem | Vorschläge anhand des Sehverhaltens |
| Suche | Suchen und Filtern im Katalog |
| Streaming / Playback | Auslieferung der Videos |
| Abrechnung | Zahlungen und Rechnungen |

Wichtig: Eine Anfrage der App (z. B. "Startseite laden") wird typischerweise über ein **API-Gateway** an viele dieser Dienste verteilt, deren Antworten dann zusammengesetzt werden.

### Wesentliche Vorteile

1. **Unabhängige Skalierbarkeit:** Nur der Dienst, der gerade unter Last steht (z. B. Playback am Freitagabend), bekommt mehr Ressourcen, nicht das ganze System.
2. **Unabhängige Entwicklung und Deployment:** Teams arbeiten an eigenen Diensten und können mehrmals täglich releasen, ohne sich mit allen anderen abzustimmen.
3. **Wartbarkeit und Erweiterbarkeit:** Kleine Codebasen sind leichter zu verstehen, zu ändern oder komplett auszutauschen.
4. **Ausfallsicherheit (Fehlerisolation):** Fällt z. B. das Empfehlungssystem aus, kann man trotzdem noch Filme suchen und schauen. Netflix hat dafür Muster wie *Circuit Breaker* (Hystrix) und Fallbacks eingesetzt.
5. **Technologiefreiheit:** Jeder Dienst kann die Technologie nutzen, die am besten passt.

### Nachteile (gehört für eine runde Antwort dazu)

- **Hohe Komplexität im Betrieb:** Viele Dienste müssen überwacht, deployed und gefunden werden (Service Discovery, Monitoring, Tracing).
- **Verteilte Systeme sind schwer:** Netzwerklatenz, Teilausfälle, Datenkonsistenz über Dienste hinweg.
- **Organisatorischer Aufwand:** Schnittstellen müssen stabil und versioniert sein.

### Fazit

Microservices lohnen sich vor allem bei **großen, komplexen Systemen mit vielen Teams und stark schwankender Last**, wie bei Netflix. Für kleine Anwendungen ist der Overhead oft größer als der Nutzen.

---

## 2. Was du beim Selbermachen hättest lernen sollen

### Lernziel der Aufgabe

Nicht "ein Muster auswendig kennen", sondern **erkennen, wann ein Muster sinnvoll ist**. Dafür musst du den Zusammenhang sehen: *Problem → Muster → Vorteil → Preis, den man dafür zahlt.*

### Kernkonzepte

- **Architekturmuster vs. Entwurfsmuster:** Architekturmuster (Schichten, Microservices, Client-Server, Event-Driven, Pipes & Filter) bestimmen die Grobstruktur des ganzen Systems. Entwurfsmuster (Observer, Factory) wirken im Kleinen innerhalb des Codes.
- **Monolith vs. Microservices:** Der Monolith ist einfach zu starten und zu testen, aber schwer zu skalieren und zu ändern, wenn er wächst.
- **Qualitätsattribute:** Architektur wird durch Qualitätsziele getrieben (Skalierbarkeit, Wartbarkeit, Verfügbarkeit, Änderbarkeit). Jede Vorteilsaussage sollte sich auf eines davon beziehen.
- **Trade-offs:** Jedes Muster tauscht etwas gegen etwas anderes. Microservices tauschen *Einfachheit* gegen *Flexibilität und Skalierbarkeit*.
- **Lose Kopplung, hohe Kohäsion:** Dienste sollen intern fachlich zusammenhängen und nach außen möglichst wenig voneinander wissen.
- **Conway's Law:** Die Architektur spiegelt die Teamstruktur wider. Microservices passen zu kleinen, autonomen Teams.

### Wie man bei so einer Aufgabe vorgeht

1. Ein Beispielsystem wählen, über das es **belastbare Quellen** gibt (Engineering-Blogs, Konferenzvorträge).
2. Das **Problem** benennen, das das Muster löst (bei Netflix: Ausfälle, Wachstum, viele Teams).
3. Das Muster **kurz und in eigenen Worten** erklären.
4. Vorteile **konkret am Beispiel** zeigen, nicht nur allgemein.
5. Mindestens einen **Nachteil** nennen, das zeigt Verständnis.

### Selbsttest

1. Warum ist ein Monolith für ein Start-up mit drei Entwicklern oft die bessere Wahl?
2. Was passiert bei Microservices, wenn ein Dienst langsam wird, von dem viele andere abhängen? Welches Muster hilft dagegen?
3. Warum braucht man ein API-Gateway?
4. Welche Qualitätsattribute verbessern sich, welche verschlechtern sich durch Microservices?
5. Nenne ein anderes Architekturmuster (z. B. Schichtenarchitektur) und ein System, bei dem es besser passt als Microservices.

### Mögliche Antworten (Kurzform)

1. Weniger Overhead, einfacheres Deployment und Debugging, keine verteilte Komplexität.
2. Fehler pflanzen sich fort (Kaskadenfehler). Abhilfe: Circuit Breaker, Timeouts, Fallbacks, Bulkheads.
3. Er bündelt Anfragen, versteckt die interne Aufteilung vor den Clients und übernimmt Querschnittsthemen wie Authentifizierung.
4. Besser: Skalierbarkeit, Änderbarkeit, Fehlerisolation. Schlechter: Einfachheit, Performance durch Netzwerkaufrufe, Konsistenz, Betriebsaufwand.
5. Z. B. Schichtenarchitektur für ein klassisches internes Verwaltungssystem mit überschaubarer Last.

---

## 3. Hinweise zur Abgabe

- **Eigene Worte verwenden:** Wenn der Text von einem KI-Tool stammt, lies ihn kritisch durch und formuliere ihn selbst, damit du ihn auch erklären kannst.
- **Quellen prüfen:** Die zwei Links aus deinem Entwurf enthalten den Zusatz `?utm_source=chatgpt.com`. Entferne ihn. Außerdem behandelt der GraphQL-Federation-Artikel eher die API-Schicht und belegt die Microservices-Vorteile nur indirekt. Besser passen Netflix-TechBlog-Beiträge oder Vorträge zur Migration in die Cloud sowie zu Hystrix und Eureka, die du selbst nachlesen und prüfen solltest.
- **Formulierung "könnten":** Im Entwurf steht "Bei Netflix könnten solche Dienste...". Besser ist eine belegte Aussage oder die klare Kennzeichnung als vereinfachtes Beispiel.
