import numpy as np
import xlrd
from matplotlib import pyplot as plt

#taking necessary input values from keyboard
X=float(input('Enter the interpolating point: ' ))

#Reading data from excel file
loc = (r'E:\Study Material\Code\Numerical_Lab\data_interpolation.xls')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

n=sheet.ncols-1    
#initialize variables
x=np.zeros([n])
y=np.zeros([n])
Y=0

#creating vectors from the data 
for i in range(1,sheet.ncols):
    #print(sheet.cell_value(1, i))
    x[i-1]=sheet.cell_value(0, i)
    y[i-1]=sheet.cell_value(1, i)

#Performing Lagrange interpolation    
for i in range(n):
    a=1
    b=1
    for j in range(n):
        if j>i: 
            a=a*(X-x[j])
            b=b*(x[i]-x[j])
        
        if j<i:
            a=a*(X-x[j])
            b=b*(x[i]-x[j])
        
    
    Y=Y+(a/b)*y[i]
    
print('The interpolating result at x = '+str(Y))
#print(Y)


plt.figure(1)
plt.plot(x,y) 
plt.plot(X,Y,'o')
plt.xlabel('Values of x')
plt.ylabel('Values of y')
plt.title('Graphical verification of the interpolation result')
plt.legend(['Measured','Estimated / Interpolated'], loc='best')
plt.show()
