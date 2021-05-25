import random

import strassen_mult
import standard_mult
import strassen2_mult
import strassen3_mult
import plotGraph

"""
@ Function: generate_test(filename, n)
@ Parameter: filename
    the file name of the generated test file
@ Parameter: n
    the length of the matrix generated
"""


def generate_test(filename, n):
    file2write = open(filename, 'w')
    for i in range(n):
        for j in range(n - 1):
            line = '%d ' % (random.randint(0, 9))
            file2write.write(line)
        line = '%d\n' % (random.randint(0, 9))
        file2write.write(line)
    file2write.close()


"""
@ Function: assemble_test.py
    the function used to assembly test different algorithms
@ Variable: data_n
    a list of "n" values used to ...
@ Variable: data_strassen_time
    ...
"""


def main():
    data_n = list()
    # data_strassen_time = list()
    data_standard_time = list()
    data_strassen2_time = list()
    data_strassen3_time = list()
    boundary = 6  # used for the optimized strassen method: strassen2_mult.py

    multi_number = 20

    for i in range(1, 25):
        data_n.append(i * multi_number)

        # generate random tests
        # generate_test('..\\test\\generate_test_%d.txt' % (i * multi_number), i * multi_number)
        testfile = '..\\test\\generate_test_%d.txt' % (i * multi_number)

        # use different solver methods to get runtime of different n given
        # strassen_time = strassen_mult.strassen_solver(testfile, testfile)
        standard_time = standard_mult.standard_solver(testfile, testfile)
        strassen2_time = strassen2_mult.strassen2_solver(testfile, testfile, boundary)
        strassen3_time = strassen3_mult.strassen3_solver(testfile, testfile)

        # print('>> N is:', i * multi_number, '\nstandard_time:', standard_time, '\nstrassen_time:', strassen_time,
        # '\nadapted_time:', adapted_time)

        print('>> N is:', i * multi_number, '\nstandard_time:', standard_time,
              '\nstrassen2_time:', strassen2_time,
              '\nstrassen3_time:', strassen3_time)

        data_standard_time.append(standard_time)
        # data_strassen_time.append(strassen_time)
        data_strassen2_time.append(strassen2_time)
        data_strassen3_time.append(strassen3_time)

    write_data('..\\data\\dataset_standard.txt', data_n, data_standard_time, 1)
    # write_data('data\\dataset_strassen.txt', data_n, data_strassen_time, 0)
    write_data('..\\data\\dataset_strassen2.txt', data_n, data_strassen2_time, 2)
    write_data('..\\data\\dataset_strassen3.txt', data_n, data_strassen3_time, 2)

    # plotGraph.plot_triplex(['data\\dataset_standard.txt', 'data\\dataset_strassen.txt', 'data\\dataset_adapted.txt'],
    #                        ['standard', 'strassen', 'adapted-%s' % boundary])

    plotGraph.plot_triplex(['..\\data\\dataset_standard.txt', '..\\data\\dataset_strassen2.txt',
                            '..\\data\\dataset_strassen3.txt'],
                           ['standard', 'strassen2', 'strassen3'])


def write_data(filename, data_n, data_times, method_type):
    file2write = open(filename, 'w')
    # print('data length:', len(data_n), 'equals', len(data_times))
    # print('data_n:\n', data_n)
    # print('data_times\n:', data_times)
    data_length = len(data_n)
    file2write.write('%d %d\n' % (data_length, method_type))
    for i in range(data_length - 1):
        file2write.write('%d ' % data_n[i])
    file2write.write('%d\n' % data_n[data_length - 1])
    for i in range(data_length - 1):
        file2write.write('%f ' % data_times[i])
    file2write.write('%f' % data_times[data_length - 1])


if __name__ == '__main__':
    main()
