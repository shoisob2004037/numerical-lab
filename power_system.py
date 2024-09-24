# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:32:30 2024

@author: shoisob
"""

import numpy as np

# Function to get matrix input from the user
def get_matrix_input(size_matrix):
    y = np.zeros((size_matrix, size_matrix), dtype=complex)
    print("Enter the elements of the admittance matrix:")
    for i in range(size_matrix):
        for j in range(size_matrix):
            y[i, j] = complex(input(f'Enter the value of y({i+1},{j+1}): '))
    return y

# Main function
def main():
    size_matrix = int(input("Enter the size of the admittance matrix: "))
    y = get_matrix_input(size_matrix)
    
    print("Original Matrix:")
    print(y)
    
    m = int(input("How many nodes do you want to eliminate: "))
    
    if 1 <= m <= size_matrix:
        for k in range(m):
            a1, b1 = y.shape
            z = np.zeros((a1-1, b1-1), dtype=complex)
            for a in range(a1-1):
                for b in range(b1-1):
                    z[a, b] = y[a, b] - ((y[a, size_matrix-1] * y[size_matrix-1, b]) / y[size_matrix-1, size_matrix-1])
            print('Matrix after eliminating node:')
            print(z)
            y = z
            size_matrix -= 1
    else:
        print('Invalid input: Number of nodes to eliminate must be between 1 and the size of the matrix.')

# Run the main function
if __name__ == "__main__":
    main()
