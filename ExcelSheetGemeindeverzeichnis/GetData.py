
from Main import get_new_sheet


sheet = get_new_sheet()

def get_column_data(column):
    row = 7
    data = []
    while True:
        cell_ars = sheet.cell(row,1)
        cell = sheet.cell(row, column)
        if cell_ars.value == None:
            break
        else:
            data.append(cell.value)
        row += 1
        print("row=" + str(row))
    return data

list = get_column_data(3)
print("length of list:", len(list))
print("list:", list)
