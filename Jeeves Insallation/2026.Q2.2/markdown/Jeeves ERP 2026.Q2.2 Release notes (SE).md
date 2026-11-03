
![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-SE-.pdf-0001-00.png)


# **RELEASE AV JEEVES ERP 2026.Q2.2** 

Stockholm, september 2026 

Detta är en mindre kvartalsrelease ("minor release"), främst avsedd för tidig tillgång till ny funktionalitet och rättningar av fel med lägre allvarlighetsgrad innan dessa inkluderas i en årlig huvudrelease. Jeeves ERP 2026.Q2.2 kommer endast att underhållas tills nästa ”minor” kvartalsrelease, Jeeves ERP 2026.Q2.3, blir tillgänglig. 

## **Vad denna release innebär för dig** 

- **Classic-klienten levereras inte längre** – Desktop-klienten är nu den enda klienten som stöds för nya installationer och uppgraderingar. Befintliga installationer av Classic-klienten omfattas fortsatt av den supportpolicy som gäller för respektive release. 

- **Stöd för din övergång till molnet** – Integrering av Jeeves ERP med externa tjänster samt standardiserat digitalt informationsutbyte för affärsdokument såsom order, leveransplaner, ordersvar och fakturor. 

- **E-fakturering och regelefterlevnad** – Förbättrad integration för inkommande e-fakturering med Pagero, med utökat stöd för automatisering och efterlevnad av polska KSeF-krav. 

## **Nyheter i Jeeves ERP 2026.Q2.2** 

### _Stöd för din övergång till molnet_ 

Outbound API Service – ett nytillskott i Jeeves API Platform för säker integration med externa webbtjänster 

En ny utgående API-tjänst kompletterar Jeeves API Platform och hjälper dig att koppla samman Jeeves ERP med externa system och molnbaserade tjänster via säkra och standardiserade integrationer. 

Tjänsten installeras lokalt i din miljö och ger Jeeves ERP ett tillförlitligt och kontrollerat sätt att kommunicera med tredjepartstjänster för specifika integrationer. 

#### Viktiga funktioner: 

- **Enklare anslutning till externa tjänster** – Med Jeeves Outbound API Service kan externa webbtjänster anropas direkt från affärsprocesser via makron eller SQL-kod. Tjänsten stöder både synkrona och asynkrona anrop, vilket gör det möjligt att välja mellan omedelbart svar eller bearbetning i bakgrunden. Ett obegränsat antal externa tjänster kan anslutas till varje Jeevesmiljö för olika användningsområden. 

- **Säker hantering av åtkomstuppgifter** – Inloggningsuppgifter och åtkomstnycklar för anslutna tjänster lagras säkert och loggas aldrig. Det är möjligt att använda olika autentiseringsuppgifter för varje miljö. Tjänsten stöder autentiseringsmetoder som klientautentisering (Client Credentials), JWT-baserad autentisering och API-nycklar. 

_(För mer information, se kapitlet_ _<u>Ny funktionalitet i plattformen - 2026.1-3 i Jeeves ERP</u> onlinedokumentation)_ 

Jeeves Digital Business Documents Package 

Med Jeeves Digital Business Documents Package introducerar vi ett modernt, API-baserat ramverk för EDI och digitalt utbyte av affärsdokument som underlättar övergången från traditionell EDI-infrastruktur till mer molnbaserade integrationsmodeller. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-SE-.pdf-0002-00.png)


Lösningen moderniserar traditionell EDI-kommunikation genom att den ersätter integrationer baserade på EDI-servrar med standardiserade API:er för utbyte av affärsdokument mellan Jeeves ERP och externa handelspartner. Stödda scenarier omfattar inkommande order, orderändringar och leveransplaner samt utgående ordersvar och fakturameddelanden. 

För europeiska industriföretag i mellansegmentet möjliggör detta snabbare och mer tillförlitliga digitala affärstransaktioner, förbättrad integration med handelspartner samt en skalbar grund för att successivt utöka stödet för digitala affärsdokument 

Viktiga funktioner: 

- **Integration med kärnramverket** – Infrastruktur för hantering av partnerprofiler, routning av digitala affärsdokument samt stöd för standardiserade API:er för affärsdokument. 

- **API:er för digital orderhantering** – Ta emot och bearbeta inkommande affärsdokument automatiskt, inklusive order [ORDERS], orderändringar [ORDCHG] och leveransplaner [DELFOR/DELINS].. 

- **Automatiserad leverans av svarsdokument** – Generera och leverera digitala ordersvar till kunder, vilket utökar möjligheterna för utgående elektronisk kommunikation. 

- **API för utgående fakturadata** – Exponera fakturadata [INVOIC] via ett API för överföring till APPER (eller annan EDI-tjänsteleverantör). API:et omfattar de uppgifter som normalt krävs för ett EDIFACT INVOIC-meddelande, men är inte avsett att täcka samtliga element i den fullständiga EDIFACT INVOIC-specifikationen. 

