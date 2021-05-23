# txt file should be as following

# file name: {method, standard for 0 & strassen for 1}{number of sampling points}{your name}
# ie: 0_10_guo means: using standard method and have runtimes of 10 n values, upload by guo

# - 1st line: [matrix dimension, method type] -> 10 0
# - 2ed line: array dimension -> 1024 2048 4095 8192 ... 16334
# - 3rd line: execution time (seconds) -> 1 3 5 12 35 ... 25

import matplotlib.pyplot as plt


def read_file(filenames):
    index = 0
    files = list()
    for filename in filenames:
        with open(filename) as f:
            files.append(f.readlines())  # read in all the context
        f.close()
        index = index + 1
    return files  # a array contains all the files' strings


# param: plotGraph(list[filename1, filename2,...]]
def plot_graph(filenames, descriptions):
    index = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    values = list()

    for lines in read_file(filenames):
        test_attr_str = lines[0].split(' ')
        dimension = eval(test_attr_str[0])
        method_type = eval(test_attr_str[1].replace('\n', ''))

        # print('>> dimension:', dimension, '\n>> type:', method_type)

        n_strings = lines[1].replace('\n', '').split(' ')
        x_values = list(map(int, n_strings))

        # print('>> x axis values is:', x_values)

        runtimes_strs = lines[2].replace('\n', '').split(' ')
        y_values = list(map(float, runtimes_strs))

        # print('>> y axis values is:', y_values)

        ax.plot(x_values, y_values, label=descriptions[index])
        plt.xlabel('n')
        plt.ylabel('Execution Time / seconds')
        index = index + 1

    plt.legend(loc='upper left')
    plt.show()


def plot_solver(standard_file, standard_des, strassen_file, strassen_des):
    plot_graph([standard_file, strassen_file], [standard_des, strassen_des])


def plot_triplex(filenames, descriptions):
    plot_graph(filenames, descriptions)
