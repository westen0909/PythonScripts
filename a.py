import xml.etree.ElementTree as ET
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import xlwt, xlrd

tree = ET.parse('country_data.xml')
root = tree.getroot()

for country in root.findall("."):
	name = country.get("TotalResults")
	print name


#INIT

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')


for a, country in enumerate(root.findall("country")):
	name = country.get("name")
	ws.write(a, 0, name)
	print name

wb.save('example.xls')


#APPEND

rb = open_workbook('example.xls',formatting_info=True)
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(0, 1, "Sample2")

for a, country in enumerate(root.findall("country")):
	name = country.get("name")
	ws.write(a, 1, name)
	print name

wb.save('example.xls')