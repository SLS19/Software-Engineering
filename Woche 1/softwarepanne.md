Aufgabe
Bei der Softwareentwicklung kommt es immer wieder zu Problemen und Pannen, die unterschiedlich große Auswirkungen haben. Der Standish Report stellt hierzu regelmäßig die Ergebnisse von Untersuchungen vor. In der Vorlesung wurden verschiedene Beispiele erläutert, bei denen ein Softwarefehler oder eine Panne im Entwicklungsprozess zu Problemen geführt hat.

Recherchiere ein weiteres Beispiel und stelle es kurz dar. Du kannst Dich dabei an folgenden Fragen orientieren:

Wo sollte die Software eingesetzt werden und was sollte sie machen?
Was ist passiert?
Wo lag der Fehler bzw. dessen Ursache?
Was sind die Folgen?
Wie hätte das Problem vermieden werden können?
Du kannst auch eigene Fragen zur Darstellung auswählen.

Hinweis: Es muss erkennbar sein, dass Du einen gewissen Aufwand in die Recherche und Darstellung investiert hast. Wenn Du Dir nicht sicher bist, ob Dein Beispiel gut ist, dann stell Dir folgende Fragen:

Hat das Problem Auswirkungen auf mehr als 50 Personen?
Wurde ein nicht-unerheblicher Schaden (finanziell, materiell, psychisch, …) verursacht?
Falls Du eine der beiden Fragen mit ‘Ja’ beantworten kannst, ist Dein Beispiel wahrscheinlich geeignet.


Softwarefehler bei Knight Capital (2012)

1. Einsatzbereich der Software

Knight Capital war ein US-amerikanisches Finanzunternehmen, das unter anderem automatisierten Wertpapierhandel betrieb. Dafür verwendete das Unternehmen ein Softwaresystem namens SMARS (Smart Market Access Routing System). Dieses System hatte die Aufgabe, Börsenaufträge zu verarbeiten und an Handelsplätze weiterzuleiten.

Im Juli 2012 wurde die Software erweitert, damit Knight Capital am neu eingeführten Retail Liquidity Program der New York Stock Exchange teilnehmen konnte. Bei der Installation dieser Erweiterung kam es jedoch zu einem schwerwiegenden Fehler.

2. Was ist passiert?

Am 1. August 2012 führte der Fehler dazu, dass das Handelssystem innerhalb von ungefähr 45 Minuten Millionen unerwünschter Börsenaufträge erzeugte und ausführte. Insgesamt kam es zu mehr als vier Millionen Handelsabschlüssen in 154 verschiedenen Aktien. Dabei wurden rund 397 Millionen Aktien gehandelt.

Das Unternehmen baute dadurch unbeabsichtigt sehr große Positionen auf, die es anschließend mit erheblichen Verlusten wieder auflösen musste. Nach Angaben der US-Börsenaufsicht verlor Knight Capital durch den Vorfall ungefähr 460 Millionen US-Dollar. Die fehlerhaften Handelsaktivitäten beeinflussten außerdem zeitweise die Kurse einzelner Aktien und wirkten sich damit auch auf andere Marktteilnehmer aus. (SEC, 2013)

3. Ursache des Fehlers

Die unmittelbare Ursache lag in einer fehlerhaften Installation der neuen Software. Knight Capital verwendete acht Server für das Handelssystem. Bei der Aktualisierung wurde der neue Programmcode auf sieben Servern installiert, während auf dem achten Server die alte Software erhalten blieb.

Diese ältere Software enthielt eine Funktion namens „Power Peg“, die zuvor für einen anderen Zweck eingesetzt worden war. Durch die neue Programmversion wurde diese veraltete Funktion auf dem nicht aktualisierten Server unbeabsichtigt aktiviert. Daraufhin begann das System, für eingehende Kundenaufträge immer wieder neue Handelsaufträge zu erzeugen, anstatt die bereits ausgeführten Aufträge korrekt zu berücksichtigen.

