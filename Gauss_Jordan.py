import numpy as np
import xlrd


no = int(input('Enter number of unknowns: '))

a = np.zeros((no,no+1))

x = np.zeros(no);
loc = (r'E:\Study Material\Code\Numerical_Lab\GaussData.xls')
             
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(sheet.ncols):
    for j in range(sheet.nrows):
        a[j,i]=sheet.cell_value(j, i)


for i in range(no):        
    for j in range(no):
        if i != j:
            r = a[j][i]/a[i][i]

            for k in range(no+1):
                a[j][k] = a[j][k] - r * a[i][k]
for i in range(no):
    x[i] = a[i][no]/a[i][i]

print('\nRequired solution is: ')
for i in range(no):
    print('\tX%d = %0.2f' %(i+1,x[i]))