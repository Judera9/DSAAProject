import math
import numpy as np
from timeit import default_timer as timer
import standard_mult

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
@ Function: matrix_add(matrix_a, matrix_b)
    add two matrix using method build in numpy
@ Parameters: matrix_a, matrix_b
"""


def matrix_add(matrix_a, matrix_b):
    return matrix_a + matrix_b


"""
@ Function: matrix_minus(matrix_a, matrix_b)
    minus two matrix using method build in numpy
@ Parameters: matrix_a, matrix_b
"""


def matrix_minus(matrix_a, matrix_b):
    return matrix_a - matrix_b


"""
@ Function: matrix_divide(matrix, row_index, col_index, length)
    divided the matrix input into four parts(return the part needed), the return variable has 
    already be flattened into a one dimensional array
        M11 | M12
        M21 | M22 -> M_row_index_col_index
@ Parameter: matrix
    the matrix needed to be divided
@ Parameters: row_index, col_index
    the index of the part needed to be divided, as explained above
"""


def matrix_divide(matrix, row_index, col_index, length):
    matrix = matrix.reshape(length, length)
    if row_index == 1:
        matrix = matrix[0:length // 2]
    else:
        matrix = matrix[length // 2: length]
    if col_index == 1:
        matrix = matrix[:, 0:length // 2]
    else:
        matrix = matrix[:, length // 2: length]
    return matrix.flatten()


"""
@ Function: matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22)
    merge the four sub matrix back into a matrix
@ Parameters: matrix_11, matrix_12, matrix_21, matrix_22
    the four sub matrices needed to be merged
"""


def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
    length = int(math.sqrt(len(matrix_11)))
    matrix_11 = matrix_11.reshape(length, length)
    matrix_12 = matrix_12.reshape(length, length)
    matrix_21 = matrix_21.reshape(length, length)
    matrix_22 = matrix_22.reshape(length, length)

    matrix_left = np.r_[matrix_11, matrix_21]
    matrix_right = np.r_[matrix_12, matrix_22]
    return np.c_[matrix_left, matrix_right].reshape(-1)


"""
@ Function: matrix_a, matrix_b, length, optimized=False, boundary=6
    multiply the two input matrices and return the results, NOTED that I use numpy matrix multiplication 
    to compute, because the numpy module has already do optimization in itself, and then I reshape the results back 
    into the one dimension array
@ Parameters: matrix_a, matrix_b
@ Parameter: length
@ Parameter: optimized
    Default to set as false. If the optimized is true, then this strassen method would use the lower boundary 
    method the optimize the raw strassen method.
@ Parameter: boundary
    This boundary is for the lower boundary method(if the 'optimized' is set to be true). Default as 32, 
    because 32 is tested to possibly be the best optimized boundary for lower boundary method
@ Pseudo code:

Suppose that A,B has n rows, and n satisfy that 2^m - c = n, and 2^m>n>2^(m-1), 
Then we construct matrix A' ,B', which A', B' has 2^m rows, A' = [A 0] , B' = [B 0]

create 10 matrix which is defined by 
S1=B'12−B'22 
S2=A'11+A'12
S3=A'21+A'22
S4=B'21−B'11 
S5=A'11+A'22
S6=B'11+B'22
S7=A'12−A'22
S8=B'21+B'22 
S9=A'11−A'21 
S10=B'11+B'12

Strassen(A',B')
n = A'.rows

