
![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-EN-.pdf-0001-00.png)


# **RELEASE OF JEEVES ERP 2026.Q2.2** 

Stockholm, September 2026 

This is a quarterly minor release, primarily intended to provide early access to new features and fixes for lower-severity bugs, before they are included in an annual major release. Jeeves ERP 2026.Q2.2 will only be maintained until the next quarterly minor release, Jeeves ERP 2026.Q2.3, is available. 

## **What this release means for you** 

- **Desktop Client only** – The Desktop Client is now the standard and only supported client for new installations and upgrades. The Classic Client is no longer delivered. Existing Classic Client deployments continue to follow the applicable support policy for their release. 

- **Supporting your cloud journey** – Connect Jeeves ERP to external services and enable standardized digital business document exchange, including orders, order changes, delivery schedules, order responses, and invoice data. 

- **eInvoicing and regulatory compliance** – Improved inbound eInvoicing integration with Pagero, with expanded support for Polish KSeF compliance and automation. 

## **Highlights in Jeeves ERP 2026.Q2.2** 

### _Supporting your cloud journey_ 

Introducing Outbound API Service – a new addition to the Jeeves API Platform for secure integration with external web services 

A new outbound API service extends the Jeeves API Platform, helping you connect Jeeves ERP to external systems and cloud-based services through secure, standardized integrations. 

The service is installed locally in your environment and provides a reliable, controlled way for Jeeves ERP to call third-party services for targeted, limited integrations. 

Key features include: 

- **Easier connection to external services** – Using Jeeves Outbound API service, external web services can be called directly from business processes via macros or SQL code. It supports synchronous and asynchronous calls, letting you choose immediate response or background processing. The service supports multiple external services per Jeeves environment for various use cases. 

- **Secure handling of access details** – Login details and access keys for connected services are stored securely and never logged. You can use different credentials for each environment. The service supports authentication methods including client credentials, JWT-based authentication, and API keys. 

_(For more details, see_ <u>New functionality in Platform – 2026.1-3</u> _in the online Jeeves ERP online documentation)_ 

#### Jeeves Digital Business Documents Package 

The Jeeves Digital Business Documents Package introduces a modern, API-based framework for EDI and digital business document exchange, supporting the transition from traditional EDI infrastructures to more cloud-oriented integration models. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-EN-.pdf-0002-00.png)


The solution modernizes traditional EDI communication by replacing EDI server-based integrations with standardized APIs for exchanging business documents between Jeeves ERP and external trading partners. Supported scenarios include inbound orders, order changes, and delivery schedules, as well as outbound order responses and invoice messages. 

For European industrial mid-market businesses, this enables faster and more reliable digital transactions, improved integration with trading partners, and a scalable foundation for expanding digital business document capabilities. 

Key features include: 

- **Core framework integration** – Infrastructure for managing partner profiles, routing digital business documents, and supporting standardized business document APIs. 

- **Inbound digital business document APIs** – Receive and automatically process inbound business documents, including orders [ORDERS], order changes [ORDCHG], and delivery schedules [DELFOR/DELINS]. 

- **Outbound order response delivery** – Generate and deliver digital order response documents to customers [ORDRSP], expanding outbound electronic communication capabilities. 

- **Outbound invoice data API** – Expose invoice data [INVOIC] through an API for transfer to APPER (or other EDI service provider). The API covers the data typically required for an EDIFACT INVOIC message but is not intended to cover every element in the complete EDIFACT INVOIC specification. 

- **Simplified error recovery and administration** – Reset and reprocess failed document transactions directly from message management programs, with enhanced configuration and control of automated integration processing. 

- **Expanded digital business document exchange** – Standardized API support for a growing set of business transactions, enabling organizations to transition from traditional EDI document exchanges to modern API-based integrations. 

- **Enhanced clarity in the Jeeves ERP documentation** – Digital business document documentation is now organized under a dedicated **Digital business documents** section, with separate **eInvoicing** and **EDI** areas, improving navigation and making implementation guidance easier to find. 

_(For more details, see the_ _<u>New functionality chapters for the EDI modules, Accounts payable ledger, and Sales module, as well as the eInvoicing and EDI</u> chapters under Digital business documents)_ 

#### Enhanced delivery address resolution 

Delivery address handling has been improved for customer orders created from incoming EDI orders. Jeeves ERP now prioritizes the delivery address specified on the EDI order, followed by the address defined for the Point of Delivery and, lastly, the standard Point of Delivery address. 

This ensures that the most specific available delivery address is used and improves the accuracy of order processing. 

### _eInvoicing and regulatory compliance_ 

#### Enhanced Pagero inbound eInvoicing integration 

Several improvements have been made to the Pagero inbound eInvoicing integration, including enhanced reliability, error handling, and invoice retrieval. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-EN-.pdf-0003-00.png)


Key improvements include: 

- **Rebuilt inbound integration components** – Partial rebuild of the inbound eInvoicing integration with Pagero, improving business logic, error handling, and user notifications. 

- **Improved retry handling** – Better management of failed incoming invoices. 

- **Ability to retrieve invoices again** – Option to re-fetch invoices directly from within Jeeves. 

_(For more details, see the online Jeeves ERP documentation, chapters New functionality in the accounts_ _<u>payable ledger</u>_ <u>,</u> _<u>New functionality in the EDI modules</u>_ <u>,</u> _and the_ _<u>eInvoicing</u> chapters under Digital business documents)_ 

Poland: KSeF compliance and eInvoicing enhancements 

Polish KSeF support has been significantly enhanced, including readiness for the FA(3) structured invoice format and upcoming KSeF-compliant bank payment processing requirements scheduled to become mandatory on January 1, 2027. 

