class LoginPageLocators:
    userNameField = "//input[@id='usernameLogin']"
    passWordField = "//input[@id='passwordLogin']"
    loginBtn = "//input[@id='loginbtn']"

class MenuLocators:
    salesManagementMenu = "//div[text()='Sales Management']"
    salesInvoiceSubMenu = "//div[text()='Sales Invoice']"
    salesInvoiceLabel = "(//div[@class='x-autocontainer-innerCt']//label//b)[3]"

class salesInvoicePageLocators:
    loggedInAs = "//label[@id='labelparametersettings']//b"
    CreateNewBtn = "//span[@id='gst_invoicecreateBtnId-btnInnerEl']"

class salesDetailsFieldLocators:
    branchId = "//input[@id='gst_invoice-branchid']"
    documentDate = "//input[@id='gst_invoice-docdate-id-inputEl']"
    warningAlert = "//*[normalize-space(text())='OK']"
    reverseChargeYesOrNo = "//input[@id='gst_invoice-revchargeyn-id-inputEl']"
    invoiceFor = "//input[@id='gst_invoice-gstinvfor-id-inputEl']"
    voucherType = "//input[@id='gst_invoice-vchtype']"
    documentId = "//input[@id='gst_invoice-docid-id-inputEl']"
    typeOfPay = "//input[@id='gst_invoice-typeofpay-id-inputEl']"
    salesType = "//input[@id='gst_invoice-salestype-id-inputEl']"
    invoiceType = "//input[@id='gst_invoice-invtype-id-inputEl']"
    tcsYesOrNo = "//input[@id='gst_invoice-tdsyn-id-inputEl']"
    taxApplicable = "//input[@id='gst_invoice-taxapp-id-inputEl']"

class customerDetailsFieldLocators:
    customerId = "//input[@id='gst_invoice-partyid']"
    warningAlert = "//span[@id='button-1009-btnInnerEl']"
    transactionForTheYear = "//input[@id='gst_invoice-translimt-id-inputEl']"
    deliveryAt = "//input[@id='gst_invoice-goodsstate']"
    interOrIntraState = "//input[@id='gst_invoice-statetype-id-inputEl']"
    soOrDcNo = "//input[@id='gst_invoice-dcno']"
    soOrDcDate = "//input[@id='gst_invoice-logicaldcno_docdate-id-inputEl']"
    customerPoNo = "//input[@id='gst_invoice-refno-id-inputEl']"
    customerPODate = "//input[@id='gst_invoice-refdate-id-inputEl']"

class otherDetailsFieldLocators:
    selectCashOrBankAccount = "//input[@id='gst_invoice-custacc']"
    issuingLocation = "//input[@id='gst_invoice-isslocid']"
    ShipmentTo = "//input[@id='gst_invoice-stype']"
    dispatchFromDefaultAddress = "//input[@id='gst_invoice-ddtype-id-inputEl']"
    
class viewAddressFieldLocators:
    viewAddress = "//span[@id='gst_invoice-viewaddress-id-btnInnerEl']"
    shipTo_GST_No ="//input[@id='gst_invoice-logicalsparty_agstno-id-inputEl']"
    shipTo_Address1 = "//input[@id='gst_invoice-logicalsparty_shiptoadd1-id-inputEl']" 
    shipTo_Address2 = "//input[@id='gst_invoice-logicalsparty_shiptoadd2-id-inputEl']"
    shipTo_Address3 = "//input[@id='gst_invoice-logicalsparty_shiptoadd3-id-inputEl']"
    shipToCityName = "//input[@id='gst_invoice-logicalsparty_shiptopcity-id-inputEl']"
    shipToStateName = "//input[@id='gst_invoice-logicalsparty_shiptostatename-id-inputEl']"
    shipToPincode = "//input[@id='gst_invoice-logicalsparty_shiptopincode-id-inputEl']"
    saveBtn = "//span[@id='button-1134-btnInnerEl']"
    cancelBtn = "//span[@id='button-1135-btnInnerEl']"

class CurrencyDetailsLocators:
    currency = "//input[@id='gst_invoice-maincurrency']"
    transactionExchangeRate = "//input[@id='gst_invoice-exrate-id-inputEl']"
    termsAndConditions = "//input[@id='gst_invoice-tandctemp']"
    taxAndOtherDetails = "//span[@id='tab-1086-btnInnerEl']"

class SummaryFieldLocators:
    grossAmount = "//input[@id='gst_invoice-gross-id-inputEl']"
    netAmount = "//input[@id='gst_invoice-netamt-id-inputEl']"
    amountInWords = "//input[@id='gst_invoice-amtwords-id-inputEl']"
    narration = "//textarea[@id='gst_invoice-narration-id-inputEl']"

class TransportDetailsFieldLocators:
    eWayBillRequest = "//input[@id='gst_invoice-ewaybillyn-id-inputEl']"
    modeOfTransport = "//input[@id='gst_invoice-modeoftransport-id-inputEl']"
    vehicleType = "//input[@id='gst_invoice-vehicletype-id-inputEl']"
    vehicleNo = "//input[@id='gst_invoice-vehicleno-id-inputEl']"
    distance = "//input[@id='gst_invoice-dist-id-inputEl']"

    