Ein weiteres Problem war der Umgang mit Warnmeldungen. Bereits vor der offiziellen Börseneröffnung hatte das Unternehmen automatisierte Fehlermeldungen erhalten, die auf die fehlerhafte Funktion hinwiesen. Diese Meldungen wurden jedoch nicht als dringende Systemwarnungen behandelt. Außerdem fehlten ausreichende Kontrollen, um sicherzustellen, dass alle Server dieselbe Softwareversion verwendeten. Die Installation erfolgte ohne eine verbindliche zweite Überprüfung. (SEC, 2013)

4. Folgen des Fehlers

Die finanziellen Folgen waren erheblich. Knight Capital erlitt einen Verlust von ungefähr 460 Millionen US-Dollar, wodurch die finanzielle Situation und der Geschäftsbetrieb des Unternehmens stark belastet wurden. Zusätzlich verlor das Unternehmen Vertrauen bei Kunden und Geschäftspartnern.

Auch andere Marktteilnehmer waren betroffen, da die große Zahl fehlerhafter Aufträge die Kurse einzelner Aktien beeinflusste. Im Oktober 2013 verhängte die US-Börsenaufsicht SEC außerdem eine Geldstrafe von zwölf Millionen US-Dollar gegen Knight Capital. Das Unternehmen hatte nach Feststellung der SEC keine ausreichenden Kontrollen und Überwachungsverfahren eingerichtet, um die Risiken seines automatisierten Handels angemessen zu begrenzen. (SEC, 2013)

5. Wie hätte das Problem vermieden werden können?

Der Vorfall hätte durch mehrere Maßnahmen wahrscheinlich verhindert oder zumindest deutlich begrenzt werden können. Zunächst hätte die Softwareinstallation automatisiert und überprüft werden müssen. Vor der Freigabe des Systems hätte sichergestellt werden sollen, dass auf allen acht Servern dieselbe, geprüfte Programmversion installiert ist.

Darüber hinaus hätte die alte Power-Peg-Funktion vollständig entfernt oder zuverlässig deaktiviert werden müssen, wenn sie nicht mehr benötigt wurde. Dadurch wäre das Risiko einer unbeabsichtigten Aktivierung reduziert worden.

Zusätzlich wären umfassendere Tests unter realistischen Handelsbedingungen sinnvoll gewesen. Diese hätten insbesondere überprüfen müssen, wie das System auf unerwartete Zustände und fehlerhafte Auftragsverarbeitungen reagiert. Ein weiterer wichtiger Schutzmechanismus wäre eine automatische Abschaltung gewesen, die bei ungewöhnlich vielen Aufträgen oder einer Überschreitung festgelegter Risikogrenzen eingreift.

Schließlich hätten die vorhandenen Fehlermeldungen als kritische Warnungen behandelt und klare Zuständigkeiten für die Reaktion auf solche Meldungen festgelegt werden müssen. Der Vorfall zeigt damit, dass nicht nur die Programmierung selbst, sondern auch die Installation, Überwachung und organisatorische Kontrolle einer Software entscheidend für deren Zuverlässigkeit sind.

6. Fazit

Der Vorfall bei Knight Capital zeigt, wie schwerwiegend die Folgen eines Fehlers im Softwareentwicklungs- und Einführungsprozess sein können. Obwohl die Änderung ursprünglich nur eine Erweiterung des bestehenden Handelssystems darstellen sollte, führten eine unvollständige Installation und unzureichende Sicherheitskontrollen zu einem finanziellen Verlust von mehreren hundert Millionen US-Dollar.

Besonders deutlich wird, dass eine Software nicht allein deshalb zuverlässig ist, weil sie zuvor funktioniert hat. Auch Änderungen und Aktualisierungen müssen sorgfältig geprüft und kontrolliert werden. Einheitliche Softwareversionen, automatisierte Installationstests, wirksame Überwachung und eine zuverlässige Notabschaltung hätten dazu beitragen können, den Vorfall zu verhindern oder seine Auswirkungen zu begrenzen.

Quellenverzeichnis

U.S. Securities and Exchange Commission (SEC) (2013): *In the Matter of Knight Capital Americas LLC, Administrative Proceeding No. 3-15570, Release No. 34-70694*, 16. Oktober 2013. Verfügbar unter: https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf

Knight Capital Group (2013): *Form 10-K for the fiscal year ended December 31, 2012*. Verfügbar unter: https://www.sec.gov/Archives/edgar/data/1060749/000119312513215378/R12.htm