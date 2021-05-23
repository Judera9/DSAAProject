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
