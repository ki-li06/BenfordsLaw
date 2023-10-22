from Main import get_new_sheet


sheet = get_new_sheet()

def get_column_data(column):
    if type(column) == str:
        encoder = {"ars": 1, "name": 2, "fläche": 3, "bev0": 4, "bev1": 5, "bev2": 6, "bev3": 7, "plz": 8, "koord0": 9, "koord1": 10}
        column_i = encoder[column]
    else:
        column_i = column
    row = 7
    data = []
    NoneElements = 0
    ZeroElements = 0
    while True:
        cell_ars = sheet.cell(row,1)
        cell = sheet.cell(row, column_i)
        if cell_ars.value == None:
            break
        elif cell.value == None:
            #print("at row " + str(row) + " cell " + str(column) + " is None ("  + sheet.cell(row, 2).value + ")")
            NoneElements += 1
            pass
        elif cell.value == 0:
            #print("at row " + str(row) + " cell " + str(column) + " is 0 ("  + sheet.cell(row, 2).value + ")")
            ZeroElements += 1
            pass
        else:
            data.append(cell.value)
        row += 1
        #print("row=" + str(row))
    if NoneElements > 0 or ZeroElements > 0:
        print("column", column,"contains invalid elements --- NoneElements:", NoneElements, " ZeroElements:", ZeroElements)
    return data

list = get_column_data("fläche")
#print("list:", list)
print(len(list), " elements in list")

