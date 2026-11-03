
![](images/Jeeves_ERP_Patch_delivery_process.pdf-0001-00.png)


- © Copyright Forterro Sweden AB. All Rights Reserved. 

**Jeeves ERP Patch delivery process** 

##### **Copyright notice** 

- © Copyright Forterro Sweden AB. All Rights Reserved. 

No part of this guide may be copied, reproduced, translated, or transmitted in any form or by any means without the prior written consent of Jeeves Information Systems AB. 

##### **Document disclaimer** 

Information contained in this guide is subject to change without notice. Please check with your Jeeves support team representative to make sure you have the most recent information. 

© Copyright Forterro Sweden AB. All Rights Reserved. 

2 (8) 

<u>Contents</u> 


![](images/Jeeves_ERP_Patch_delivery_process.pdf-0003-01.png)


# **Contents** 

|**1**|**About this guide ........................................................................................................... 4**|
|---|---|
|1.1|Document version/revision..................................................................................................................... 4|
|1.2|Audience.......................................................................................................................................................... 4|
|1.3|Document conventions.............................................................................................................................. 4|
|1.4|List of acronyms........................................................................................................................................... 4|
|**2**|**Patch delivery in Jeeves ............................................................................................. 5**|
|2.1|Patch delivery for Platform.................................................................................................................... 5|
|2.1.1|Manifest file ...................................................................................... 5|
|2.2|Patch delivery for Application............................................................................................................... 7|
|**3**|**Build number format ................................................................................................... 8**|
|3.1|Build number format of Platform......................................................................................................... 8|
|3.2|Build number format of Application................................................................................................... 8|



© Copyright Forterro Sweden AB. All Rights Reserved. 

3 (8) 

<u>About this guide</u> 


![](images/Jeeves_ERP_Patch_delivery_process.pdf-0004-01.png)


# 1 About this guide 

This guide describes the patch delivery process followed by Jeeves for Platform and Application parts. This process applies to Jeeves ERP 2026.Q2.2 and later versions. 

## 1.1 Document version/revision 

|**Version/revision**|**Description**|**Date**|
|---|---|---|
|1.0|Created patch delivery process doc<br>followed byJeeves|March 2026|
|1.1|Updated patch delivery package folder<br>contents asper 2026.Q2.2 release|August 2026|



## 1.2 Audience 

This guide is meant for technicians with knowledge of Jeeves ERP who will install and configure Jeeves ERP components. 

## 1.3 Document conventions 

Use of typographic conventions in documentation helps users locate and interpret information easily. The following guidelines present specific typographic conventions. This guide enables you to establish and maintain a common understanding of various conventions used in the document. For simplicity and consistency, this guide describes the method of performing tasks. Other conventions used in this guide are listed in the following table. 

|**Representation **|**Description **|
|---|---|
|Bold text|Procedures, references to screens, dialog boxes and their<br>elements,file and folder names,commands,and buttons.|
|Numbered list|Stepwise instructions.|
|Bulleted list|Sets of features or options used toperform an activity.|
|Note text|Anyexception,extra information,orpitfalls.|
|Italic text|References to related documents and information.|



## 1.4 List of acronyms 

|**Acronym **|**Description **|
|---|---|
|AWS|Amazon web service|
|DNS|Domain name system|
|ECS|Elastic container service|
|SMTP|Simple mail transferprotocol|
|URL|Uniform resource locator|
|VPC|Virtualprivate cloud|



© Copyright Forterro Sweden AB. All Rights Reserved. 

4 (8) 

<u>Patch delivery in Jeeves</u> 


![](images/Jeeves_ERP_Patch_delivery_process.pdf-0005-01.png)


# 2 Patch delivery in Jeeves 

Jeeves ERP consists of two main parts: Application and Platform. 

- The Application contains the business logic and the data used in the system. 

- The Platform includes the components that interact with the Application and make it available to end users through APIs and client interfaces. 

Patches for the Application and Platform are delivered separately. 

## 2.1 Patch delivery for Platform 

Each Platform patch delivery includes all the platform components, packaged in a single folder. 

The package folder (for example: …\\Patch_deliveries\v2026.2) contains a ZIP file with the platform components, along with the release notes and a manifest file: 

- Classic Server 

- Classic Util 

- Client Broker 

- Control Client 

- Design Studio 

- ERP Client 

- NewLocalBusinessServer 

- Rest Service 

- SiteDB 

- ReleaseManifest.json (manifest file) 

