import math
from timeit import default_timer as timer
import strassen_mult
import numpy as np

"""
@ Filename: strassen2_mult.py
    This file contains method that use lower bound optimization for matrix multiplication, 
    add a boundary for the strassen method, under it using standard method
@ Methods: 
    read_matrix(m_lines)
    strassen2(matrix_a, matrix_b, length, boundary)
    strassen2_solver(file_1, file_2, boundary)
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
@ Function: strassen2(matrix_a, matrix_b, length, boundary)
    directly use the strassen(matrix_a, matrix_b, length, optimized=False, boundary=32), 
    and reset 'optimized' to be true, and set a new boundary
@ Parameters: matrix_a, matrix_b
@ Parameter: length
@ Parameter: boundary
    the boundary of standard method and strassen method
"""


def strassen2(matrix_a, matrix_b, length, boundary):
    return strassen_mult.strassen(matrix_a, matrix_b, length, optimized=True, boundary=boundary)


"""
@ Function: strassen2_solver(file_1, file_2, boundary)
    the solver method for the lower bound optimization matrix multiplication
@ Parameters: file_1, file_2
    the test files that read in
"""


def strassen2_solver(file_1, file_2, boundary):
    m1_file = open(file_1, 'r+')
    m2_file = open(file_2, 'r+')

    matrix_a = read_matrix(m1_file)
    matrix_b = read_matrix(m2_file)
    length = int(math.sqrt(len(matrix_a)))

    tic = timer()
    result_matrix = strassen2(matrix_a, matrix_b, length, boundary)
    toc = timer()
    result_length = int(math.sqrt(len(result_matrix)))
    result_matrix = result_matrix.reshape(result_length, result_length)
    return toc - tic
