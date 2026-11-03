APPLICATION OBJECTS WHEN PATCHING JEEVES ERP Created for supporting Third-party entities (Podmiot3) in the FA3 format 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Podmiot3_in_the_FA3_format.pdf-0002-00.png)


### **_Copyright notice_** 

- © Copyright Forterro Sweden AB.  All Rights Reserved. 

No part of this guide may be copied, reproduced, translated, or transmitted in any form or by any means without the prior written consent of Jeeves Information Systems AB. 

### _Document disclaimer_ 

Information contained in this guide is subject to change without notice. Please check with your Jeeves support team representative to make sure you have the most recent information. 

Page 2 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Podmiot3_in_the_FA3_format.pdf-0003-00.png)


## **Contents** 

|**_About this guide .................................................................................................................................. 4_**|
|---|
|**_List of files and objects ....................................................................................................................... 5_**|
|**Application objects to patch: ..................................................................................................................... 5**|
|New term(s) in APPL.TED: ............................................................................................................................................................................... 5|
|New user function(s) in APPL.UFU:.............................................................................................................................................................. 5|
|Changed user function(s) in APPL.UFU: .................................................................................................................................................... 5|
|New table(s) TBD\*.TBD: .................................................................................................................................................................................. 5|
|Changed table(s) TBD\*.TBD: ......................................................................................................................................................................... 5|
|Changed program(s) PGM\*.PGM: .............................................................................................................................................................. 5|
|Changed window context(s) WCD\*.WCD: .............................................................................................................................................. 5|
|New connection(s) CXX\*.CXX: ..................................................................................................................................................................... 5|
|Changed trigger(s) in TRG\*.TRG: ................................................................................................................................................................ 5|
|New procedure(s) in (UTV)SPR*.SPR .......................................................................................................................................................... 5|
|Changed procedure(s) in (UTV)SPR\.SPR: ................................................................................................................................................ 5|
|Error messages .................................................................................................................................................................................................... 5|



Page 3 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Podmiot3_in_the_FA3_format.pdf-0004-00.png)


# **About this guide** 

This document lists the objects and files which must be considered while updating the Jeeves ERP patch to support Third-party entities (Podmiot3) in the FA3 format. 

**Note** 

This functionality is delivered as hotfixes to the supported versions of Jeeves; along with information about the versions on the respective hotfix levels on which they are tested. 

Page 4 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Podmiot3_in_the_FA3_format.pdf-0005-00.png)


**List of files and objects Application objects to patch:** **_New term(s) in APPL.TED:_** KusFtgNr 

**_New user function(s) in APPL.UFU:_** UF_Check_PL3rdPartyInfo_Records 

**_Changed user function(s) in APPL.UFU:_** Uf_CalcPL3rdPartyInfoRowno 

**_New table(s) TBD\*.TBD:_** PL3rdPartyInfo.tbd 

**_Changed table(s) TBD\*.TBD:_** kus.tbd sy2.tbd **_Changed program(s) PGM\*.PGM:_** kus.pgm **_Changed window context(s) WCD\*.WCD:_** PL3rdPartyInfo.wcd 

**_New connection(s) CXX\*.CXX:_** Kus_1toM_PL3rdPartyInfo.cxx 

**_Changed trigger(s) in TRG\*.TRG:_** kus.trg PL3rdPartyInfo.trg sy2.trg 

**_New procedure(s) in (UTV)SPR*.SPR_** Jeeves_Copy_Podmiot3_Info.spr 

**_Changed procedure(s) in (UTV)SPR\.SPR:_** Jeeves_Upd_1527.spr 

**_Error messages_** 

Note that new error messages are available in the language package. 

Page 5 | 6 


![](images/Application_objects_when_patching_Jeeves_ERP_to_Podmiot3_in_the_FA3_format.pdf-0006-00.png)


You can download and apply the latest language package to display these messages in Jeeves ERP as follows: 

1. After the complete installation of Jeeves application, navigate to the **Packages** folder in your Jeeves application folder. Both English (Lang_sw.JSP.zip) and Swedish (Lang_se.JSP.zip) language packages can be found here. 

2. Launch **JeevesPackageManager.exe** and import these language packages into your database. 3. The default language needs to be set up for standard records at the company level in the Language (SprakKod) field in the System data, own company (sy1) program. Refer to Jeeves online documentation for Language codes. 

Page 6 | 6 

