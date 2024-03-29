import numpy as np
import math
from timeit import default_timer as timer

"""
@ Filename: standard_mult.py
    This file contains method that use standard matrix multiplication, O(n^3) time complication
@ Methods: 
    read_matrix(m_lines)
    standard(matrix_a, matrix_b, length)
    standard_solver(file_1, file_2)
"""

"""
@ Function: read_matrix
    used to read from the file passed in this method, turn the lines input into a list first, 
    than convert it into a numpy one dimension array for the use of later multiplication
@ Parameter: m_lines
    a type of file input stream for python
"""


def read_matrix(m_lines):
    newMatrix = []
    for m_line in m_lines:
        m_line = m_line.split()
        int_line = list(map(int, m_line))
        newMatrix.append(int_line)
    return np.array(newMatrix).reshape(-1)


"""
@ Function: standard(matrix_a, matrix_b, length)
    multiply the two input matrices and return the results, NOTED that I use numpy matrix multiplication 
    to compute, because the numpy module has already do optimization in itself, and then I reshape the results back 
    into the one dimension array
@ Parameters: matrix_a, matrix_b
@ Parameter: length
@ Pseudo code:

SQUARE-MATRIX-MULTIPLY (A, B)
    n = A.rows
    let C be a new n×n matrix
    for i = 1 to n 
        for j = 1 to n 
            for k =1 to n 
                cij = cij + aik×bkj
    return C
"""


def standard(matrix_a, matrix_b, length):
    matrix_a = matrix_a.reshape(length, length)
    matrix_b = matrix_b.reshape(length, length)
    matrix_c = np.zeros([1, length * length], dtype=int).reshape(length, length)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                matrix_c[i, j] += matrix_a[i, k] * matrix_b[k, j]
    return matrix_c.reshape(-1)


"""
@ Function: standard_solver(file_1, file_2)
    the solver method for the standard matrix multiplication
@ Parameters: file_1, file_2
    the test files that read in
"""


def standard_solver(file_1, file_2):
    m1_file = open(file_1, 'r+')
    m2_file = open(file_2, 'r+')
    matrix_a = read_matrix(m1_file)
    matrix_b = read_matrix(m2_file)
    length = int(math.sqrt(len(matrix_a)))
    # print('>> [INFO] Input matrix A:\n', matrix_a.reshape(length, length))
    # print('>> [INFO] Input matrix B:\n', matrix_b.reshape(length, length))
    tic = timer()
    result_matrix = standard(matrix_a, matrix_b, length)
    toc = timer()
    # print('>> [INFO] Output matrix B:\n', result_matrix.reshape(length, length))

    return toc - tic
