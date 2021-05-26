import random

import strassen_mult
import standard_mult
import strassen2_mult
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
    data_strassen_time = list()
    # data_standard_time = list()
    # data_strassen2_4_time = list()
    # data_strassen2_6_time = list()
    # data_strassen2_8_time = list()
    # data_strassen3_time = list()
    # boundary = 6  # used for the optimized strassen method: strassen2_mult.py

    multi_number = 10

    for i in range(1, 5):
        data_n.append(i * multi_number)

        # generate random tests
        # generate_test('..\\test\\generate_test_%d.txt' % (i * multi_number), i * multi_number)
        testfile = '..\\test\\generate_test_%d.txt' % (i * multi_number)

        # use different solver methods to get runtime of different n given
        strassen_time = strassen_mult.strassen_solver(testfile, testfile)
        # strassen2_4_time = strassen2_mult.strassen2_solver(testfile, testfile, boundary=4)
        # strassen2_6_time = strassen2_mult.strassen2_solver(testfile, testfile, boundary=6)
        # strassen2_8_time = strassen2_mult.strassen2_solver(testfile, testfile, boundary=8)

        # print('>> N is:', i * multi_number, '\nstandard_time:', standard_time, '\nstrassen_time:', strassen_time,
        # '\nadapted_time:', adapted_time)

        print('>> N is:', i * multi_number,
              '\nstrassen_time:', strassen_time,
              # '\nstrassen2_8_time:', strassen2_8_time
              )

        # data_strassen2_4_time.append(strassen2_4_time)
        data_strassen_time.append(strassen_time)
        # data_strassen2_6_time.append(strassen2_6_time)
        # data_strassen2_8_time.append(strassen2_8_time)

    # write_data('..\\data\\dataset_strassen2_4.txt', data_n, data_strassen2_4_time, 2)
    write_data('..\\data\\dataset_strassen_without_print.txt', data_n, data_strassen_time, 0)
    # write_data('..\\data\\dataset_strassen2_6.txt', data_n, data_strassen2_6_time, 2)
    # write_data('..\\data\\dataset_strassen2_8.txt', data_n, data_strassen2_8_time, 2)

    # plotGraph.plot_triplex(['data\\dataset_standard.txt', 'data\\dataset_strassen.txt', 'data\\dataset_adapted.txt'],
    #                        ['standard', 'strassen', 'adapted-%s' % boundary])

    # plotGraph.plot_triplex(['..\\data\\dataset_strassen2_6.txt',
    #                         '..\\data\\dataset_strassen2_8.txt'],
    #                        ['strassen2 with boundary 6',
    #                         'strassen2 with boundary 8'])


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
