import requests
import xml.etree.ElementTree as etree
import sys
from datetime import date, datetime

dollarCurrencyCode = "R01235"
euroCurrencyCode = "R01239"

dateFrom = datetime.strptime(sys.argv[1], "%d.%m.%Y").date().strftime("%d/%m/%Y")
dateTo = datetime.strptime(sys.argv[2], "%d.%m.%Y").date().strftime("%d/%m/%Y")
currency = sys.argv[3]
properCurrencyISOCode = currency == "EUR" or currency == "USD"

if (not properCurrencyISOCode):
    raise BaseException("Thy currency code is unacceptable.")

usableCbrCurrencyCode = ""

if(currency == "EUR"):
    usableCbrCurrencyCode = euroCurrencyCode
elif(currency == "USD"):
    usableCbrCurrencyCode = dollarCurrencyCode
else:
    raise BaseException("How de fuck did you passed through previous check?!")

requestString = "http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=" + dateFrom + "&date_req2=" + dateTo + "&VAL_NM_RQ=" + usableCbrCurrencyCode

unparsedXml = requests.get(requestString).text
xmlTree = etree.ElementTree(etree.fromstring(unparsedXml))
root = xmlTree.getroot()
for child in root:
    info = "Дата: " + child.attrib["Date"] + ", Курс (Руб.): " + str(child[1].text)
    print(info)
