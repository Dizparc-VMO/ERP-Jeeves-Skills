
![](images/Tested_platforms_and_test_activities_Jeeves_ERP_2026.Q2.2.pdf-0001-00.png)


©2026Jeeves Information Systems AB.  All rights reserved. 

Jeeves ERP 2026.2 Tested platforms and test activities 

#### **Copyright notice** 

©Forterro Sweden AB. All rights reserved. 

No part of this guide may be copied, reproduced, translated, or transmitted in any form or by any means without the prior written consent of Jeeves Information Systems AB. 

#### **Document disclaimer** 

Information contained in this guide is subject to change without notice. Please check with your Jeeves support team representative to make sure you have the most recent information. 

©2026 Jeeves Information Systems AB. All rights reserved. 

2 (7) 

Contents 


![](images/Tested_platforms_and_test_activities_Jeeves_ERP_2026.Q2.2.pdf-0003-01.png)


# **Contents** 

|**1**|**Tested platforms ............................................................................................................ 4**|
|---|---|
|1.1|Server-side software.................................................................................................................................. 4|
|1.2|Client platforms........................................................................................................................................... 4|
|1.3|Third party integration software.......................................................................................................... 4|
|1.4|Cloud Setup.................................................................................................................................................... 4|
|1.5|Mobility Setup............................................................................................................................................... 4|
|**2**|**Test activities ................................................................................................................. 5**|
|2.1|Main test activities..................................................................................................................................... 5|
|2.1.1|Functional test for application ............................................................... 5|
|2.1.2|Regression test .................................................................................. 5|
|2.1.3|Acceptance test ................................................................................. 7|



©2026 Jeeves Information Systems AB. All rights reserved. 

3 (7) 

Tested Platforms and Activities JeevesERP2026.2 


![](images/Tested_platforms_and_test_activities_Jeeves_ERP_2026.Q2.2.pdf-0004-01.png)


# 1 Tested platforms 

## 1.1 Server-side software 

|**Software**|**Version(s)**|
|---|---|
|Operating system|Microsoft Windows server 2025<br>Microsoft Windows server 2022|
|Database server|Microsoft SQL server 2025 (CU 7)|



## 1.2 Client platforms 

|**Operating system **|**Jeeves client setup**|
|---|---|
|Microsoft Windows 11 version 25H2<br>(Build: 26200.9168)|Jeeves Classic client, Desktop client<br>ConnectionType=6 (Clients are connected through Client<br>broker and directed to the server)|



## 1.3 Third party integration software 

|**Product version**|**Jeeves client**|**Operating system**|
|---|---|---|
||**setup**||
|.NET 3.5, 4.5.2, 4.6.2,4.8, Core<br>10.0|64-bit client|Windows 11|
|MS Office 365|64-bit client|Windows 11|



## 1.4 Cloud Setup 

|**Operating system**|**SQL server**|**Jeeves client setup**|
|---|---|---|
|Windows Server 2022<br>Client Win 11 version 25H2<br>(Build: 26200.8457)|SQL Server 2025 (CU7)|Desktop client and DesignStudio,<br>Upgrade installation of JAS 2024.0 to<br>JAS 2026.2<br>Port=4502, Connectiontype=6,<br>ClientBrokerMode=3<br>Login with Federated authentication<br>enabled|
|Windows Server 2025<br>(SDM3)<br>Client Win 11 version 25H2<br>(Build: 26200.9168)|SQL Server 2025 (CU7)|Desktop client and DesignStudio<br>Login with Federated authentication<br>only|



## 1.5 Mobility Setup 

|**Operating system**|**SQL server**|**Jeeves Mobile setup**|
|---|---|---|
|iOS Version 26.2|SQL 2022 (CU 27)|1.54.1|
|Android Version 16|SQL 2022 (CU 27)|1.55|



©2026 Jeeves Information Systems AB. All rights reserved. 

4 (7) 

Tested Platforms and Activities JeevesERP2026.2 


![](images/Tested_platforms_and_test_activities_Jeeves_ERP_2026.Q2.2.pdf-0005-01.png)


# 2 Test activities 

The following types of tests have been made - functional tests, regression tests, and acceptance tests. 

During functional testing, all the corrected errors that were approved for this release, and new features included in this release, were tested to ensure that these worked as expected. 

