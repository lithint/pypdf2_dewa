import PyPDF2
pdObj = open('document.pdf','rb')
pdfR = PyPDF2.PdfFileReader(pdObj)
total_pages = pdfR.numPages
print("Total Number of Pages",total_pages)

#Electricity Reading
pageObj1 = pdfR.getPage(1)
text_data = pageObj1.extractText()
print("Electricity:",text_data)


data_list = text_data.split(':')
acc_inv_number = data_list[0]
print("Accnum_Invnum",acc_inv_number)
import re
k = re.findall(r'\d+', acc_inv_number)
account_number,invoice_number = k[0],k[1]
print("Account Number",account_number)
print("Invoice Number",invoice_number)

dates = data_list[1]
issue_date = re.search(r'(\d+/\d+/\d+)',dates).group(1)
print("Issue Date",issue_date)
month = data_list[2].replace("Month","")


d = data_list[4]

period = re.match(r'(\d+\/\d+\/\d+)\s*to\s*(\d+\/\d+\/\d+)',d)
from_period = period.group(1)
to_period = period.group(2)[:10]
print("From Period",from_period)
print("To Period",to_period)

electricity = re.search('Electricity(.*)Kilowatt',text_data)
print("Electricity:",electricity.group(1))

meter_number = re.search('Meter number:(.*)Current reading',text_data)
print("Meter Number:",meter_number.group(1))

current_reading = re.search('Current reading:(.*)Pre',text_data)
print("Current Reading:",current_reading.group(1))

prev_reading = re.search('Previous reading:(.*)CarbonFootprint',text_data)
print("Previous Reading:",prev_reading.group(1))

electricity_total = re.search("Electricity total(.*)VATAED",text_data)
print("Electricity Total:",electricity_total.group(1))

#Water Reading
pageObj1 = pdfR.getPage(2)
text_data = pageObj1.extractText()
print("Water:",text_data)

water = re.search('ComeWater(.*)Imperial Gallons',text_data)
print("Water:",water.group(1))

water_meter_number = re.search('Meter number:(.*)Multiplication factor',text_data)
print("Meter Number:",water_meter_number.group(1))

current_reading = re.search('Current reading:(.*)Previous reading:',text_data)
print("Current Reading:",current_reading.group(1))

prev_reading = re.search('Previous reading:(.*)(Current reading - Previous reading )',text_data)
print("Previous Reading:",prev_reading.group(1))

electricity_total = re.search("Water total(.*)VATAED",text_data)
print("Water Total:",electricity_total.group(1))
