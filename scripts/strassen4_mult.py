# import math
# import numpy as np
# from timeit import default_timer as timer
# import standard_mult
# import strassen2_mult
# import strassen_mult
#
#
# def read_matrix(m_lines):
#     newMatrix = []
#     for m_line in m_lines:
#         m_line = m_line.split()
#         int_line = list(map(int, m_line))
#         newMatrix.append(int_line)
#     return np.array(newMatrix).reshape(-1)
#
#
# def matrix_add(matrix_a, matrix_b):
#     return matrix_a + matrix_b
#
#
# def matrix_minus(matrix_a, matrix_b):
#     return matrix_a - matrix_b
#
#
# def matrix_divide(matrix, row_index, col_index, length):
#     matrix = matrix.reshape(length, length)
#     if row_index == 1:
#         matrix = matrix[0:length // 2]
#     else:
#         matrix = matrix[length // 2: length]
#     if col_index == 1:
#         matrix = matrix[:, 0:length // 2]
#     else:
#         matrix = matrix[:, length // 2: length]
#     return matrix.flatten()
#
#
# def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
#     length = int(math.sqrt(len(matrix_11)))
#     matrix_11 = matrix_11.reshape(length, length)
#     matrix_12 = matrix_12.reshape(length, length)
#     matrix_21 = matrix_21.reshape(length, length)
#     matrix_22 = matrix_22.reshape(length, length)
#
#     matrix_left = np.r_[matrix_11, matrix_21]
#     matrix_right = np.r_[matrix_12, matrix_22]
#     return np.c_[matrix_left, matrix_right].reshape(-1)
#
#
# def strassen_stack(matrix_a, matrix_b, length, optimized=False, boundary=6):
#     if optimized and boundary > length:
#         matrix_all = standard_mult.standard(matrix_a, matrix_b, length).reshape(-1)
#     elif length == 1:
#         matrix_all = np.array([matrix_a[0] * matrix_b[0]])
#     else:
#         if length % 2 != 0:
#             matrix_a = matrix_a.reshape(length, length)
#             matrix_b = matrix_b.reshape(length, length)
#             matrix_a = np.r_[matrix_a, np.zeros(length, dtype=int).reshape(1, length)]
#             matrix_a = np.c_[matrix_a, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
#             matrix_b = np.r_[matrix_b, np.zeros(length, dtype=int).reshape(1, length)]
#             matrix_b = np.c_[matrix_b, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
#             length += 1
#         s1 = matrix_minus(matrix_divide(matrix_b, 1, 2, length), matrix_divide(matrix_b, 2, 2, length))
#         # print('s1: \n', s1.reshape(length // 2, length // 2))
#         s2 = matrix_add(matrix_divide(matrix_a, 1, 1, length), matrix_divide(matrix_a, 1, 2, length))
#         # print('s2: \n', s2.reshape(length // 2, length // 2))
#         s3 = matrix_add((matrix_divide(matrix_a, 2, 1, length)), (matrix_divide(matrix_a, 2, 2, length)))
#         # print('s3: \n', s3.reshape(length // 2, length // 2))
#         s4 = matrix_minus(matrix_divide(matrix_b, 2, 1, length), matrix_divide(matrix_b, 1, 1, length))
#         # print('s4: \n', s4.reshape(length // 2, length // 2))
#         s5 = matrix_add(matrix_divide(matrix_a, 1, 1, length), matrix_divide(matrix_a, 2, 2, length))
#         # print('s5: \n', s5.reshape(length // 2, length // 2))
#         s6 = matrix_add(matrix_divide(matrix_b, 1, 1, length), matrix_divide(matrix_b, 2, 2, length))
#         # print('s6: \n', s6.reshape(length // 2, length // 2))
#         s7 = matrix_minus(matrix_divide(matrix_a, 1, 2, length), matrix_divide(matrix_a, 2, 2, length))
#         # print('s7: \n', s7.reshape(length // 2, length // 2))
#         s8 = matrix_add(matrix_divide(matrix_b, 2, 1, length), matrix_divide(matrix_b, 2, 2, length))
#         # print('s8: \n', s8.reshape(length // 2, length // 2))
#         s9 = matrix_minus(matrix_divide(matrix_a, 1, 1, length), matrix_divide(matrix_a, 2, 1, length))
#         # print('s9: \n', s9.reshape(length // 2, length // 2))
#         s10 = matrix_add(matrix_divide(matrix_b, 1, 1, length), matrix_divide(matrix_b, 1, 2, length))
#         # print('s10: \n', s10.reshape(length // 2, length // 2))
#
#
#         p1 = strassen(matrix_divide(matrix_a, 1, 1, length), s1, length // 2, optimized, boundary)
#         p2 = strassen(s2, matrix_divide(matrix_b, 2, 2, length), length // 2, optimized, boundary)
#         p3 = strassen(s3, matrix_divide(matrix_b, 1, 1, length), length // 2, optimized, boundary)
#         p4 = strassen(matrix_divide(matrix_a, 2, 2, length), s4, length // 2, optimized, boundary)
#         p5 = strassen(s5, s6, length // 2, optimized, boundary)
#         p6 = strassen(s7, s8, length // 2, optimized, boundary)
#         p7 = strassen(s9, s10, length // 2, optimized, boundary)
#
#         c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
#         c12 = matrix_add(p1, p2)
#         c21 = matrix_add(p3, p4)
#         c22 = matrix_minus(matrix_add(p5, p1), matrix_add(p3, p7))
#
#         matrix_all = matrix_merge(c11, c12, c21, c22)
#     return matrix_all
#
#
# def strassen_solver(file_1, file_2, optimize, boundary):
#     m1_file = open(file_1, 'r+')
#     m2_file = open(file_2, 'r+')
#
#     matrix_a = read_matrix(m1_file)
#     matrix_b = read_matrix(m2_file)
#     length = int(math.sqrt(len(matrix_a)))
#     # matrixC = np.zeros((length, length))
#
#     # print('>> [INFO] Input matrix A:\n', matrix_a.reshape(length, length))
#     # print('>> [INFO] Input matrix B:\n', matrix_b.reshape(length, length))
#     # print(matrixC)
#     tic = timer()
#     result_matrix = strassen_stack(matrix_a, matrix_b, length, optimize, boundary)
#     toc = timer()
#     result_length = int(math.sqrt(len(result_matrix)))
#     result_matrix = result_matrix.reshape(result_length, result_length)
#     # print('>> [INFO] Output matrix B:\n', result_matrix)  # FIXME: adjust result
#     return toc - tic
