import random

import strassen_mult
import standard_mult
import strassen2_mult
import plotGraph

"""
@ Filename: assemble_test.py
    assembly test all the methods here(except methods about multi-processing), and plot results of them
@ Methods: 
    generate_test(filename, n)
    main()
    write_data(filename, data_n, data_times, method_type)
"""


"""
@ Function: generate_test(filename, n)
    generate tests for random numbers, and write them into test files
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
    is a list of "n" values used in the test. In the following for loop, NOTED that 
    'multi_number = 10' is the distance of each N value, 'for i in range(1, 5)' means that the test range is:
    [10 20 30 40]
    
{take strassen algorithm for example}
@ Variable: data_strassen_time
    is a list of time of the running results
@ Variable: strassen_time
    is a single result for a particular N value, been append to data_strassen_time
"""


def main():
    data_n = list()
    data_strassen_time = list()
    # boundary = 6  # used for the optimized strassen method: strassen2_mult.py

    multi_number = 10
    for i in range(1, 5):
        data_n.append(i * multi_number)
        testfile = '..\\test\\generate_test_%d.txt' % (i * multi_number)
        strassen_time = strassen_mult.strassen_solver(testfile, testfile)
        data_strassen_time.append(strassen_time)
    write_data('..\\data\\dataset_strassen_without_print.txt', data_n, data_strassen_time, 0)  # write in dataset_*
    plotGraph.plot_triplex(['data\\dataset_strassen.txt'], ['strassen'])


"""
@ Function: write_data(filename, data_n, data_times, method_type)
    write data into the 'filename' file
@ Parameters: filename, data_n, data_times, method_type
    method_type is 0 for strassen, 1 for standard, 2 for optimized
"""


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
