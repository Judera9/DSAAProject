import numpy as np
import math
from timeit import default_timer as timer


def read_matrix(m_lines):
    newMatrix = []
    for m_line in m_lines:
        m_line = m_line.split()
        int_line = list(map(int, m_line))
        newMatrix.append(int_line)
    return np.array(newMatrix).reshape(-1)


def standard(matrix_a, matrix_b, length):
    matrix_a = matrix_a.reshape(length, length)
    matrix_b = matrix_b.reshape(length, length)
    matrix_c = np.zeros([1, length * length], dtype=int).reshape(length, length)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                matrix_c[i, j] += matrix_a[i, k] * matrix_b[k, j]
    return matrix_c


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
    # print('>> [INFO] Output matrix B:\n', result_matrix)

    return toc - tic
