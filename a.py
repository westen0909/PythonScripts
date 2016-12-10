import xml.etree.ElementTree as ET
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import xlwt, xlrd

tree = ET.parse('country_data.xml')
root = tree.getroot()

#Get Attribute Value
# for country in root.findall("."):
# 	name = country.get("TotalResults")
# 	print name

# LINK TO PATH
# path = 'C:\Users\Joshua\Desktop\LocalScripts'
# ws.write(0, col+3, xlwt.Formula('HYPERLINK("%s";"Link")' % path))

# INIT
# wb = xlwt.Workbook()
# ws = wb.add_sheet('A Test Sheet')

# for a, fetch in enumerate(root.findall("set/test")):
# 	name = fetch.get("name")
# 	ws.write(a, 0, name)

# for a, fetch in enumerate(root.findall("set/test2")):
# 	status = fetch.get("status")
# 	ws.write(a, 1, status)

# wb.save('example.xls')

#APPEND
# rb = open_workbook('example.xls',formatting_info=True)
# wb = copy(rb)
# ws = wb.get_sheet(0)
# table = rb.sheet_by_index(0) #Gets the index order
# col = table.ncols
# latest_row = table.nrows

# for a, fetch in enumerate(root.findall("set/test")):
# 	name = fetch.get("name")
# 	ws.write(a, col, name)

# for a, fetch in enumerate(root.findall("set/test2")):
# 	status = fetch.get("status")
# 	ws.write(a, col+1, status)

# wb.save('example.xls')