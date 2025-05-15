# Prosjektplan – Braathen Retail

## Prosjektnavn
Braathen Retail – Enkel nettbutikk for skolelever

## Prosjektbeskrivelse
Braathen Retail skal være en brukervennlig nettbutikk hvor elever kan registrere seg, logge inn, se produkter, legge varer i handlekurven og se en oversikt over sine varer. Løsningen skal være enkel, responsiv og sikker nok for et skoleprosjekt.

## Mål
- Lage en enkel og oversiktlig nettbutikk med moderne design.
- Brukere skal kunne registrere seg, logge inn og ut.
- Produkter skal kunne vises med navn, beskrivelse og pris.
- Brukere skal kunne legge varer i en handlekurv og se totalpris.
- All funksjonalitet skal være tilgjengelig på både mobil og desktop.

## Teknologivalg
- **Backend:** Python med Flask
- **Frontend:** HTML, CSS, JavaScript (kun for små interaksjoner)
- **Database:** SQLite (for enkel brukerhåndtering)
- **Sessions:** Flask sessions for innlogging og handlekurv

## Funksjonelle krav
1. **Registrering og innlogging**
   - Brukere kan registrere seg med navn, e-post og passord.
   - Brukere kan logge inn og ut.
   - Passord lagres som hash i databasen.

2. **Produktvisning**
   - Produkter vises med navn, beskrivelse og pris.
   - Produktene er hardkodet for enkelhet.

3. **Handlekurv**
   - Brukere kan legge produkter i handlekurven.
   - Handlekurven viser antall, pris per produkt og totalpris.
   - Handlekurven lagres i session.

4. **Brukergrensesnitt**
   - Moderne og responsivt design.
   - Tydelige knapper for hovedhandlinger.
   - Flash-meldinger for tilbakemelding på handlinger.

5. **Navigasjon**
   - Enkel navigasjon mellom forside, butikk, handlekurv, innlogging og registrering.

## Ikke-funksjonelle krav
- **Responsivt design:** Skal fungere på mobil og desktop.
- **Enkel kodebase:** Lett å forstå og utvide.
- **Sikkerhet:** Passord lagres som hash, ingen sensitive data eksponeres.
- **Ytelse:** Rask lasting, minimal bruk av eksterne ressurser.

## Milepæler og leveranser
1. **Oppsett av prosjektstruktur**  
   - Opprette mapper for templates, static, og database.
2. **Brukerhåndtering**  
   - Registrering, innlogging, utlogging, sessions.
3. **Produkt- og handlekurvlogikk**  
   - Vise produkter, legge til i handlekurv, vise handlekurv.
4. **Frontend og design**  
   - Lage og style HTML-sider, gjøre design responsivt.
5. **Testing og kvalitetssikring**  
   - Teste alle brukerflyter og rette feil.
6. **Dokumentasjon**  
   - Skrive brukerdokumentasjon og FAQ.

## Sider og brukerflyt
- **index.html:** Forside med velkomst, handle-knapp og innlogging.
- **register.html:** Registreringsskjema.
- **login.html:** Innloggingsskjema.
- **shop.html:** Produktoversikt og kjøpsmulighet.
- **cart.html:** Handlekurv med oversikt og totalpris.

## Fremtidige utvidelser (ikke med i denne versjonen)
- Betalingsløsning
- Ordrehistorikk
- Produktadministrasjon for admin

---

**Planen er laget for å sikre at prosjektet utvikles strukturert og målrettet, med fokus på brukervennlighet og enkelhet.**