- **Förenklad felhantering och administration** – Återställ och bearbeta om misslyckade dokumenttransaktioner direkt från program för meddelandehantering, med förbättrade möjligheter till konfiguration och styrning av automatiserade integrationsprocesser. 

- **Utökat stöd för digitalt utbyte av affärsdokument** – Standardiserat API-stöd för ett växande antal affärstransaktioner gör det möjligt för företag att gå från traditionellt EDI-baserat dokumentutbyte till moderna API-baserade integrationer. 

- **Förbättrad struktur i Jeeves ERP-dokumentationen** – Dokumentationen för digitala affärsdokument är nu samlad under ett särskilt avsnitt, Digitala affärsdokument, med separata områden för e-fakturering och EDI. Detta förbättrar navigeringen och gör det enklare att hitta vägledning för implementering. 

_(För mer information, se kapitlen_ _<u>Ny funktionalitet i EDI-modulerna, Leverantörsreskontran, och Försäljningsmodulen, samt kapitlen e-Fakturering and EDI</u> under Digitala affärsdokument)_ 

#### Förbättrad hantering av leveransadresser 

Hanteringen av leveransadresser har förbättrats för kundorder som skapas från inkommande EDI-order. Jeeves ERP prioriterar nu den leveransadress som anges i EDI-ordern, därefter adressen som är definierad för leveransstället och slutligen standardadressen för leveransstället. 

Detta säkerställer att den mest specifika tillgängliga leveransadressen används och förbättrar träffsäkerheten i orderhanteringen 

### _e-fakturering och regelefterlevnad_ 

Förbättrad integration för inkommande e-fakturering med Pagero 

Integrationen för inkommande e-fakturering med Pagero har förbättrats, med förbättringar inom integrationsstabilitet, felhantering och hämtning av fakturor. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-SE-.pdf-0003-00.png)


Viktiga förbättringar: 

- **Ombyggda integrationskomponenter för inkommande fakturor** – Delar av integrationen för inkommande e-fakturor via Pagero har byggts om, vilket förbättrar affärslogiken, felhanteringen och användaraviseringarna. 

- **Förbättrad hantering av återförsök** – Effektivare hantering av inkommande fakturor som tidigare har misslyckats i behandlingen. 

- **Möjlighet att hämta fakturor på nytt** – Stöd för att hämta in fakturor på nytt direkt från Jeeves. 

_(För mer information, se online-kapitlen_ _<u>Ny funktionalitet i leverantörsreskontran, Ny funktionalitet i EDImodulerna samt kapitlet e-fakturering under Digitala affärsdokument</u>_ 

Polen: KSeF-efterlevnad och förbättringar av e-fakturering 

Stödet för det polska KSeF-systemet har utökats avsevärt, inklusive förberedelser för det strukturerade fakturaformatet FA(3) samt kommande regelkrav för bankbetalningar. 

Funktionaliteten är tillgänglig för tidig åtkomst och hjälper företag att öka automatiseringen, förbättra betalningsavstämningen samt säkerställa regelefterlevnad i fakturerings- och betalningsprocesser. 

#### Viktiga funktioner: 

- **KSeF-anpassad hantering av bankbetalningar** – Stöd för utgående leverantörsbetalningar i ISO 20022 XML-format (pain.001), inkommande kundbetalningsaviseringar i camt.054-format, KSeF-identifierare i betalningsreferenser samt den polska split payment-mekanismen (MPP). 

- **Stöd för e-fakturor enligt FA(3)** – Utökat stöd för det senaste KSeF-fakturaformatet, inklusive information om tredje part (Podmiot3) samt kundspecifika artikelnummer, beskrivningar och specifikationer. 

- **Förbättrad hantering av förskotts- och slutregleringsfakturor** – Slutregleringsfakturor kan innehålla information om kopplade förskottsfakturor, inklusive fakturanummer, datum och belopp, vilket förbättrar avstämningsmöjligheterna. 

- **Ökad automatisering och effektivare hantering** – Effektiviserade processer genom automatisk hämtning av KSeF-PDF:er, förbättrad språkhantering och minskat behov av manuella åtgärder. 

- **Förbättrad validering och regelefterlevnad** – Förbättringar av validerings- och bearbetningslogiken för fakturor bidrar till att minska antalet KSeF-avvisningar och öka den övergripande tillförlitligheten. 

- **Tydligare struktur i Jeeves ERP-dokumentationen** – Tidigare utspritt innehåll för Polen har samlats i ett särskilt avsnitt, Polen, under Landsspecifika implementationer. Detta gör informationen enklare att hitta och minskar behovet av att navigera mellan flera olika kapitel. 

_(För mer information, se online-kapitlet_ _<u>Elektroniska kundfakturor, KSeF utgående flöde.)</u>_ 

## **Rättningar och förbättringar** 

Förutom ny funktionalitet och vidareutveckling innehåller varje ny release av Jeeves ERP ett antal generella förbättringar och uppdateringar: 

- Prestandaförbättringar – generella förbättringar av hastighet och svarstid i applikationen. 

- Stabilitetsförbättringar – olika buggar har rättats. För mer information se rättningsrapporterna. 

- • Viktiga säkerhetsuppdateringar – de senaste säkerhetspatcharna har implementerats för att skydda mot sårbarheter. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-SE-.pdf-0004-00.png)


