import os
from openpyxl import load_workbook

path_txt_to_excel = os.path.dirname(os.path.realpath(__file__)) + "\\filePath.txt"
#this xlsx file is https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugQ/AuszugGV3QAktuell.html, just located somewhere else on my computer
path_excel = str(open(path_txt_to_excel, 'r').read())
print("path_excel:", path_excel, " (type=", type(path_excel), ")")

print("loading workbook...")
wb_obj = load_workbook(path_excel)
print("finished loading workbook")

sheet_orig = wb_obj["Onlineprodukt_Gemeinden30092023"]
sheet_new = wb_obj["GemeindeverzeichnisGekürzt"]


def get_orig_sheet():
    return sheet_orig

def get_new_sheet():
    return sheet_new

def save_workbook():
    wb_obj.save(path_excel)

#print("loaded main.py")