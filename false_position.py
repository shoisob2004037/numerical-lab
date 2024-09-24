import numpy as np
import sys
import matplotlib.pyplot as plt
from xlwt import Workbook

def f(x):
    return 0.7*x**5 - 8*x**4 + 44*x**3 - 90*x**2 + 82*x - 25

a = float(input("Enter 1st Initial Guess: "))
b = float(input("Enter 2nd Initial Guess: "))

fxa = f(a)
fxb = f(b)

if fxa * fxb > 0:
    print("Sorry, wrong initial guess. The product of f(a) and f(b) must be less than 0. Please try again.")
    sys.exit()
elif fxa * fxb < 0:
    err = float(input("Enter desired percentage relative error: "))
    ite = int(input("Enter number of iterations: "))

    x_a = np.zeros(ite)
    x_b = np.zeros(ite)
    x_c = np.zeros(ite)
    f_a = np.zeros(ite)
    f_b = np.zeros(ite)
    f_c = np.zeros(ite)
    real_err = np.zeros(ite)
    itern = np.zeros(ite)

    x_a[0] = a
    x_b[0] = b
    f_a[0] = fxa
    f_b[0] = fxb

    for i in range(ite):
        itern[i] = i + 1

        f_a[i] = f(x_a[i])
        f_b[i] = f(x_b[i])

        x_c[i] = x_b[i] - (x_a[i] - x_b[i]) * f_b[i] / (f_a[i] - f_b[i])
        f_c[i] = f(x_c[i])

        if i > 0:
            real_err[i] = abs(((x_c[i] - x_c[i-1]) / x_c[i]) * 100)

        if all([i > 0, abs(real_err[i]) < err]):
            break
        elif f_c[i] == 0:
            break

        if i == ite - 1:
            break

        # Modified logic: only consider f(a) and f(c)
        if f_a[i] * f_c[i] < 0:  # If the product is negative, update x_b
            x_b[i+1] = x_c[i]
            x_a[i+1] = x_a[i]
        else:  # If the product is positive, update x_a
            x_a[i+1] = x_c[i]
            x_b[i+1] = x_b[i]

    # Plotting the function and iterations
    x_values = np.linspace(a, b, 500)
    y_values = f(x_values)

    plt.plot(x_values, y_values, label="f(x)", color="blue")
    plt.axhline(0, color='black',linewidth=1) 

    # Plotting the points of a, b, and c at each iteration
    plt.scatter(x_a[:i+1], f_a[:i+1], color="red", label="x_a")
    plt.scatter(x_b[:i+1], f_b[:i+1], color="green", label="x_b")
    plt.scatter(x_c[:i+1], f_c[:i+1], color="orange", label="x_c (root approximation)")

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('False Position Method')
    plt.legend()
    plt.show()

    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    num_of_iter = i

    sheet1.write(0, 3, 'FALSE POSITION METHOD')
    sheet1.write(1, 0, 'Itrtn No')  
    sheet1.write(1, 1, 'x_a')
    sheet1.write(1, 2, 'x_b')
    sheet1.write(1, 3, 'f(a)')
    sheet1.write(1, 4, 'f(b)')
    sheet1.write(1, 5, 'x_c')
    sheet1.write(1, 6, 'f(c)')
    sheet1.write(1, 7, 'Relative error')

    for n in range(num_of_iter + 1):
        sheet1.write(n + 2, 0, itern[n])
        sheet1.write(n + 2, 1, x_a[n])
        sheet1.write(n + 2, 2, x_b[n])
        sheet1.write(n + 2, 3, f_a[n])
        sheet1.write(n + 2, 4, f_b[n])
        sheet1.write(n + 2, 5, x_c[n])
        sheet1.write(n + 2, 6, f_c[n])
        sheet1.write(n + 2, 7, real_err[n])

    sheet1.write(n + 4, 2, 'The')
    sheet1.write(n + 4, 3, 'root')
    sheet1.write(n + 4, 4, 'is')
    sheet1.write(n + 4, 5, x_c[i])

    wb.save('FALSE POSITION.xls')

    print("The root is", x_c[i])
