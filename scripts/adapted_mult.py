import math
import numpy as np
from timeit import default_timer as timer
import strassen2_mult
import strassen_mult
import assemble_test
import standard_mult
import plotGraph
import multiprocessing
import os

"""
NOTED: 
    I need to have an '__name__ == "__main__"' method here, and copy some codes from the assemble_test.py
file. This is because for python, using the multi-processing method requires to put the progress of creating 
new sub-processes in the main process(for process safety). As a result, I could not use assemble test to run 
and plot answers like other multiply algorithms.

@ Filename: adapted_mult.py
    This file is used to find the threshold and the write it into the .yaml configuration file, 
    which is under the config/ package. What's more, the graph of cross point and the adapted 
    algorithm runtime are also plotted by matplotlib.
@ Methods:
    read_matrix((m_lines)  # read matrix from file input stream, into a one dimension array
    
    # this one and the following is to creat eight different computation methods for the eight sub-processes
    fun_sub1_1(matrix_a11, matrix_b11, length, matrix_11_1)
    fun_sub1_2(matrix_a12, matrix_b21, length, matrix_11_2)
    ...
    fun_sub4_1(matrix_a21, matrix_b12, length, matrix_22_1)
    
    set_threshold(data_N, optimized, standard)
    adapted_mult(test_file, length, threshold_val)
    __name__ == "__main__"
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
@ Function: fun_sub1_1(matrix_a11, matrix_b11, length, matrix_11_1)
    this one and the following is to creat eight different computation methods for the eight sub-processes,
    why using eight different methods is because I am afraid that using the same methods would cause some 
    errors for process safety.
@ Parameters: matrix_a11, matrix_b11
    the sub matrices that need to use strassen2(the lower bound method) to optimize, length of the sub matices 
    is half the parent matrix
@ Parameters: length
    the size of the parent matrix
@ Parameters；matrix_11_1
    the answer of the multiplication of the sub-matrix, NOTED that this variable is shared with the parent process,
    which just like declared in the parent process: 'matrix_11_1 = multiprocessing.Manager().list()'. 
    In fact, generally the variable declared in different processes could not be shared.

PS: the comments in these functions is used to test the results of sub computation
"""


