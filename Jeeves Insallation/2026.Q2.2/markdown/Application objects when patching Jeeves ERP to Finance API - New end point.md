APPLICATION OBJECTS WHEN PATCHING JEEVES ERP Created for supporting Finance API - New end point 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Finance_API_-_New_end_point.pdf-0002-00.png)


### **_Copyright notice_** 

- © Copyright Forterro Sweden AB.  All Rights Reserved. 

No part of this guide may be copied, reproduced, translated, or transmitted in any form or by any means without the prior written consent of Jeeves Information Systems AB. 

### _Document disclaimer_ 

Information contained in this guide is subject to change without notice. Please check with your Jeeves support team representative to make sure you have the most recent information. 

Page 2 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Finance_API_-_New_end_point.pdf-0003-00.png)


## **Contents** 

|**_About this guide .................................................................................................................................. 4_**|
|---|
|**_List of files and objects ....................................................................................................................... 5_**|
|**Application objects to patch: ..................................................................................................................... 5**|
|New term(s) in APPL.TED: ............................................................................................................................................................................... 5|
|New table(s) TBD\*.TBD: .................................................................................................................................................................................. 5|
|Changed table(s) TBD\*.TBD: ......................................................................................................................................................................... 5|
|New program(s) PGM\*.PGM: ....................................................................................................................................................................... 5|
|Changed program(s) PGM\*.PGM: .............................................................................................................................................................. 5|
|New window context(s) WCD\*.WCD: ....................................................................................................................................................... 5|
|New connection(s) CXX\*.CXX: ..................................................................................................................................................................... 5|
|New trigger(s) in TRG\*.TRG: ......................................................................................................................................................................... 5|
|Changed trigger(s) in TRG\*.TRG: ................................................................................................................................................................ 5|
|New procedure(s) in (UTV)SPR\.SPR: .......................................................................................................................................................... 6|
|Error messages .................................................................................................................................................................................................... 6|



Page 3 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Finance_API_-_New_end_point.pdf-0004-00.png)


# **About this guide** 

This document lists the objects and files which must be considered while updating the Jeeves ERP patch to support Finance API - New end point. 

### **Note** 

This functionality is delivered as hotfixes to the supported versions of Jeeves; along with information about the versions on the respective hotfix levels on which they are tested. 

Page 4 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Finance_API_-_New_end_point.pdf-0005-00.png)


# **List of files and objects Application objects to patch:** 

**_New term(s) in APPL.TED:_** ErrorCode ErrorMessage ImportLogID InvoiceNo ProcessingFlow SupplierID 

**_New table(s) TBD\*.TBD:_** ImportSuppInvcLog.tbd 

**_Changed table(s) TBD\*.TBD:_** PrelimPvLr.tbd pvlr.tbd sy2.tbd 

**_New program(s) PGM\*.PGM:_** ImportSuppInvcLog.pgm 

**_Changed program(s) PGM\*.PGM:_** xPrelimPvLr.pgm xPvlr.pgm 

**_New window context(s) WCD\*.WCD:_** ImportSuppInvcLog.wcd 

**_New connection(s) CXX\*.CXX:_** PrelimPvLr_1toM_ImportSuppInvcLog.cxx Pvlr_1toM_ImportSuppInvcLog.cxx Sy1_1toM_ImportSuppInvcLog.cxx 

**_New trigger(s) in TRG\*.TRG:_** ImportSuppInvcLog.trg 

**_Changed trigger(s) in TRG\*.TRG:_** PrelimPvLr.trg pvlr.trg sy2.trg 

Page 5 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Finance_API_-_New_end_point.pdf-0006-00.png)


**_New procedure(s) in (UTV)SPR\.SPR:_** Jeeves_API_ImportSuppInvoice_XML.spr Jeeves_Calculate_SequentialDiscounts.spr 

## **_Error messages_** 

Note that new error messages are available in the language package. 

You can download and apply the latest language package to display these messages in Jeeves ERP as follows: 

1. After the complete installation of Jeeves application, navigate to the **Packages** folder in your Jeeves application folder. Both English (Lang_sw.JSP.zip) and Swedish (Lang_se.JSP.zip) language packages can be found here. 

2. Launch **JeevesPackageManager.exe** and import these language packages into your database. 

3. The default language needs to be set up for standard records at the company level in the Language (SprakKod) field in the System data, own company (sy1) program. Refer to Jeeves online documentation for Language codes. 

Page 6 | 6 

