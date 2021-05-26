# DSAAProject
strassen method adaptation and analysis

## Note -5.20
there should be a ./test/ package here, generated test in the file assemble_test.py
but it is too large.... so I don't put it here

## How to use python to plot
* download python from the official site:
[download 3.8.* version would be better](https://www.python.org/downloads/)

* use <pip install *> to install necessary modules

* install the .py files from this project

**assemble_test.py**\
In order to use python to run two matrix multiplication;

Look at the file,

~~~python
multi_number = 2
    for i in range(1, 20):
~~~

This will generate tests of distance with 2 of each n, and ranged from 2 to 38, that is, ranged from 2*[1,20)

You should change 2 and 20 to other number you want

**plot_graph.py**\
In order to use matplotlib(plt)to plot the results in "data" package

If you use algorithm in Java, generate your test results in the form like other data .txt file in "data", then run the **main.py** script. Remember to edit the file name before run it.

# 待完成任务

## 跑代码

* java adapted方法先写完
* 跑java代码，记录时间（把格式调对）
* 如果要跑python的assemble_test
* C++代码问一下，如果可以的话也跑一下数据，格式同样按照指定的格式
* plotGraph画图，**两个文件数据要一样**
* 

## 分析
* 按照链接分析
* 
* 多线程优化

## 做ppt
* 链接上关于硬件、编程语言（可以查一下不同语言递归的垃圾回收机制，函数调用栈）、等等
* 链接上的其他内容
* 根据strassen作者论文添加一些分析和说明
* 说明阶梯状的原因（做一点数学推导）
* 其他能想到的

# Finished in 5.26
Pre is not as well as expected\
Results is good\
English presentation need to be improved
