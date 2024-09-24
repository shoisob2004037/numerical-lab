# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 23:42:53 2022


"""
import numpy as np
import xlrd


no = 3;

a = np.zeros((no,no+1)) 
print(a)
x = np.zeros(no)
print(x)
location = (r'E:\Study Material\Code\Numerical_Lab\GaussData.xls')

wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)

for i in range(sheet.ncols):
    for j in range(sheet.nrows):
        a[j,i]=sheet.cell_value(j, i)

print(a)

for i in range(no):     
    for j in range(i+1,no):
        r = (a[j][i]/a[i][i])
        for k in range(no+1):
            a[j][k] = a[j][k] - r * a [i][k]

x[no-1] = a[no-1][no]/a[no-1][no-1]
   

for i in range(no-2,-1,-1):
    x[i] = a[i][no]
    
    for j in range(i+1,no):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

print('\nRequired solution is: ')
for i in range(no):
    print('\tX%d = %0.2f' %(i+1,x[i]))