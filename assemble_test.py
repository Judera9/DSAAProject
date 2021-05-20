import random

import strassen_mut
import standard_mut
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
    multi_number = 2
    for i in range(1, 20):
        data_n.append(i * multi_number)
        generate_test('test\\generate_test_%d.txt' % (i * multi_number), i * multi_number)
        testfile = 'test\\generate_test_%d.txt' % (i * multi_number)
        strassen_time = strassen_mut.strassen_solver(testfile, testfile)
        standard_time = standard_mut.standard_solver(testfile, testfile)
        print('standard_time:', standard_time, '\nstrassen_time:', strassen_time)
        data_standard_time.append(standard_time)
        data_strassen_time.append(strassen_time)
    write_data('data\\dataset_standard.txt', data_n, data_standard_time, 1)
    write_data('data\\dataset_strassen.txt', data_n, data_strassen_time, 0)
    plotGraph.plot_solver('data\\dataset_standard.txt', 'standard', 'data\\dataset_strassen.txt', 'strassen')


def write_data(filename, data_n, data_times, method_type):
    file2write = open(filename, 'w')
    print('data length:', len(data_n), 'equals', len(data_times))
    print('data_n:\n', data_n)
    print('data_times\n:', data_times)
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
