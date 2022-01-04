# presidenten
Prosjekt som handler om å få simulert kortspillet "Presidenten"

# Idébank
*HP - Høy prioritet, MP - Middels prioritet, LP - Lav prioritet*
- [HP] Legge inn muligheten for å lagre/laste inn et spill
- [HP] Utvikle "innstillinger" menyen
- [MP] Legge inn flere språk
- [LP] Gi spillet et grafisk brukergrensesnitt (GUI)
- [MP] Mulighet for å opprette bruker (kanskje også med passord ellerno?)
       > dette kan da gi muligheten for å opprette scoreboard, statistikker osv
- [LP] Gjøre det mulig å spille ONLINE
- [LP] Gjøre det mulig å koble opp til en database og laste opp scoreboard, statistikk osv til en nettside for eksempel

# Bugs
- metode self.check_more_than_four_on_table() tar hensyn til HELE historikken, og ikke bare de siste kortene. Det kan derfor tillate at spillere kan slå ut bunken med to kort på en tom bunke, bare fordi de to kortene som ble lagt ut, er av samme verdi som de to siste i historikken. **(KANSKJE FIKSET?)**

# Ting å sjekke opp
- burde spille et helt spill ferdig, så se hva som skjer: om spillerne får tilskrevet riktige plasser (pres., boms, vicepres., viceboms, nøytral) og om alt blir printet fint. Hva som skjer etterpå er det ikke enda skrevet kode til. (dvs. hva hvis spilleren sier ja: la spillere gjøre utveksling av kort osv...)
