import math
from timeit import default_timer as timer
import strassen_mut
import numpy as np


def read_matrix(m_lines):
    newMatrix = []
    for m_line in m_lines:
        m_line = m_line.split()
        int_line = list(map(int, m_line))
        newMatrix.append(int_line)
    return np.array(newMatrix).reshape(-1)


def adapted(matrix_a, matrix_b, length, boundary):
    return strassen_mut.strassen(matrix_a, matrix_b, length, adapted=True, boundary=boundary)


def adapted_solver(file_1, file_2, boundary):
    m1_file = open(file_1, 'r+')
    m2_file = open(file_2, 'r+')

    matrix_a = read_matrix(m1_file)
    matrix_b = read_matrix(m2_file)
    length = int(math.sqrt(len(matrix_a)))
    # matrixC = np.zeros((length, length))

    # print('>> [INFO] Input matrix A:\n', matrix_a.reshape(length, length))
    # print('>> [INFO] Input matrix B:\n', matrix_b.reshape(length, length))
    # print(matrixC)
    tic = timer()
    result_matrix = adapted(matrix_a, matrix_b, length, boundary)
    toc = timer()
    result_length = int(math.sqrt(len(result_matrix)))
    result_matrix = result_matrix.reshape(result_length, result_length)
    # print('>> [INFO] Output matrix B:\n', result_matrix)  # FIXME: adjust result
    return toc - tic