The functionality is available for early adoption and helps organizations improve automation, payment reconciliation, and regulatory compliance across invoicing and payment processes. 

Key features include: 

- **KSeF-compliant bank payment processing** – Support for outgoing supplier payments in ISO 20022 XML (pain.001) format, incoming customer payment notifications in camt.054 format, KSeF identifiers in payment references, and the Polish split payment mechanism (MPP). 

- **FA(3) eInvoice support** – Expanded support for the latest KSeF invoice format, including thirdparty information (Podmiot3) and customer-specific item numbers, descriptions, and specifications. 

- **Advance and settlement invoice enhancements** – Settlement invoices can include information about linked advance invoices, including invoice numbers, dates, and amounts, improving reconciliation. 

- **Automation and usability improvements** – Streamlined processing through automated KSeF PDF retrieval, improved language handling, and reduced manual intervention. 

- **Validation and compliance improvements** – Enhancements to invoice validation and processing logic to help reduce KSeF rejections and improve overall reliability. 

- **Enhanced clarity in the Jeeves ERP documentation** – Previously dispersed Poland-specific content has been reorganized into a dedicated **Poland** section under **Country-specific implementations** , improving discoverability and reducing the need to navigate multiple chapters. 

_(For more details, see online chapter_ _<u>Customer eInvoices, KSeF outgoing flow)</u>_ 

## **Corrections and enhancements** 

Along with new features and feature enhancements, each Jeeves ERP release includes several general improvements and updates: 

- Performance improvements – enhanced the overall speed and responsiveness of the application. 

- Stability enhancements – various bugs have been corrected. For details, please see the lists of corrections. 

- Important security updates – includes the latest security patches to protect against vulnerabilities. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-EN-.pdf-0004-00.png)


A complete list of error corrections and enhancements can be found in the documents: 

- Jeeves ERP Corrections and enhancements in Platform 2026.2.html 

- Jeeves ERP Corrections and enhancements in JAS 2026.2.html 

Corrections and enhancements in Jeeves Mobile apps can be found in the version information in the App Store and the “What’s new” section on Google Play: 

- <u>Jeeves ERP – App Store</u> 

- <u>Jeeves ERP – Google Play</u> 

## **Documentation** 

|Document|Status|
|---|---|
|Jeeves ERP Corrections and enhancements in Platform 2026.2|Updated|
|Jeeves ERP Corrections and enhancements in JAS 2026.2|Updated|
|Jeeves ERP Installation and configuration|Updated|
|Jeeves ERP Upgrade considerations|Updated|
|Jeeves ERP PEPPOL installation and configuration|Updated|
|Jeeves ERP e-Approval configurationguide|Updated|
|Jeeves Cloud Print service installation and configuration|Unchanged|
|Jeeves ERP New Local Business server installation and configuration|Unchanged|
|Jeeves ERP Design studio installation and configuration|Unchanged|
|Jeeves ERP Hybrid cloud local installation and configuration|Unchanged|
|Jeeves ERP Client settings transitionguide|Unchanged|
|Jeeves ERP Site repositorysettingsguide|Unchanged|
|Jeeves Launchpad services configuration|Unchanged|
|Jeeves Launchpad userguide|Unchanged|



Note that the Jeeves WMS documentation is delivered as part of the WMS release package, available in the Jeeves ERP Product download center. 

## **System requirements** 

See the Jeeves ERP Upgrade considerations guide. 

## **Languages** 

Supported languages are English, Swedish, Norwegian, Finnish, Danish, Polish, French, German, Dutch, and Simplified Chinese. 

## **Upgrade considerations** 

There are a few special considerations that need to be taken when upgrading to Jeeves ERP 2026.Q2.2, including .NET Framework 4.8.1 prerequisites and the removal of manual COM registration requirements. 

For details, please refer to the section about upgrading to Jeeves ERP 2026.Q2.2 in the Jeeves ERP Upgrade considerations guide. 


![](images/Jeeves_ERP_2026.Q2.2_Release_notes_-EN-.pdf-0005-00.png)


## **Maintenance** 

Defects in Jeeves ERP 2026.Q2.2 must be verified in the Jeeves verification environment to be classified as a defect in Jeeves Incident management. This does not apply to customers with a support agreement. 

Bugs and support requests should be reported in Jeeves Incident management, with the relevant application (for example, General ledger or Inventory) specified as the “Category” and the full platform version number in the “Product Other” field. 

Corrections for critical or high-severity issues (severity level 1 or 2) will be published as patches via the <u>Jeeves Download Center.</u> 

Severity 1 corrections will be released as soon as possible. Any severity 2 corrections for the platform, as well as any application (JAS) corrections, will be released weekly. 

Corrections for medium- and low-severity issues (severity levels 3 and 4) will be included in an upcoming Jeeves ERP quarterly release or the next annual release, available via the <u>Jeeves Download Center.</u> 

## **Download** 

Jeeves ERP 2026.Q2.2 is available for download via the <u>Jeeves Download Center.</u> 

The standard APIs developed by Jeeves are delivered as packages via the <u>Jeeves Download Center.</u> 

Read more about our releases on the <u>Jeeves Product Releases</u> page in our Support portal. 

## **Cloud Services** 

To order Jeeves Cloud Services, for example, Federated authentication, eApproval Cloud or Jeeves API Platform, please use <u>Jeeves Cloud ERP Services Portal. If you have questions, contact your customer</u> account representative at Forterro Sweden. 

- For more information, go to the <u>Information about Cloud Services page.</u> 

## **Questions** 

If you have questions concerning Jeeves ERP 2026.Q2.2, please contact Jeeves Product Management. 

