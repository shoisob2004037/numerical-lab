import math
import numpy as np
from xlwt import Workbook

x = float(input("Enter an initial value: "))
err = float(input("Enter desired percentage relative error: "))
ite = int(input("Enter number of iterations: "))

# Define the new function f(x)
def f(x):
    return 0.7*x**5 - 8*x**4 + 44*x**3 - 90*x**2 + 82*x - 25

# Define the derivative of the new function df(x)
def df(x):
    return 3.5*x**4 - 32*x**3 + 132*x**2 - 180*x + 82


# Arrays for storing iteration results
new_x = np.zeros([ite])
ite_list = np.zeros([ite])
rel_err = np.zeros([ite])
f_x = np.zeros([ite])
df_x = np.zeros([ite])

# Initial values
new_x[0] = x
f_x[0] = f(x)
df_x[0] = df(x)

for i in range(ite):
    ite_list[i] = i + 1
    
    new_x[i+1] = new_x[i] - (f(new_x[i]) / df(new_x[i]))
    f_x[i] = f(new_x[i])
    df_x[i] = df(new_x[i])
    
    if i > 0:
        rel_err[i] = ((new_x[i] - new_x[i-1]) / new_x[i]) * 100
        
    if i > 0 and abs(rel_err[i]) < err:
        break
    if i == ite - 1:
        break
    
# Writing results to an Excel sheet
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
num_of_iter = i

sheet1.write(0, 2, 'Newton Raphson Method')
sheet1.write(1, 0, 'Iteration No')
sheet1.write(1, 1, 'x_n')
sheet1.write(1, 2, 'f(x)')
sheet1.write(1, 3, 'df(x)')
sheet1.write(1, 4, 'x_new')
sheet1.write(1, 5, 'rel_err')

for n in range(num_of_iter + 1):
    sheet1.write(n + 2, 0, ite_list[n])
    sheet1.write(n + 2, 1, new_x[n])
    sheet1.write(n + 2, 2, f_x[n])
    sheet1.write(n + 2, 3, df_x[n])
    sheet1.write(n + 2, 4, new_x[n + 1])
    sheet1.write(n + 2, 5, rel_err[n])

sheet1.write(n + 6, 1, 'The')
sheet1.write(n + 6, 2, 'root')
sheet1.write(n + 6, 3, 'is')
sheet1.write(n + 6, 4, new_x[n])

wb.save('NEWTON_RAPHSON.xls')

print("The root is =", new_x[n])
