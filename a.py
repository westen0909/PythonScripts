import xml.etree.ElementTree as ET
from xlutils.copy import copy
from xlrd import open_workbook
from xlwt import easyxf
import xlwt, xlrd

tree = ET.parse('country_data.xml')
root = tree.getroot()

rb = open_workbook('example.xls',formatting_info=True)
wb = copy(rb)
ws = wb.get_sheet(0)

table = rb.sheet_by_index(0) #Gets the index order

col = table.ncols
latest_row = table.nrows

for row in table.col(col-1):
	old_value = row.value

	for a, neighbor in enumerate(root.findall("country/neighbor")):
		name = neighbor.get("name")

		if old_value == name:
			ws.write(a, col+1, name)
		else:
			ws.write(latest_row+1, col+1, name)

for a, country in enumerate(root.findall("country")):
	name = country.get("name")
	ws.write(a, col, name)




wb.save('example.xls')


