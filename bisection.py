# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 16:19:50 2022
"""

import numpy as np 
from xlwt import Workbook

def f(x):
    return 0.7*x**5 - 8*x**4 + 44*x**3 - 90*x**2 + 82*x - 25

# Taking input for initial values
xl = float(input('Enter 1st initial value: ')) 
xu = float(input('Enter 2nd initial value: '))  

fxl = f(xl)
fxu = f(xu)

if fxl * fxu > 0:
    print('Wrong initial input')
elif fxl * fxu < 0:
    # Taking input for error and number of iterations
    err = float(input('Enter desired percentage relative error: '))
    ite = int(input('Enter number of iterations: '))

    # Initialization
    x_l = np.zeros(ite)
    x_u = np.zeros(ite)
    x_c = np.zeros(ite)
    
    f_xl = np.zeros(ite)
    f_xu = np.zeros(ite)
    f_xc = np.zeros(ite)
    
    rel_err = np.zeros(ite)
    itern = np.zeros(ite)

    # Initial conditions
    x_l[0] = xl
    x_u[0] = xu
    
    f_xl[0] = fxl
    f_xu[0] = fxu 

    # Iterating through the method
    for i in range(ite):
        itern[i] = i + 1
        x_c[i] = (x_l[i] + x_u[i]) / 2 
        f_xl[i] = f(x_l[i])
        f_xu[i] = f(x_u[i])
        f_xc[i] = f(x_c[i])

        # Calculating relative error    
        if i > 0:
            rel_err[i] = ((x_c[i] - x_c[i-1]) / x_c[i]) * 100
        
        if i > 0 and abs(rel_err[i]) < err:
            break 
        elif f_xc[i] == 0:
            break
   
        # Update x_u or x_l based on your logic
        if f_xc[i] * f_xl[i] < 0:  # If the product is negative, update x_u
            x_u[i+1] = x_c[i]
            x_l[i+1] = x_l[i]
        elif f_xc[i] * f_xl[i] > 0:  # If the product is positive, update x_l
            x_l[i+1] = x_c[i]
            x_u[i+1] = x_u[i]
   
    # Saving results to Excel file
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    num_of_iter = i
    
    sheet1.write(0, 3, 'Bisection Method')
    sheet1.write(1, 0, 'Number of iteration')
    sheet1.write(1, 1, 'x_l')
    sheet1.write(1, 2, 'x_u')
    sheet1.write(1, 3, 'f(x_l)')
    sheet1.write(1, 4, 'f(x_u)')
    sheet1.write(1, 5, 'x_c')
    sheet1.write(1, 6, 'f(x_c)')
    sheet1.write(1, 7, 'Relative error')

    for n in range(num_of_iter + 1):
        sheet1.write(n + 2, 0, itern[n])
        sheet1.write(n + 2, 1, x_l[n])
        sheet1.write(n + 2, 2, x_u[n])
        sheet1.write(n + 2, 3, f_xl[n])
        sheet1.write(n + 2, 4, f_xu[n])
        sheet1.write(n + 2, 5, x_c[n])
        sheet1.write(n + 2, 6, f_xc[n])
        sheet1.write(n + 2, 7, rel_err[n])
    
    sheet1.write(n + 4, 2, 'The')
    sheet1.write(n + 4, 3, 'root')
    sheet1.write(n + 4, 4, 'is')
    sheet1.write(n + 4, 5, x_c[i])
    wb.save('bisection.xls')