- Release notes 

Although every patch delivery includes all components, only some may be updated in a given release. Each package contains a manifest file in JSON format listing the version of every component. By comparing the current manifest file with the new one, it is possible to identify which components have changed and update only them. 

### 2.1.1 Manifest file 

Each Platform patch delivery includes a manifest file in JSON format named ReleaseManifest.json. This file provides: 

- A list of all components included in the delivery 

- The file version of each component 

- Compatibility details validated during testing 

The manifest file can be used to compare component versions between patch deliveries and to identify which components are impacted by the update. 

Example of the manifest file (JSON format): 

<mark>{ "ProductVersion": "2026.2", "Branch": "2026.2", "Patch": 0, "Date": "2026-08-28 04:38:39 PM", "Components": { "ClassicServer": { "Version": "26.2.26240.01", "Date": "2026-08-28 09:30:41 AM"</mark> 

© Copyright Forterro Sweden AB. All Rights Reserved. 

5 (8) 

<u>Patch delivery in Jeeves</u> 


![](images/Jeeves_ERP_Patch_delivery_process.pdf-0006-01.png)


<mark>}, "ControlClient": { "Version": "26.2.26240.01", "Date": "2026-08-28 09:26:07 AM" }, "ClientBroker": { "Version": "26.2.26240.01", "Date": "2026-08-03 09:24:29 PM" }, "ClassicUtils": { "Version": "26.2.26240.01", "Date": "2026-08-28 09:26:26 AM" }, "ERPClient": { "Version": "26.2.26240.01", "Date": "2026-08-28 10:14:21 AM" }, "DesignStudio": { "Version": "26.2.26240.01", "Date": "2026-08-28 10:15:32 AM" }, "NewLocalBusinessServer": { "Version": "26.2.26240.01", "Date": "2026-08-28 09:41:02 AM" }, "RestService": { "Version": "26.2.26240.01", "Date": "2026-08-28 09:28:16 AM" }, "SiteDB": { "Version": "26.2.26240.01", "Date": "2026-08-28 09:25:02 AM" } }</mark> <u><mark>}</mark></u> 

#### **<u>Note:</u>** 

The **Patch** value is updated each time a new patch is released. 

© Copyright Forterro Sweden AB. All Rights Reserved. 

6 (8) 

<u>Patch delivery in Jeeves</u> 


![](images/Jeeves_ERP_Patch_delivery_process.pdf-0007-01.png)


## 2.2 Patch delivery for Application 

Each Application patch delivery contains all the application objects related to the specific update, packaged in a single folder. 

The package folder includes a ZIP file containing the updated application objects and a Corrections and Enhancements report in HTML format. 

#### **<u>Note:</u>** 

Unlike Platform patches, Application patch deliveries do not include a manifest file. 

© Copyright Forterro Sweden AB. All Rights Reserved. 

7 (8) 

<u>Build number format</u> 


![](images/Jeeves_ERP_Patch_delivery_process.pdf-0008-01.png)


# 3 Build number format 

The build number formats of Platform and Application components are as follows: 

## 3.1 Build number format of Platform 

Build number format of Platform components: 

{{Version Number}}_{{ShortReleaseYear}}.{{ReleaseUpdate}}.{{ShortYear}}{{DayOfBuild}}.{{Revision}} 

For example: 2025.0_26.0.26010.1 Where: 

- 2025.0 → Version number 

- 26.0 → Short release year.Release update 

- 26010 → 10th day of the build release year 20 **26** 

- .1 → Revision number 

## 3.2 Build number format of Application 

Build number format of Application components: 

Jeeves ERP {{ReleaseYear}}.{{Update}}.{{Update Number}} / {{Patch Number}} / {{Build Date Time}} / JAS{{Year}}{{Quarter}}HF_{{YearOfBuild}}{{MonthOfBuild}}{{DayOfBuild}}.{{Revision}} 

For example: Jeeves ERP 2024.Q2.3 / Patch13 / 2025-03-28 09:11:00 / JAS20243HF_20250327.1 Where: 

- Jeeves ERP 2024.Q2.3 → Release year.Release update number 

- Patch13 → Patch number 

- 2025-03-28 09:11:00 → Build date and time 

- JAS20243 → JAS year and quarter 

- HF_20250327 → Build year (2025), month (03), day (27) 

- .1 → Revision number 

© Copyright Forterro Sweden AB. All Rights Reserved. 

8 (8) 