def fun_sub1_1(matrix_a11, matrix_b11, length, matrix_11_1):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_11_1.append(strassen2_mult.strassen2(matrix_a11, matrix_b11, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 1_1: finish in time:', toc - tic)


def fun_sub1_2(matrix_a12, matrix_b21, length, matrix_11_2):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_11_2.append(strassen2_mult.strassen2(matrix_a12, matrix_b21, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 1_2: finish in time:', toc - tic)


def fun_sub2_1(matrix_a11, matrix_b12, length, matrix_12_1):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_12_1.append(strassen2_mult.strassen2(matrix_a11, matrix_b12, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 2_1: finish in time:', toc - tic)


def fun_sub2_2(matrix_a12, matrix_b22, length, matrix_12_2):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_12_2.append(strassen2_mult.strassen2(matrix_a12, matrix_b22, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 2_2: finish in time:', toc - tic)


def fun_sub3_1(matrix_a21, matrix_b11, length, matrix_21_1):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_21_1.append(strassen2_mult.strassen2(matrix_a21, matrix_b11, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 3_1: finish in time:', toc - tic)


def fun_sub3_2(matrix_a22, matrix_b21, length, matrix_21_2):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_21_2.append(strassen2_mult.strassen2(matrix_a22, matrix_b21, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 3_2: finish in time:', toc - tic)


def fun_sub4_1(matrix_a21, matrix_b12, length, matrix_22_1):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_22_1.append(strassen2_mult.strassen2(matrix_a21, matrix_b12, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 4_1:finish in time:', toc - tic)


def fun_sub4_2(matrix_a22, matrix_b22, length, matrix_22_2):
    # print('Current process is {0}'.format(os.getpid()))
    # tic = timer()
    matrix_22_2.append(strassen2_mult.strassen2(matrix_a22, matrix_b22, length // 2, boundary=32))
    # toc = timer()
    # print('<< out fun 4_2:finish in time:', toc - tic)


"""
@ Function: strassen3_solver(file_1, file_2)
    the solver method for the multiprocessing optimization
@ Parameters: file_1, file_2
    the test files that read in
"""


def strassen3_solver(file_1, file_2):
    matrix_11_1 = multiprocessing.Manager().list()  # creat a shared variable for sub process and this(parent) process
    matrix_11_2 = multiprocessing.Manager().list()
    matrix_12_1 = multiprocessing.Manager().list()
    matrix_12_2 = multiprocessing.Manager().list()
    matrix_21_1 = multiprocessing.Manager().list()
    matrix_21_2 = multiprocessing.Manager().list()
    matrix_22_1 = multiprocessing.Manager().list()
    matrix_22_2 = multiprocessing.Manager().list()
    # length = multiprocessing.Manager().Value('i', 0)  # no need to create this shared variable

    m1_file = open(file_1, 'r+')
    m2_file = open(file_2, 'r+')

    matrix_a = read_matrix(m1_file)  # read matrices
    matrix_b = read_matrix(m2_file)

    length = int(math.sqrt(len(matrix_a)))  # get the length of the read-in matrix

    # if the read-in matrix length is not even number, need to change it into even for later eight sub matrices
    if length % 2 != 0:
        matrix_a = matrix_a.reshape(length, length)
        matrix_b = matrix_b.reshape(length, length)
        matrix_a = np.r_[matrix_a, np.zeros(length, dtype=int).reshape(1, length)]
        matrix_a = np.c_[matrix_a, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
        matrix_b = np.r_[matrix_b, np.zeros(length, dtype=int).reshape(1, length)]
        matrix_b = np.c_[matrix_b, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
        length += 1

    matrix_a11 = strassen_mult.matrix_divide(matrix_a, 1, 1, length)  # divided into eight sub-matrices
    matrix_a12 = strassen_mult.matrix_divide(matrix_a, 1, 2, length)
    matrix_a21 = strassen_mult.matrix_divide(matrix_a, 2, 1, length)
    matrix_a22 = strassen_mult.matrix_divide(matrix_a, 2, 2, length)

    matrix_b11 = strassen_mult.matrix_divide(matrix_b, 1, 1, length)
    matrix_b12 = strassen_mult.matrix_divide(matrix_b, 1, 2, length)
    matrix_b21 = strassen_mult.matrix_divide(matrix_b, 2, 1, length)
    matrix_b22 = strassen_mult.matrix_divide(matrix_b, 2, 2, length)

    # Here is the code I firstly tried to use Threading module to optimize, but failed
    # thread1 = MyThread(1, matrix_a11, matrix_b11, 1)
    # thread2 = MyThread(2, matrix_a12, matrix_b21, 2)
    # ...
    # thread7 = MyThread(7, matrix_a21, matrix_b12, 7)
    # thread8 = MyThread(8, matrix_a22, matrix_b22, 8)

    # create eight sub-processes, and pass in the target functions and correspond arguments
    tic = timer()
    p1 = multiprocessing.Process(target=fun_sub1_1, args=(matrix_a11, matrix_b11, length, matrix_11_1))
    p2 = multiprocessing.Process(target=fun_sub1_2, args=(matrix_a12, matrix_b21, length, matrix_11_2))
    p3 = multiprocessing.Process(target=fun_sub2_1, args=(matrix_a11, matrix_b12, length, matrix_12_1))
    p4 = multiprocessing.Process(target=fun_sub2_2, args=(matrix_a12, matrix_b22, length, matrix_12_2))
    p5 = multiprocessing.Process(target=fun_sub3_1, args=(matrix_a21, matrix_b11, length, matrix_21_1))
    p6 = multiprocessing.Process(target=fun_sub3_2, args=(matrix_a22, matrix_b21, length, matrix_21_2))
    p7 = multiprocessing.Process(target=fun_sub4_1, args=(matrix_a21, matrix_b12, length, matrix_22_1))
    p8 = multiprocessing.Process(target=fun_sub4_2, args=(matrix_a22, matrix_b22, length, matrix_22_2))

    # start those process and join the results
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()

    # thread1.start()
    # thread2.start()
    # ...
    # thread8.start()

    # thread1.join()
    # ...
    # thread8.join()

    matrix_11 = strassen_mult.matrix_add(matrix_11_1[0], matrix_11_2[0])  # the four new sub-matrices
    matrix_12 = strassen_mult.matrix_add(matrix_12_1[0], matrix_12_2[0])
    matrix_21 = strassen_mult.matrix_add(matrix_21_1[0], matrix_21_2[0])
    matrix_22 = strassen_mult.matrix_add(matrix_22_1[0], matrix_22_2[0])
    result_matrix = strassen_mult.matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22)  # get the result here
    toc = timer()

    # used to test the multiplication result
    # result_length = int(math.sqrt(len(result_matrix)))
    # result_matrix = result_matrix.reshape(result_length, result_length)
    # print('>> [INFO] Output matrix B:\n', result_matrix, '\nresult length:', result_length)
    return toc - tic


""""
@ Function: set_threshold(data_N, optimized, standard)
    find the threshold point and write it into a .yaml configuration file
@ Parameters: data_N
    the list of N values that used to test
@ Parameters: optimized, standard
    the runtime results of the optimized algorithm(the multi-processing lower bound 32 optimization), 
    and the results of the standard one
"""


def set_threshold(data_N, optimized, standard):
    if optimized[1] > standard[1]:  # judge that standard is really lower at first
        pass
        # print('standard is lower than optimized at first')
    else:
        pass
        # print('standard is faster at first')

    for index in range(len(data_N)):
        if optimized[index] < standard[index]:  # the condition to find the threshold
            # print('find the threshold:', data_N[index])
            threshlod = data_N[index]
            filename = '..\\config\\threshold.yaml'  # write into a configuration file
            file2write = open(filename, 'w')
            file2write.write('Adapted Configuration:\n\tMethods:\n\t\t- '
                             'Strassen3\n\t\t- Standard\n\tThreshold:\n\t\t- %d' % threshlod)
            file2write.close()
            return threshlod
        else:
            pass
            # print('in', data_N, 'not found yet')


"""
@ Function: adapted_mult(test_file, length, threshold_val)
    the adapted multiplication method, return using standard when N is under threshold, 
    return using strassen3_solver(the multi-processing lower bound 32 optimization) when larger than it
"""


def adapted_mult(test_file, length, threshold_val):
    if length >= threshold_val:
        return strassen3_solver(test_file, testfile)
    else:
        return standard_mult.standard_solver(test_file, testfile)


"""
@ Main: a similar method like the main() in the assemble_test.py
    as NOTED in the upper comment of this file, I need to create a main process for using the 
    multiprocessing module provided by python
"""


if __name__ == "__main__":
    print('parent process is {0}'.format(os.getpid()))
    data_n = list()
    data_strassen3_time = list()
    data_standard_time = list()
    # boundary = 32  # used for the optimized strassen method: strassen2_mult.py
    multi_number = 20
    for i in range(5, 13):
        data_n.append(i * multi_number)
        # generate random tests
        # generate_test('..\\test\\generate_test_%d.txt' % (i * multi_number), i * multi_number)
        testfile = '..\\test\\generate_test_%d.txt' % (i * multi_number)

        # use different solver methods to get runtime of different n given
        strassen3_time = strassen3_solver(testfile, testfile)
        standard_time = standard_mult.standard_solver(testfile, testfile)
        print()
        print('N is:', i * multi_number,
              '\nstrassen3_time:', strassen3_time,
              '\nstandard_time:', standard_time)
        print()
        data_strassen3_time.append(strassen3_time)
        data_standard_time.append(standard_time)
    assemble_test.write_data('..\\data\\dataset_strassen3.txt', data_n, data_strassen3_time, 2)
    assemble_test.write_data('..\\data\\dataset_standard.txt', data_n, data_standard_time, 1)
    plotGraph.plot_triplex(['..\\data\\dataset_strassen3.txt', '..\\data\\dataset_standard.txt'],
                           ['strassen3', 'standard'])
    threshold = set_threshold(data_n, data_strassen3_time, data_standard_time)
    data_adapted_time = list()
    data_n.clear()
    for i in range(1, 20):
        data_n.append(i * multi_number)
        testfile = '..\\test\\generate_test_%d.txt' % (i * multi_number)

        # use different solver methods to get runtime of different n given
        adapted_time = adapted_mult(testfile, i * multi_number, threshold)
        # print('>> N is:', i * multi_number,
        #       '\nadapted_time:', adapted_time)
        data_adapted_time.append(adapted_time)
    assemble_test.write_data('..\\data\\dataset_adapted.txt', data_n, data_adapted_time, 2)
    plotGraph.plot_triplex(['..\\data\\dataset_adapted.txt'],
                           ['adapted'])