En komplett sammanställning av alla rättningar och förbättringar finns i följande dokument: 

- Jeeves ERP Corrections and enhancements in Platform 2026.2.html 

- Jeeves ERP Corrections and enhancements in JAS 2026.2.html 

Rättningar och förbättringar i Jeeves mobilappar finns i versionsinformationen i App Store och i avsnittet ”What's new” på Google Play: 

- <u>Jeeves ERP – App Store</u> 

- <u>Jeeves ERP – Google Play</u> 

## **Dokumentation** 

|Dokument|Status|
|---|---|
|Jeeves ERP Corrections and enhancements in Platform 2026.2|Uppdaterat|
|Jeeves ERP Corrections and enhancements in JAS 2026.2|Uppdaterat|
|Jeeves ERP Installation and configuration|Uppdaterat|
|Jeeves ERP Upgrade considerations|Uppdaterat|
|Jeeves ERP PEPPOL installation and configuration|Uppdaterat|
|Jeeves ERP e-Approval configurationguide|Uppdaterat|
|Jeeves Cloud Print service installation and configuration|Oförändrat|
|Jeeves ERP New Local Business server installation and configuration|Oförändrat|
|Jeeves ERP Design studio installation and configuration|Oförändrat|
|Jeeves ERP Hybrid cloud local installation and configuration|Oförändrat|
|Jeeves ERP Client settings transitionguide|Oförändrat|
|Jeeves ERP Site repositorysettingsguide|Oförändrat|
|Jeeves Launchpad services configuration|Oförändrat|
|Jeeves Launchpad userguide|Oförändrat|



Observera att dokumentationen för Jeeves WMS levereras som en del av WMS-releasepaketet och finns tillgänglig i <u>Jeeves Download Center.</u> 

## **Systemkrav** 

Se guiden Jeeves ERP Upgrade considerations. 

## **Språk** 

Produkten levereras på engelska, svenska, norska, finska, danska, polska, franska, tyska, nederländska och förenklad kinesiska. 

## **Att tänka på vid uppgradering** 

Vid uppgradering till Jeeves ERP 2026.Q2.2 finns några särskilda förutsättningar att ta hänsyn till, däribland krav på .NET Framework 4.8.1 och att manuell COM-registrering inte längre krävs. 

Mer information finns i avsnittet om uppgradering till Jeeves ERP 2026.Q2.2 i guiden Jeeves ERP Upgrade considerations. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-SE-.pdf-0005-00.png)


## **Underhåll** 

Fel i Jeeves ERP 2026.Q2.2 måste verifieras i Jeeves verifieringsmiljö för att klassificeras som ett fel i Jeeves Incident Management. Detta gäller inte kunder med supportavtal. 

Buggar och supportärenden ska rapporteras i Jeeves Incident Management, med relevant applikation, till exempel Huvudbok (General ledger) eller Lager (Inventory) som ”Category”, samt fullständigt versionsnummer för plattformen som ”Product Other”. 

Rättningar av kritiska fel eller fel med hög allvarlighetsgrad (severity level 1 eller 2) publiceras som patchar via <u>Jeeves Download Center.</u> 

Rättningar av fel med severity level 1 släpps så snart som möjligt. Eventuella rättningar av fel med severity level 2 för plattformen, samt alla applikationsrättningar (JAS), släpps veckovis. Rättningar av fel med medelhög eller låg allvarlighetsgrad (severity level 3 och 4) ingår i nästkommande kvartalsrelease av Jeeves ERP eller i nästa årliga release, tillgänglig via <u>Jeeves Download Center.</u> 

## **Nedladdning** 

Jeeves ERP 2026.Q2.2 finns tillgänglig för nedladdning från <u>Jeeves Download Center.</u> 

De standard-API:er som utvecklas av Jeeves levereras som paket i <u>Jeeves Download Center.</u> 

Läs mer om våra releaser på sidan <u>Jeeves Produktreleaser i vår Supportportal.</u> 

## **Cloud-tjänster** 

Beställning av Jeeves Cloud-tjänster, exempelvis Federerad autentisering, eAttest Cloud eller Jeeves API Platform görs på <u>Jeeves Cloud ERP Services Portal. Vid frågor, vänligen kontakta din kundansvarige hos</u> Forterro Sweden. 

- För mer information, se sidan <u>Information om Cloud-tjänster.</u> 

## **Frågor** 

Har du frågor angående Jeeves ERP 2026.Q2.2, vänligen kontakta Jeeves Product Management. 

