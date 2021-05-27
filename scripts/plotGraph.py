import matplotlib.pyplot as plt

"""
@ Filename: plotGraph.py
    Using methods in this file to plot graph of the results, using matplotlib
    The following is our agreement of the dataset.* file:
        txt file should be as following
        
        file name: {method, standard for 0 & strassen for 1}{number of sampling points}{your name}
        ie: 0_10_guo means: using standard method and have runtimes of 10 n values, upload by guo
        
        - 1st line: [matrix dimension, method type] -> 10 0
        - 2ed line: array dimension -> 1024 2048 4095 8192 ... 16334
        - 3rd line: execution time (seconds) -> 1 3 5 12 35 ... 25
@ Methods: 
    read_file(filenames)
    plot_graph(filenames, descriptions)
    plot_solver(standard_file, standard_des, strassen_file, strassen_des)  # deprecated
    plot_triplex(filenames, descriptions)
"""


def read_file(filenames):
    index = 0
    files = list()
    for filename in filenames:
        with open(filename) as f:
            files.append(f.readlines())  # read in all the context
        f.close()
        index = index + 1
    return files  # a array contains all the files' strings


"""
@ Function: plot_graph(filenames, descriptions)
    used to plot results
@ Parameters: filenames, descriptions
    list of files: like [file1, file2, file3...]
    list of descriptions: like [desc1, desc2, desc3...]
"""


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

        n_strings = lines[1].replace('\n', '').split(' ')
        x_values = list(map(int, n_strings))

        runtimes_strs = lines[2].replace('\n', '').split(' ')
        y_values = list(map(float, runtimes_strs))

        ax.plot(x_values, y_values, label=descriptions[index])
        plt.xlabel('n')
        plt.ylabel('Execution Time / seconds')
        index = index + 1

    plt.legend(loc='upper left')
    plt.show()


"""
@ Function(deprecated): plot_solver(standard_file, standard_des, strassen_file, strassen_des)
    plot just two of the results, deprecated now
@ Parameter: standard_file, standard_des, strassen_file, strassen_des
"""


def plot_solver(standard_file, standard_des, strassen_file, strassen_des):
    plot_graph([standard_file, strassen_file], [standard_des, strassen_des])


"""
@ Function: plot_triplex(filenames, descriptions)
    plot a list of results(actually this triplex is not only three, but can plot any number of results)
@ Parameter: filenames, descriptions
    list of files: like [file1, file2, file3...]
    list of descriptions: like [desc1, desc2, desc3...]
    NOTED: the amount of input results must have corresponding descriptions
"""


def plot_triplex(filenames, descriptions):
    plot_graph(filenames, descriptions)

# plot_triplex([
#     # '..\\data\\python_final_data\\depre_adapted\\dataset_adapted_128_to500type2.txt',
#     # '..\\data\\python_final_data\\depre_adapted\\dataset_adapted_64_to500type2.txt',
#     # '..\\data\\python_final_data\\depre_adapted\\dataset_adapted_32_to500type2.txt',
#     # '..\\data\\python_final_data\\strassen2_boundary8\\dataset_strassen2_8_to500type2.txt',
#     # '..\\data\\python_final_data\\strassen2_boundary6\\dataset_strassen2_6_to500type2.txt',
#     # '..\\data\\python_final_data\\strassen2_boundary4\\dataset_strassen2_4_to500type2.txt',
#     # '..\\data\\python_final_data\\strassen3_strassen\\dataset_strassen3(not using s2)_to1000.txt',
#     '..\\data\\python_final_data\\strassen3_strassen2_boundary6\\dataset_strassen3_strassen2_6_to1000.txt',
#     '..\\data\\python_final_data\\strassen3_strassen2_boundary32\\dataset_strassen3_strassen2_32_to1000.txt',
#     # '..\\data\\python_final_data\\standard\\dataset_standard_to500type2.txt',
#     # '..\\data\\python_final_data\\strassen_original\\dataset_strassen_to500type2.txt'
# ],
#     [
#         # 'lowerBound_128_python',
#         # 'lowerBound_64_python',
#         # 'lowerBound_32_python',
#         # 'lowerBound_8_python',
#         # 'lowerBound_6_python',
#         # 'lowerBound_4_python',
#         # 'MultiProcess_with_strassen_python',
#         'MultiProcess_with_lowerBound_6_python',
#         'MultiProcess_with_lowerBound_32_python',
#         # 'standard_python',
#         # 'strassen_python'
#     ])
#
# plot_triplex([
#     # '..\\data\\python_final_data\\depre_adapted\\dataset_adapted_64_to500type2.txt',
#     '..\\data\\java_final_data\\strassen2_128_java_4000.txt',
#     '..\\data\\java_final_data\\strassen2_64_java_4000.txt',
#     '..\\data\\java_final_data\\strassen2_32_java_4000.txt',
#     '..\\data\\java_final_data\\strassen2_16_java_4000.txt',
#     # '..\\data\\python_final_data\\standard\\dataset_standard_to500type2.txt',
#     # '..\\data\\java_final_data\\standard_java_500.txt',
#     # '..\\data\\python_final_data\\strassen_original\\dataset_strassen_to500type2.txt',
#     # '..\\data\\java_final_data\\strassen_java_500.txt'
# ],
#     [
#         # 'lowerBound_64_python',
#         'lowerBound_128_java',
#         'lowerBound_64_java',
#         'lowerBound_32_java',
#         'lowerBound_16_java',
#         # 'standard_python_500',
#         # 'standard_java',
#         # 'strassen_python_500',
#         # 'strassen_java'
#     ])

# plot_triplex(['..\\data\\c_super_method\\CPP.txt'], ['standard_method_c'])

# plot_triplex([
#     '..\\data\\dataset_strassen_with_print.txt',
#     '..\\data\\dataset_strassen_without_print.txt',
#     # '..\\data\\python_final_data\\strassen3_thread\\standard_type2.txt',
# ], [
#     'strassen_with_print',
#     'strassen_without_print',
#     # 'standard'
# ])