P1 Strassen(A'11,B'12 − B'22) 
P2 Strassen(A'11 + A'12,B'22) 
P3 Strassen(A'21 + A'22,B'11) 
P4 Strassen(A'22,B'21 − B'11) 
P5 Strassen(A'11 + A'22,B'11 + B'22) 
P6 Strassen(A'12 − A'22,B'21 + B'22) 
P7 Strassen(A'11 − A'21,B'11 + B'12) 

let C' be a new (2^m)*(2^m) matrix
if m==1
    c11=a11*b11
else partition A, B and C as above
C'11= P5 + P4 − P2 + P6 
C'12= P1 + P2 
C'21= P3 + P4 
C'22= P1 + P5 − P3 − P7 
for i = 1 to n 
    for j = 1 to n 
        cij = c'ij
return C 
"""


def strassen(matrix_a, matrix_b, length, optimized=False, boundary=32):

    # if this is an strassen2(lower bound optimization), here is the boundary judge
    if optimized and boundary > length:
        matrix_all = standard_mult.standard(matrix_a, matrix_b, length)  # using standard method
    elif length == 1:  # if length is 1, stop recursion and start to merge from the smallest sub matrix
        matrix_all = np.array([matrix_a[0] * matrix_b[0]])
    else:
        if length % 2 != 0:
            matrix_a = matrix_a.reshape(length, length)
            matrix_b = matrix_b.reshape(length, length)
            matrix_a = np.r_[matrix_a, np.zeros(length, dtype=int).reshape(1, length)]
            matrix_a = np.c_[matrix_a, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
            matrix_b = np.r_[matrix_b, np.zeros(length, dtype=int).reshape(1, length)]
            matrix_b = np.c_[matrix_b, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
            length += 1
        s1 = matrix_minus(matrix_divide(matrix_b, 1, 2, length), matrix_divide(matrix_b, 2, 2, length))
        # print('s1: \n', s1.reshape(length // 2, length // 2))
        s2 = matrix_add(matrix_divide(matrix_a, 1, 1, length), matrix_divide(matrix_a, 1, 2, length))
        # print('s2: \n', s2.reshape(length // 2, length // 2))
        s3 = matrix_add((matrix_divide(matrix_a, 2, 1, length)), (matrix_divide(matrix_a, 2, 2, length)))
        # print('s3: \n', s3.reshape(length // 2, length // 2))
        s4 = matrix_minus(matrix_divide(matrix_b, 2, 1, length), matrix_divide(matrix_b, 1, 1, length))
        # print('s4: \n', s4.reshape(length // 2, length // 2))
        s5 = matrix_add(matrix_divide(matrix_a, 1, 1, length), matrix_divide(matrix_a, 2, 2, length))
        # print('s5: \n', s5.reshape(length // 2, length // 2))
        s6 = matrix_add(matrix_divide(matrix_b, 1, 1, length), matrix_divide(matrix_b, 2, 2, length))
        # print('s6: \n', s6.reshape(length // 2, length // 2))
        s7 = matrix_minus(matrix_divide(matrix_a, 1, 2, length), matrix_divide(matrix_a, 2, 2, length))
        # print('s7: \n', s7.reshape(length // 2, length // 2))
        s8 = matrix_add(matrix_divide(matrix_b, 2, 1, length), matrix_divide(matrix_b, 2, 2, length))
        # print('s8: \n', s8.reshape(length // 2, length // 2))
        s9 = matrix_minus(matrix_divide(matrix_a, 1, 1, length), matrix_divide(matrix_a, 2, 1, length))
        # print('s9: \n', s9.reshape(length // 2, length // 2))
        s10 = matrix_add(matrix_divide(matrix_b, 1, 1, length), matrix_divide(matrix_b, 1, 2, length))
        # print('s10: \n', s10.reshape(length // 2, length // 2))

        p1 = strassen(matrix_divide(matrix_a, 1, 1, length), s1, length // 2, optimized, boundary)
        p2 = strassen(s2, matrix_divide(matrix_b, 2, 2, length), length // 2, optimized, boundary)
        p3 = strassen(s3, matrix_divide(matrix_b, 1, 1, length), length // 2, optimized, boundary)
        p4 = strassen(matrix_divide(matrix_a, 2, 2, length), s4, length // 2, optimized, boundary)
        p5 = strassen(s5, s6, length // 2, optimized, boundary)
        p6 = strassen(s7, s8, length // 2, optimized, boundary)
        p7 = strassen(s9, s10, length // 2, optimized, boundary)

        c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
        c12 = matrix_add(p1, p2)
        c21 = matrix_add(p3, p4)
        c22 = matrix_minus(matrix_add(p5, p1), matrix_add(p3, p7))

        matrix_all = matrix_merge(c11, c12, c21, c22)
    return matrix_all


"""
@ Function: strassen_solver(file_1, file_2)
    the solver method for the strassen matrix multiplication(not containing the lower boundary optimization)
@ Parameters: file_1, file_2
    the test files that read in 
"""


def strassen_solver(file_1, file_2):
    m1_file = open(file_1, 'r+')
    m2_file = open(file_2, 'r+')

    matrix_a = read_matrix(m1_file)
    matrix_b = read_matrix(m2_file)
    length = int(math.sqrt(len(matrix_a)))

    # print('>> [INFO] Input matrix A:\n', matrix_a.reshape(length, length))
    # print('>> [INFO] Input matrix B:\n', matrix_b.reshape(length, length))
    tic = timer()
    result_matrix = strassen(matrix_a, matrix_b, length)
    toc = timer()
    result_length = int(math.sqrt(len(result_matrix)))
    result_matrix = result_matrix.reshape(result_length, result_length)
    # print('>> [INFO] Output matrix B:\n', result_matrix)
    return toc - tic
