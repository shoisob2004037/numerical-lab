import numpy as np
import pandas as pd

filename = "LU decomp.xlsx"  
sheet_name = 0  

def read_excel_matrix(filename, sheet_name):

        df = pd.read_excel(filename, sheet_name=sheet_name,header=None)
        return df.to_numpy()

A = read_excel_matrix(filename, sheet_name)
if A is not None:
    b = read_excel_matrix(filename, sheet_name + 1)
    if b is not None and b.shape[0] == A.shape[0]:
        n = len(A)
        print("Rank of Matrix:") 
        print(n)
        print("Matrix A: ")
        print(A)
        print("Matrix B: ")
        print(b)
        U=A
        L=np.zeros((n, n))
        
        for i in range(n):
            L[i][i]=1
  
            for j in range(i + 1, n):
              factor = U[j][i] / U[i][i]
              for k in range(i , n):
                if k<j and k==i:
                    L[j][k]=U[j][k]/U[k][k]
                U[j][k] -= factor * U[i][k]
           

        d=np.zeros(n)
        Lb = np.concatenate((L, b.reshape(n, 1)), axis=1)
        print("\nLb: ")
        print(Lb);
        for i in range(n):
            sum_terms=0
            for j in range(n):
                sum_terms += d[j] * Lb[i][j]
            d[i] = Lb[i][n] - sum_terms
            
        print("\n\nD: ")
        print(d);
        
        ud = np.concatenate((U, d.reshape(n, 1)), axis=1)
        print("Matrix UD: ")
        print(ud)
        
        soln = np.zeros(n)
        for i in range(n - 1, -1, -1):
          sum_terms = 0
          for j in range(i , n):
              sum_terms += soln[j] * ud[i][j]
          soln[i] = (ud[i][n] - sum_terms) / U[i][i]
        if soln is not None:
            print("\n\nsolution vector A:")
            print(soln)

        else:
            print("Error: Invalid matrix or vector dimensions from Excel file.")
