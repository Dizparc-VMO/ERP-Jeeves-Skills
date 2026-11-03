APPLICATION OBJECTS WHEN PATCHING JEEVES ERP Created for supporting Poland eInvoices via KSeF - Supplier payments outgoing 


![](images/Application_objects_when_patching_Jeeves_ERP_for_KSeF_-_Supplier_payments_outgoing.pdf-0002-00.png)


### **_Copyright notice_** 

- © Copyright Forterro Sweden AB.  All Rights Reserved. 

No part of this guide may be copied, reproduced, translated, or transmitted in any form or by any means without the prior written consent of Jeeves Information Systems AB. 

### _Document disclaimer_ 

Information contained in this guide is subject to change without notice. Please check with your Jeeves support team representative to make sure you have the most recent information. 

Page 2 | 5 


![](images/Application_objects_when_patching_Jeeves_ERP_for_KSeF_-_Supplier_payments_outgoing.pdf-0003-00.png)


## **Contents** 

|**_About this guide .................................................................................................................................. 4_**|
|---|
|**_List of files and objects ....................................................................................................................... 5_**|
|**Application objects to patch: ..................................................................................................................... 5**|
|New user function(s) in APPL.UFU:.............................................................................................................................................................. 5|
|Changed table(s) TBD\*.TBD: ......................................................................................................................................................................... 5|
|Changed window context(s) WCD\*.WCD: .............................................................................................................................................. 5|
|Changed trigger(s) in TRG\*.TRG: ................................................................................................................................................................ 5|
|Changed procedure(s) in (UTV)SPR\.SPR: ................................................................................................................................................ 5|
|Error messages .................................................................................................................................................................................................... 5|



Page 3 | 5 


![](images/Application_objects_when_patching_Jeeves_ERP_for_KSeF_-_Supplier_payments_outgoing.pdf-0004-00.png)


# **About this guide** 

This document lists the objects and files which must be considered while updating the Jeeves ERP patch to support Poland eInvoices via KSeF - Supplier payments outgoing. 

### **Note** 

This functionality is delivered as hotfixes to the supported versions of Jeeves; along with information about the versions on the respective hotfix levels on which they are tested. 

Page 4 | 5 


![](images/Application_objects_when_patching_Jeeves_ERP_for_KSeF_-_Supplier_payments_outgoing.pdf-0005-00.png)


# **List of files and objects Application objects to patch:** 

**_New user function(s) in APPL.UFU:_** UF_lrfb_Fetch_KsefRefNo UF_wLrfbF_lrfb_KSefRefNo_PFC 

**_Changed table(s) TBD\*.TBD:_** lrfb.tbd 

**_Changed window context(s) WCD\*.WCD:_** 

wLrfb.wcd wLrfbAvp.wcd wLrfbMak.wcd 

**_Changed trigger(s) in TRG\*.TRG:_** lrfb.trg 

**_Changed procedure(s) in (UTV)SPR\.SPR:_** 

FBS_Create.spr JEEVES_Create_SEPA_FI_Fbs.spr JEEVES_Create_SEPA_FI_BNPParibas.spr 

## **_Error messages_** 

Note that new error messages are available in the language package. 

You can download and apply the latest language package to display these messages in Jeeves ERP as follows: 

1. After the complete installation of Jeeves application, navigate to the **Packages** folder in your Jeeves application folder. Both English (Lang_sw.JSP.zip) and Swedish (Lang_se.JSP.zip) language packages can be found here. 

2. Launch **JeevesPackageManager.exe** and import these language packages into your database. 

3. The default language needs to be set up for standard records at the company level in the Language (SprakKod) field in the System data, own company (sy1) program. Refer to Jeeves online documentation for Language codes. 

Page 5 | 5 

