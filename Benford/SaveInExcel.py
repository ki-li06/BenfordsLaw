from openpyxl import Workbook
from AnalysisBenfordsLaw import prob_d_i as prob_d_i

wb = Workbook()

# grab the active worksheet
ws = wb.active

for d in range(0, 10):
    for i in range(1, 5):
        ws.cell(row=i+1, column= d+1+1).value = prob_d_i(d, i)*100

# Save the file
wb.save("0_Excels\Prob(D_i=d).xlsx")

print("test_Openpyxl.py loaded successfully!")
