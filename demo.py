#   1 # coding=utf-8
#   2 # copyright@zhangwenchi at 2019/9/21
#   3 import numpy as np
#   4
#   5
#   6 num_addorsub=0
#   7 num_mul=0
#   8 num_assign=0
#   9
#  10 def read_matrix(file_path):
#  11     input_matrix = list()
#  12     with open(file_path, 'r') as f:
#  13         txt = f.read()
#  14         for line in txt.split('\n'):
#  15             input_matrix.extend(line.split())
#  16     matrix = [list() for i in range(0, 6)]
#  17     for i in range(0, 6):
#  18         for j in range(0, 6):
#  19             matrix[i].append(float(input_matrix[i * 6 + j]))
#  20     return matrix
#  21
#  22 def matrix_add(matrix_a, matrix_b):
#  23     '''
#  24     :param matrix_a:
#  25     :param matrix_b:
#  26     :return:matrix_c=matrix_a+matrix_b
#  27     '''
#  28     rows = len(matrix_a) # get numbers of rows
#  29     columns = len(matrix_a[0]) # get numbers of cols
#  30     matrix_c = [list() for i in range(rows)] # build matrix 2d list
#  31     for i in range(rows):
#  32         for j in range(columns):
#  33             matrix_c_temp = matrix_a[i][j] + matrix_b[i][j]
#  34             global num_addorsub,num_assign
#  35             num_addorsub=num_addorsub+1
#  36             num_assign = num_assign+1
#  37             matrix_c[i].append(matrix_c_temp)
#  38     return matrix_c
#  39
#  40
#  41 def matrix_minus(matrix_a, matrix_b):
#  42     '''
#  43     :param matrix_a:
#  44     :param matrix_b:
#  45     :return:matrix_c=matrix_a-matrix_b
#  46     '''
#  47     rows = len(matrix_a)
#  48     columns = len(matrix_a[0])
#  49     matrix_c = [list() for i in range(rows)]
#  50     for i in range(rows):
#  51         for j in range(columns):
#  52             matrix_c_temp = matrix_a[i][j] - matrix_b[i][j]
#  53             global num_addorsub,num_assign
#  54             num_addorsub = num_addorsub + 1
#  55             num_assign=num_assign+1
#  56             matrix_c[i].append(matrix_c_temp)
#  57     return matrix_c
#  58
#  59
#  60 def matrix_divide(matrix_a, row, column):
#  61     '''
#  62     :param matrix_a:
#  63     :param row:
#  64     :param column:
#  65     :return: matrix_b=matrix_a(row,column) to divide matrix_a
#  66     '''
#  67     length = len(matrix_a)
#  68     matrix_b = [list() for i in range(length // 2)]
#  69     k = 0
#  70     for i in range((row - 1) * length // 2, row * length // 2):
#  71         for j in range((column - 1) * length // 2, column * length // 2):
#  72             matrix_c_temp = matrix_a[i][j]
#  73             matrix_b[k].append(matrix_c_temp)
#  74         k += 1
#  75     return matrix_b
#  76
#  77
#  78 def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
#  79     '''
#  80     :param matrix_11:
#  81     :param matrix_12:
#  82     :param matrix_21:
#  83     :param matrix_22:
#  84     :return:mariix merged by 4 parts above
#  85     '''
#  86     length = len(matrix_11)
#  87     matrix_all = [list() for i in range(length * 2)]  # build a matrix of double rows
#  88     for i in range(length):
#  89         # for each row. matrix_all list contain row of matrix_11 and matrix_12
#  90         matrix_all[i] = matrix_11[i] + matrix_12[i]
#  91     for j in range(length):
#  92         # for each row. matrix_all list contain row of matrix_21 and matrix_22
#  93         matrix_all[length + j] = matrix_21[j] + matrix_22[j]
#  94     return matrix_all
#  95
#  96
#  97 def strassen(matrix_a, matrix_b):
#  98     '''
#  99     :param matrix_a:
# 100     :param matrix_b:
# 101     :return:matrix_a * matrix_b
# 102     '''
# 103     rows = len(matrix_a)
# 104     if rows == 1:
# 105         matrix_all = [list() for i in range(rows)]
# 106         matrix_all[0].append(matrix_a[0][0] * matrix_b[0][0])
# 107     elif(rows % 2 ==1):
# 108         matrix_a_np = np.array(matrix_a)
# 109         matrix_b_np = np.array(matrix_b)
# 110         matrix_all = np.dot(matrix_a_np,matrix_b_np)
# 111         global num_mul,num_addorsub
# 112         num_mul = num_mul + 27
# 113         num_addorsub=num_addorsub + 18
# 114     else:
# 115         # 10 first parts of computing
# 116         s1 = matrix_minus((matrix_divide(matrix_b, 1, 2)), (matrix_divide(matrix_b, 2, 2)))
# 117         s2 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 1, 2)))
# 118         s3 = matrix_add((matrix_divide(matrix_a, 2, 1)), (matrix_divide(matrix_a, 2, 2)))
# 119         s4 = matrix_minus((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 1, 1)))
# 120         s5 = matrix_add((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 2)))
# 121         s6 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 2, 2)))
# 122         s7 = matrix_minus((matrix_divide(matrix_a, 1, 2)), (matrix_divide(matrix_a, 2, 2)))
# 123         s8 = matrix_add((matrix_divide(matrix_b, 2, 1)), (matrix_divide(matrix_b, 2, 2)))
# 124         s9 = matrix_minus((matrix_divide(matrix_a, 1, 1)), (matrix_divide(matrix_a, 2, 1)))
# 125         s10 = matrix_add((matrix_divide(matrix_b, 1, 1)), (matrix_divide(matrix_b, 1, 2)))
# 126         # 7 second parts of computing
# 127         p1 = strassen(matrix_divide(matrix_a, 1, 1), s1)
# 128         p2 = strassen(s2, matrix_divide(matrix_b, 2, 2))
# 129         p3 = strassen(s3, matrix_divide(matrix_b, 1, 1))
# 130         p4 = strassen(matrix_divide(matrix_a, 2, 2), s4)
# 131         p5 = strassen(s5, s6)
# 132         p6 = strassen(s7, s8)
# 133         p7 = strassen(s9, s10)
# 134         # 4 final parts of result
# 135         c11 = matrix_add(matrix_add(p5, p4), matrix_minus(p6, p2))
# 136         c12 = matrix_add(p1, p2)
# 137         c21 = matrix_add(p3, p4)
# 138         c22 = matrix_minus(matrix_add(p5, p1), matrix_add(p3, p7))
# 139         matrix_all = matrix_merge(c11, c12, c21, c22)
# 140         global num_assign
# 141         num_assign =num_assign+22
# 142     return matrix_all
# 143
# 144
# 145 def main():
# 146     # read data
# 147     A = read_matrix('matrixA.txt')
# 148     B = read_matrix('matrixB.txt')
# 149
# 150     # compute A*B
# 151     C = strassen(A,B)
# 152     print("\nResult of matrix given\n",np.array(C))
# 153
# 154     # verificate A*B
# 155     C_verification=np.dot(A,B)
# 156     print("\nSubtract from standard results\n",np.array((C-C_verification),dtype=int))
# 157
# 158     # statistical data
# 159     print("\nfrequency of add/sub",num_addorsub)
# 160     print("frequency of assign", num_assign)
# 161     print("frequency of mul", num_mul)
# 162
# 163     new_matrixA = np.random.random_integers(-5,5,size=(8, 8))
# 164     print("\nRandom Matrix A:\n", new_matrixA)
# 165     new_matrixB = np.random.random_integers(-5,5,size=(8, 8))
# 166     print("\nRandom Matrix B:\n", new_matrixB)
# 167
# 168     AdotB=strassen(new_matrixA, new_matrixB)
# 169     print("\n A*B Result of matrixs by generate randomly\n",np.array(AdotB))
# 170
# 171     BdotA = strassen(new_matrixB, new_matrixA)
# 172     print("\n B*A Result of matrixs by generate randomly\n", np.array(BdotA))
# 173
# 174     result=new_matrixA
# 175     for i in range(0,2019):
# 176         result=strassen(result,new_matrixA)
# 177     print("\n A^2019 Result of matrixs by generate randomly\n",np.array(result))
# 178 if __name__ == '__main__':
# 179     main()
