import os


path_txt_to_excel = os.path.dirname(os.path.realpath(__file__)) + "\\filePath.txt"
path_excel = str(open(path_txt_to_excel, 'r').read())
print("path_excel:", path_excel, " (type=", type(path_excel), ")")
