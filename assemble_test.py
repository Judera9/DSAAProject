import random

import strassen_mut
import standard_mut
import adapted_mut
import plotGraph


def generate_test(filename, n):
    file2write = open(filename, 'w')
    for i in range(n):
        for j in range(n - 1):
            line = '%d ' % (random.randint(0, 9))
            file2write.write(line)
        line = '%d\n' % (random.randint(0, 9))
        file2write.write(line)
    file2write.close()


def main():
    data_n = list()
    data_strassen_time = list()
    data_standard_time = list()
    data_adapted_time = list()
    multi_number = 250
    boundary = 32
    data_adapted_time_32 = list()
    data_adapted_time_64 = list()
    data_adapted_time_128 = list()
    multi_number = 25
    # boundary = 32
    for i in range(1, 20):
        data_n.append(i * multi_number)

        generate_test('test\\generate_test_%d.txt' % (i * multi_number), i * multi_number)  # generate random test
        testfile = 'test\\generate_test_%d.txt' % (i * multi_number)

        strassen_time = strassen_mut.strassen_solver(testfile, testfile)
        standard_time = standard_mut.standard_solver(testfile, testfile)
        adapted_time_32 = adapted_mut.adapted_solver(testfile, testfile, 32)
        adapted_time_64 = adapted_mut.adapted_solver(testfile, testfile, 64)
        adapted_time_128 = adapted_mut.adapted_solver(testfile, testfile, 128)

        # print('>> N is:', i * multi_number, '\nstandard_time:', standard_time, '\nstrassen_time:', strassen_time,
        # '\nadapted_time:', adapted_time)

        # print('>> N is:', i * multi_number, '\nstandard_time:', standard_time, '\nadapted_time:', adapted_time)

        print('>> N is:', i * multi_number, '\nstandard_time:', standard_time, '\nstrassen_time:', strassen_time,
              '\nadapted_time_32:', adapted_time_32,
              '\nadapted_time_64:', adapted_time_64, '\nadapted_time_128:', adapted_time_128)

        data_standard_time.append(standard_time)
        data_strassen_time.append(strassen_time)
        data_adapted_time_32.append(adapted_time_32)
        data_adapted_time_64.append(adapted_time_64)
        data_adapted_time_128.append(adapted_time_128)

    write_data('data\\dataset_standard.txt', data_n, data_standard_time, 1)
    write_data('data\\dataset_strassen.txt', data_n, data_strassen_time, 0)
    write_data('data\\dataset_adapted_32.txt', data_n, data_adapted_time_32, 2)
    write_data('data\\dataset_adapted_64.txt', data_n, data_adapted_time_64, 2)
    write_data('data\\dataset_adapted_128.txt', data_n, data_adapted_time_128, 2)

    # plotGraph.plot_triplex(['data\\dataset_standard.txt', 'data\\dataset_strassen.txt', 'data\\dataset_adapted.txt'],
    #                        ['standard', 'strassen', 'adapted-%s' % boundary])

    plotGraph.plot_triplex(['data\\dataset_standard.txt', 'data\\dataset_strassen.txt', 'data\\dataset_adapted_32.txt',
                            'data\\dataset_adapted_64.txt', 'data\\dataset_adapted_128.txt'],
                           ['standard', 'strassen', 'adapted-%s' % 32, 'adapted-%s' % 64, 'adapted-%s' % 128])


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
