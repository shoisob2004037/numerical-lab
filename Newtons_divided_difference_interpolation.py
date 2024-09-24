import numpy as np
import xlrd
from matplotlib import pyplot as plt

#taking necessary input values from keyboard
X=float(input('Enter the interpolating point: ' ))

#Reading data from excel file
loc = (r'E:\Study Material\Code\Numerical_Lab\data_interpolation.xls')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

n=sheet.ncols-1    #number of data points
#initialize variables
x=np.zeros([n])
y=np.zeros([n])
F=np.zeros([n-1,n])

#creating vectors from the data 
for i in range(1,sheet.ncols):
    #print(sheet.cell_value(1, i))
    x[i-1]=sheet.cell_value(0, i)
    y[i-1]=sheet.cell_value(1, i)

#Computing divided difference
y1=y    
for j in range(1,n):
    for i in range(j+1,n+1):
        F[j-1,i-1]=(y1[i-1]-y1[i-2])/(x[i-1]-x[i-1-j])
    y1=F[j-1,:]

#initialize variables    
Y=0
summation=0
b=np.zeros([n])
b[0]=1

#Computing the function value at the interpolating point
for j in range(n):
    if j==0:
        summation=y1[j]
    
    if j>0:
        a=F[j-1,j]
        for i in range(j):
            b[i+1]=(X-x[i])*b[i]
            
        summation=a*b[i+1]
    
    Y=summation+Y
    
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