During regression testing, application functionality was tested using Jeeves’ standard processes defined in the user guides. Extended functionality tests were run within each module besides the user guide tests. All the new features that are included in Jeeves ERP 2026.Q2.2 and all errors with severity 1 and 2 corrected since last release were validated again in the regression test environment to ensure product quality. The purpose of the regression tests was to ensure that the standard processes/functionality passed. 

During acceptance testing, application functionality was tested using end user workflows. The focus was to verify that the corrected errors detected during the regression tests passed and were working as intended. The objective of the acceptance tests was to approve the version to be delivered. 

The test environments were based on the standard menu, template companies and role-based user interface. The setup also included normal users, users with single sign on and with the security manager activated to test the application. 

## 2.1 Main test activities 

### 2.1.1 Functional test for application 

- **<mark>New enhancements</mark>** 

- **<mark>Corrected error reports</mark>** 

### 2.1.2 Regression test 

- **<mark>Application</mark>** 

New installation 

Upgraded installations from (JAS version 2024.0, 2025.0 and 2026.0) to latest 2026.2 

Following is a list of tested business process flows, covering functionality across Jeeves modules based on Jeeves user guides: Production Sales Purchases Inventory ICT Service Product configurator General ledger Accounts receivables Accounts payables EDM WMS cloud printing support WMS smoke pass Split functionality in arrival Application and WMS unit test execution. EDI Order, Order Response, Delivery Plan, Order Change and Invoice response 

©2026 Jeeves Information Systems AB. All rights reserved. 

5 (7) 

Tested Platforms and Activities JeevesERP2026.2 


![](images/Tested_platforms_and_test_activities_Jeeves_ERP_2026.Q2.2.pdf-0006-01.png)


Serial number was not set on stock ARSI record when processing credit order returns Handling the Podmiot3 (3<sup>rd</sup> party) element for FA(3) file Language handling in FA(3) file Advance invoices: non-printable order rows excluded from FA(3) file More details about the advance invoice(s) linked to the settlement invoice displayed in FA(3) file Support KSeF information in Supplier payments outgoing and Import of bank payment files Exploratory testing for all modules 

- **<mark>Platform</mark>** 

Jeeves Outbound Service Jeeves Console and Identity Service Cloud Printing integration flow Backward Compatibility for SQL Tunnel Cloud Agent. Federated login for Desktop Client File Comparison and Digital Signature Exploratory testing related to focus. Desktop client - User defined connections tests. Security Manager – Basic test. Security Modes Package Manager. Communication Layer Test. Performance Testing - Latest Desktop Client EDM testing specific to S3. Design studio workflows using Jeeves Server running on IIS. Cloud report - Basic test (Query, procedure reports including params, Macro reports). Federated login for Design studio Digital Signature of dlls Design studio Smoke tests - Existing functionalities 

- **<mark>Mobility</mark>** 

Federated Login for Mobility Mobile order workflow using IPAD and mobile device(Split screen and List window navigation tests) Online field service app flow Notification services Mobile apps simulate bad network scenarios 

- **<mark>PEPPOL</mark>** 

Polish Ksef Outgoing Invoice along with outgoing PDF retrieval Polish Ksef Incoming Invoice Smoke Pass: Pagero integration service (Outgoing and Incoming invoices including Business Response) Smoke Pass: CreditFlow/OptoSwedenSender Outgoing invoices Message broker cloud agent backward compatibility test with previous supported Application versions (2024.0 and 2025.0) 

©2026 Jeeves Information Systems AB. All rights reserved. 

6 (7) 

Tested Platforms and Activities JeevesERP2026.2 


![](images/Tested_platforms_and_test_activities_Jeeves_ERP_2026.Q2.2.pdf-0007-01.png)


- **<mark>e-Approval</mark>** 

eApproval cloud regression test including EDM eApproval PDF viewer test 

- **<mark>Automation tests</mark>** 

e-Approval main workflows Desktop main workflows Mobility main workflows Finance API Sales API Jeeves API Peppol flow Online Doc UI 

### 2.1.3 Acceptance test 

Environment setup Upgraded installation from (JAS 2025.0,2024.0) to latest 2026.2 End user workflow – Classic and Desktop clients Bug revalidation- Application Bug revalidation- Platform File comparison, digital signature Translation test - 8 supported languages Correction of errors found during regression test 

©2026 Jeeves Information Systems AB. All rights reserved. 

7 (7) 

