import os
import pandas as pd
from openpyxl import load_workbook
import time

path_txt_to_excel = os.path.dirname(os.path.realpath(__file__)) + "\\filePath.txt"
#this xlsx file is https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugQ/AuszugGV3QAktuell.html, just located somewhere else on my computer
path_excel = str(open(path_txt_to_excel, 'r').read())
print("path_excel:", path_excel, " (type=", type(path_excel), ")")

# To open the workbook 
# workbook object is created
wb_obj = load_workbook(path_excel)
 
# Get workbook active sheet object
# from the active attribute
sheet_obj = wb_obj.worksheets[1]
 
# Cell objects also have a row, column, 
# and coordinate attributes that provide
# location information for the cell.
 
# Note: The first row or 
# column integer is 1, not 0.
 

row = 7
cell_obj_satzart = sheet_obj.cell(row = row, column = 1)
elements = 0

while cell_obj_satzart.value != None:
    cell_obj_gem = sheet_obj.cell(row = row, column = 7)
    if cell_obj_gem.value != None:
        cell_obj_name = sheet_obj.cell(row = row, column = 8)
        print("row=" +  str(row) + " => " + cell_obj_name.value) 
        elements = elements + 1
    #time.sleep(0.0001)  # add a 20 millisecond delay
    row = row + 1
    cell_obj_satzart = sheet_obj.cell(row = row, column = 1)

print("elements:", elements)