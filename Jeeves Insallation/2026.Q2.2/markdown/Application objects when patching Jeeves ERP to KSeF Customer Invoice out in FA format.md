APPLICATION OBJECTS WHEN PATCHING JEEVES ERP Created for supporting KSeF Customer Invoice out in FA format 


![](images/Application_objects_when_patching_Jeeves_ERP_to_KSeF_Customer_Invoice_out_in_FA_format.pdf-0002-00.png)


### **_Copyright notice_** 

- © Copyright Forterro Sweden AB.  All Rights Reserved. 

No part of this guide may be copied, reproduced, translated, or transmitted in any form or by any means without the prior written consent of Jeeves Information Systems AB. 

### _Document disclaimer_ 

Information contained in this guide is subject to change without notice. Please check with your Jeeves support team representative to make sure you have the most recent information. 

Page 2 | 7 


![](images/Application_objects_when_patching_Jeeves_ERP_to_KSeF_Customer_Invoice_out_in_FA_format.pdf-0003-00.png)


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
|New program(s) PGM\*.PGM: ....................................................................................................................................................................... 5|
|Changed program(s) PGM\*.PGM: .............................................................................................................................................................. 6|
|New window context(s) WCD\*.WCD: ....................................................................................................................................................... 6|
|Changed window context(s) WCD\*.WCD: .............................................................................................................................................. 6|
|New connection(s) CXX\*.CXX: ..................................................................................................................................................................... 6|
|Changed trigger(s) in TRG\*.TRG: ................................................................................................................................................................ 7|
|Changed procedure(s) in (UTV)SPR\.SPR: ................................................................................................................................................ 7|
|Changed Package(s): ........................................................................................................................................................................................ 7|
|Error messages .................................................................................................................................................................................................... 7|



Page 3 | 7 


![](images/Application_objects_when_patching_Jeeves_ERP_to_KSeF_Customer_Invoice_out_in_FA_format.pdf-0004-00.png)


# **About this guide** 

This document lists the objects and files which must be considered while updating the Jeeves ERP patch to support the KSeF Customer Invoice out in FA format. 

### **Note** 

This functionality is delivered as hotfixes to the supported versions of Jeeves; along with information about the versions on the respective hotfix levels on which they are tested. 

Page 4 | 7 


![](images/Application_objects_when_patching_Jeeves_ERP_to_KSeF_Customer_Invoice_out_in_FA_format.pdf-0005-00.png)


# **List of files and objects Application objects to patch:** 

**_New term(s) in APPL.TED:_** PriceDispOption CorrectionReason IDWew PL3PrtyRoleDescr PL3PrtyRoleID ThirdPartyType 

**_New user function(s) in APPL.UFU:_** Uf_CalcPL3rdPartyInfoRowno UF_FetchFrDetails UF_PL3rdPartyInfo_ClearDetailFields UF_PL3rdPartyInfo_EnterAddMode, UF_PL3rdPartyInfo_PreInsert UF_PL3rdPartyInfo_PreUpdate UF_PL3rdPartyInfo_ProgramNodeStarts UF_PL3rdPartyInfo_SetDetailFieldState UF_PL3rdpartyinfo_SetFieldState 

**_Changed user function(s) in APPL.UFU:_** UF_Oh_From_Fh_Korr UF_Uoh_Create_Fh_Copy 

**_New table(s) TBD\*.TBD:_** PL3rdPartyInfo.tbd, PL3rdPartyRole.tbd 

**_Changed table(s) TBD\*.TBD:_** sy1.tbd sy2.tbd einvoiceadm.tbd fh.tbd oh.tbd uoh.tbd fr.tbd 

**_New program(s) PGM\*.PGM:_** PL3rdPartyRole.pgm 

Page 5 | 7 


![](images/Application_objects_when_patching_Jeeves_ERP_to_KSeF_Customer_Invoice_out_in_FA_format.pdf-0006-00.png)


**_Changed program(s) PGM\*.PGM:_** FhKorrP.pgm Order1.pgm uoh.pgm Order.pgm **_New window context(s) WCD\*.WCD:_** PL3rdPartyInfo.wcd PL3rdPartyRole.wcd **_Changed window context(s) WCD\*.WCD:_** sy.wcd Sy1Kr.wcd Sy1Lager.wcd Sy1Utb.wcd fh.wcd FhBetF.wcd FhFin.wcd FhInk.wcd fhKAvst.wcd fhop.wcd FhRest.wcd FhUtbet.wcd OrderBH.wcd OrderFromQA.wcd OrderH.wcd OrderPH.wcd OrderShuffle.wcd ordofh.wcd OrdPH.wcd uoh.wcd wFh2vt.wcd WFhFakt.wcd WFhOrder.wcd wFhXx.wcd WFskFh.wcd WOhSok.wcd wUoh2.wcd fr.wcd, mfr.wcd 

**_New connection(s) CXX\*.CXX:_** oh_1toM_PL3rdPartyInfo.cxx 

Page 6 | 7 


![](images/Application_objects_when_patching_Jeeves_ERP_to_KSeF_Customer_Invoice_out_in_FA_format.pdf-0007-00.png)


sy1_1toM_PL3rdPartyRole.cxx Uoh_1toM_PL3rdPartyInfo.cxx Fr_1toM_PL3rdPartyInfo.cxx 

**_New trigger(s) in TRG\*.TRG:_** PL3rdPartyInfo.trg PL3rdPartyRole.trg 

**_Changed trigger(s) in TRG\*.TRG:_** fh.trg oh.trg sy2.trg uoh.trg fr.trg 

## **_Changed procedure(s) in (UTV)SPR\.SPR:_** 

Jeeves_FN_Get_TermLangText.spr JEEVES_Oh_From_Fh.spr JEEVES_Oh_From_Fh_Worp.spr JEEVES_Uoh_Create_Fh_Copy.spr Jeeves_Upd_1525.spr (Version 20260) Jeeves_Upd_1521.spr (Version 20250) 

Jeeves_FA_Format_Polish.spr: Note that this procedure is not created as part of Jeeves standard. All objects are delivered only in the FA3.JSP package. 

**_Changed Package(s):_** FA3.JSP 

## **_Error messages_** 

Note that new error messages are available in the language package. 

You can download and apply the latest language package to display these messages in Jeeves ERP as follows: 

1. After the complete installation of Jeeves application, navigate to the **Packages** folder in your Jeeves application folder. Both English (Lang_sw.JSP.zip) and Swedish (Lang_se.JSP.zip) language packages can be found here. 

2. Launch **JeevesPackageManager.exe** and import these language packages into your database. 

3. The default language needs to be set up for standard records at the company level in the Language (SprakKod) field in the System data, own company (sy1) program. Refer to Jeeves online documentation for Language codes. 

Page 7 | 7 

