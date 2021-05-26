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


def read_matrix(m_lines):
    newMatrix = []
    for m_line in m_lines:
        m_line = m_line.split()
        int_line = list(map(int, m_line))
        newMatrix.append(int_line)
    return np.array(newMatrix).reshape(-1)


def fun_sub1_1(matrix_a11, matrix_b11, length, matrix_11_1):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_11_1.append(strassen2_mult.strassen2(matrix_a11, matrix_b11, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 1_1: finish in time:', toc - tic)


def fun_sub1_2(matrix_a12, matrix_b21, length, matrix_11_2):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_11_2.append(strassen2_mult.strassen2(matrix_a12, matrix_b21, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 1_2: finish in time:', toc - tic)


def fun_sub2_1(matrix_a11, matrix_b12, length, matrix_12_1):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_12_1.append(strassen2_mult.strassen2(matrix_a11, matrix_b12, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 2_1: finish in time:', toc - tic)


def fun_sub2_2(matrix_a12, matrix_b22, length, matrix_12_2):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_12_2.append(strassen2_mult.strassen2(matrix_a12, matrix_b22, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 2_2: finish in time:', toc - tic)


def fun_sub3_1(matrix_a21, matrix_b11, length, matrix_21_1):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_21_1.append(strassen2_mult.strassen2(matrix_a21, matrix_b11, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 3_1: finish in time:', toc - tic)


def fun_sub3_2(matrix_a22, matrix_b21, length, matrix_21_2):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_21_2.append(strassen2_mult.strassen2(matrix_a22, matrix_b21, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 3_2: finish in time:', toc - tic)


def fun_sub4_1(matrix_a21, matrix_b12, length, matrix_22_1):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_22_1.append(strassen2_mult.strassen2(matrix_a21, matrix_b12, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 4_1:finish in time:', toc - tic)


def fun_sub4_2(matrix_a22, matrix_b22, length, matrix_22_2):
    # print('Current process is {0}'.format(os.getpid()))
    tic = timer()
    matrix_22_2.append(strassen2_mult.strassen2(matrix_a22, matrix_b22, length // 2, boundary=32))
    toc = timer()
    # print('<< out fun 4_2:finish in time:', toc - tic)


# class MyThread(threading.Thread):
#     def __init__(self, thread_id, matrix_1, matrix_2, counter):
#         threading.Thread.__init__(self)
#         self.threadID = thread_id
#         self.counter = counter
#         self.matrix_1 = matrix_1
#         self.matrix_2 = matrix_2
#
#     def run(self):
#         # print("run in:,", self.threadID)
#         if self.counter == 1:
#             fun_sub1_1(self.matrix_1, self.matrix_2)
#         elif self.counter == 2:
#             fun_sub1_2(self.matrix_1, self.matrix_2)
#         elif self.counter == 3:
#             fun_sub2_1(self.matrix_1, self.matrix_2)
#         elif self.counter == 4:
#             fun_sub2_2(self.matrix_1, self.matrix_2)
#         elif self.counter == 5:
#             fun_sub3_1(self.matrix_1, self.matrix_2)
#         elif self.counter == 6:
#             fun_sub3_2(self.matrix_1, self.matrix_2)
#         elif self.counter == 7:
#             fun_sub4_1(self.matrix_1, self.matrix_2)
#         elif self.counter == 8:
#             fun_sub4_2(self.matrix_1, self.matrix_2)
#         # print("run out:", self.threadID)


def strassen3_solver(file_1, file_2):
    matrix_11_1 = multiprocessing.Manager().list()
    matrix_11_2 = multiprocessing.Manager().list()
    matrix_12_1 = multiprocessing.Manager().list()
    matrix_12_2 = multiprocessing.Manager().list()
    matrix_21_1 = multiprocessing.Manager().list()
    matrix_21_2 = multiprocessing.Manager().list()
    matrix_22_1 = multiprocessing.Manager().list()
    matrix_22_2 = multiprocessing.Manager().list()
    length = multiprocessing.Manager().Value('i', 0)

    m1_file = open(file_1, 'r+')
    m2_file = open(file_2, 'r+')

    matrix_a = read_matrix(m1_file)
    matrix_b = read_matrix(m2_file)

    length = int(math.sqrt(len(matrix_a)))
    if length % 2 != 0:
        matrix_a = matrix_a.reshape(length, length)
        matrix_b = matrix_b.reshape(length, length)
        matrix_a = np.r_[matrix_a, np.zeros(length, dtype=int).reshape(1, length)]
        matrix_a = np.c_[matrix_a, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
        matrix_b = np.r_[matrix_b, np.zeros(length, dtype=int).reshape(1, length)]
        matrix_b = np.c_[matrix_b, np.zeros(length + 1, dtype=int).reshape(length + 1, 1)]
        length += 1

    matrix_a11 = strassen_mult.matrix_divide(matrix_a, 1, 1, length)
    matrix_a12 = strassen_mult.matrix_divide(matrix_a, 1, 2, length)
    matrix_a21 = strassen_mult.matrix_divide(matrix_a, 2, 1, length)
    matrix_a22 = strassen_mult.matrix_divide(matrix_a, 2, 2, length)

    matrix_b11 = strassen_mult.matrix_divide(matrix_b, 1, 1, length)
    matrix_b12 = strassen_mult.matrix_divide(matrix_b, 1, 2, length)
    matrix_b21 = strassen_mult.matrix_divide(matrix_b, 2, 1, length)
    matrix_b22 = strassen_mult.matrix_divide(matrix_b, 2, 2, length)
    # print('>> [INFO] Output matrix B:\n', matrix_b11.reshape(length // 2, length // 2), '\nresult length:',
    #       length // 2)

    # thread1 = MyThread(1, matrix_a11, matrix_b11, 1)
    # thread2 = MyThread(2, matrix_a12, matrix_b21, 2)
    # thread3 = MyThread(3, matrix_a11, matrix_b12, 3)
    # thread4 = MyThread(4, matrix_a12, matrix_b22, 4)
    # thread5 = MyThread(5, matrix_a21, matrix_b11, 5)
    # thread6 = MyThread(6, matrix_a22, matrix_b21, 6)
    # thread7 = MyThread(7, matrix_a21, matrix_b12, 7)
    # thread8 = MyThread(8, matrix_a22, matrix_b22, 8)

    tic = timer()
    p1 = multiprocessing.Process(target=fun_sub1_1, args=(matrix_a11, matrix_b11, length, matrix_11_1))
    p2 = multiprocessing.Process(target=fun_sub1_2, args=(matrix_a12, matrix_b21, length, matrix_11_2))
    p3 = multiprocessing.Process(target=fun_sub2_1, args=(matrix_a11, matrix_b12, length, matrix_12_1))
    p4 = multiprocessing.Process(target=fun_sub2_2, args=(matrix_a12, matrix_b22, length, matrix_12_2))
    p5 = multiprocessing.Process(target=fun_sub3_1, args=(matrix_a21, matrix_b11, length, matrix_21_1))
    p6 = multiprocessing.Process(target=fun_sub3_2, args=(matrix_a22, matrix_b21, length, matrix_21_2))
    p7 = multiprocessing.Process(target=fun_sub4_1, args=(matrix_a21, matrix_b12, length, matrix_22_1))
    p8 = multiprocessing.Process(target=fun_sub4_2, args=(matrix_a22, matrix_b22, length, matrix_22_2))

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
    # thread3.start()
    # thread4.start()
    # thread5.start()
    # thread6.start()
    # thread7.start()
    # thread8.start()
    #
    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()
    # thread5.join()
    # thread6.join()
    # thread7.join()
    # thread8.join()

    matrix_11 = strassen_mult.matrix_add(matrix_11_1[0], matrix_11_2[0])
    matrix_12 = strassen_mult.matrix_add(matrix_12_1[0], matrix_12_2[0])
    matrix_21 = strassen_mult.matrix_add(matrix_21_1[0], matrix_21_2[0])
    matrix_22 = strassen_mult.matrix_add(matrix_22_1[0], matrix_22_2[0])
    result_matrix = strassen_mult.matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22)
    toc = timer()
    result_length = int(math.sqrt(len(result_matrix)))
    result_matrix = result_matrix.reshape(result_length, result_length)
    # print('>> [INFO] Output matrix B:\n', result_matrix, '\nresult length:', result_length)  # FIXME: adjust result
    return toc - tic


def set_threshold(data_N, optimized, standard):
    threshlod = 0
    if optimized[1] > standard[1]:  # standard is really lower at first
        data_2_is_standard = True
        print('standard is lower than optimized at first')
    else:
        print('standard is faster at first')

    for index in range(len(data_N)):
        if optimized[index] < standard[index]:
            print('find the threshold:', data_N[index])
            threshlod = data_N[index]
            filename = '..\\config\\threshold.yaml'
            file2write = open(filename, 'w')
            file2write.write('Adapted Configuration:\n\tMethods:\n\t\t- '
                             'Strassen3\n\t\t- Standard\n\tThreshold:\n\t\t- %d' % threshlod)
            file2write.close()
            return threshlod
        else:
            print('in', data_N, 'not found yet')


def adapted_mult(test_file, length, threshold_val):
    if length >= threshold_val:
        return strassen3_solver(test_file, testfile)
    else:
        return standard_mult.standard_solver(test_file, testfile)


if __name__ == "__main__":
    print('parent process is {0}'.format(os.getpid()))
    data_n = list()
    data_strassen3_time = list()
    data_standard_time = list()
    boundary = 32  # used for the optimized strassen method: strassen2_mult.py
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
