# Part 1 Theoretical Analysis

Suppose that $A=(a_{ij})$ and $B=(b_{ij})$ are square $n×n$ matrices, then in the product $C=A\cdot B$, we define the entry $c_{ij}$, for $i,j=1,2,\cdots,n$, by
$$
c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj} \tag{1}
$$
We must compute $n^2$ matrix entries, and each is the sum of $n$ values. The following procedure takes $n×n$  matrices A and B and multiplies them, returning their $n×n$ product $C$. We assume that each matrix has an attribute *rows*, giving the number of rows in the matrix.

## Square Matrix Multiply

### Pseudo code

---

SQUARE-MATRIX-MULTIPLY (A, B)

1    $n = A.rows$

2    let $C$ be a new $n×n$ matrix

3    for $i=1$ to $n$

4        for $j=1$ to $n$

5            $c_{ij}=0$

6            for $k=1$ to $n$

7                $c_{ij}=c_{ij}+a_{ik}\cdot b_{kj}$

8    return $C$

---

### Proof 

The SQUARE-MATRIX-MULTIPLY procedure works as follows. The for loop of lines 3–7 computes the entries of each row $i$, and within a given row $i$, the for loop of lines 4–7 computes each of the entries $c_{ij}$ , for each column $j$ . Line 5 initializes $c_{ij}$ to 0 as we start computing the sum given in equation$(1)$, and each iteration of the for loop of lines 6–7 adds in one more term of equation$(1)$.

Because each of the triply-nested for loops runs exactly $n$ iterations, and each execution of line 7 takes constant time, the SQUARE-MATRIX-MULTIPLY procedure takes $\Theta(n^3)$ time.





## Strassen algorithm

### Case 1

At fisrst, we assume that n is an exact power of 2 in each of the $n×n$ matrices.

#### Pseudo code

---

Suppose that we partition each of $A$, $B$, and $C$ into four $n/2 ×n/2$ matrices:
$$
A=\left[\matrix{A_{11} &A_{12} \\ A_{21}&A_{22} }\right],{\;}{\;}
B=\left[\matrix{B_{11} &B_{12} \\ B_{21}&B_{22} }\right],{\;}{\;}
C=\left[\matrix{C_{11} &C_{12} \\ C_{21}&C_{22} }\right]
$$
Create 10 matrix which is defined by 
$$
\begin{align}
&S_1=B_{12}-B_{22}\\
&S_2=A_{11}+A_{12}\\
&S_3=A_{21}+A_{22}\\
&S_4=B_{21}-B_{11}\\
&S_5=A_{11}+A_{22}\\
&S_6=B_{11}+B_{22}\\
&S_7=A_{12}-A_{22}\\
&S_8=B_{21}+B_{22}\\
&S_9=A_{11}-A_{21}\\
&S_{10}=B_{11}+B_{12}
\end{align}
$$
Method Strassen(A,B)
$n = A.rows$

$P_1=Strassen(A_{11},B_{12} − B_{22}) $
$P_2=Strassen(A_{11} + A_{12},B_{22}) $
$P_3=Strassen(A_{21} + A_{22},B_{11})$
$P_4=Strassen(A_{22},B_{21} − B_{11}) $
$P_5=Strassen(A_{11} + A_{22},B_{11} + B_{22}) $
$P_6=Strassen(A_{12} − A_{22},B_{21} + B_{22}) $
$P_7=Strassen(A_{11} − A_{21},B_{11} + B_{12}) $

let $C$ be a new $m\times n$ matrix
if $n==1$
    $c_{11}=a_{11}*b_{11}$
else partition $A$, $B$ and $C$ as above
    $C_{11}= P_5 + P_4 − P_2 + P_6 $
    $C_{12}= P_1 + P_2 $
    $C_{21}= P_3 + P_4 $
    $ C_{22}= P_1 + P_5 − P_3 − P_7 $
    $C=\left[\matrix{C_{11} &C_{12} \\ C_{21}&C_{22} }\right]$

return $C$ 

---



#### Proof

##### Step 1

First we assume that n is an exact power of 2 in each of the $n×n$ matrices.

We make this assumption because in each divide step, we will divide $n×n$ matrices into four $n/2 ×n/2$ matrices, and by assuming that $n$ is an exact power of 2, we are guaranteed that as long as $n\geq2$ , the dimension $n/2$ is an integer.

Suppose that we partition each of $A$, $B$, and $C$ into four $n/2 ×n/2$ matrices:
$$
A=\left[\matrix{A_{11} &A_{12} \\ A_{21}&A_{22} }\right],{\;}{\;}
B=\left[\matrix{B_{11} &B_{12} \\ B_{21}&B_{22} }\right],{\;}{\;}
C=\left[\matrix{C_{11} &C_{12} \\ C_{21}&C_{22} }\right]\tag{2}
$$
so that we can rewrite the equation $C=A\cdot B$ as
$$
\left[\matrix{C_{11} &C_{12} \\ C_{21}&C_{22} }\right]=
\left[\matrix{A_{11} &A_{12} \\ A_{21}&A_{22} }\right]\cdot
\left[\matrix{B_{11} &B_{12} \\ B_{21}&B_{22} }\right]\tag{3}
$$
The equation$(3)$ corresponds to the four equations
$$
C_{11}=A_{11}\cdot B_{11}+A_{12}\cdot B_{21}\tag{4}
$$

$$
C_{12}=A_{11}\cdot B_{12}+A_{12}\cdot B_{22}\tag{5}
$$

$$
C_{21}=A_{21}\cdot B_{11}+A_{12}\cdot B_{21}\tag{6}
$$

$$
C_{22}=A_{21}\cdot B_{12}+A_{22}\cdot B_{22}\tag{7}
$$

Each of these four equations specififies two multiplications of $n/2 ×n/2$ matrices and the addition of their$n/2 ×n/2$ produts.

This step take $\Theta (1)$ time by index calculation.

##### Step 2

Create 10 matrices $S_1,S_2,\cdots,S_{10}$, each of which is $n/2 ×n/2$ and is the sum or difference of two matrices created in step 1.

And the ten matrices are shown as follows:
$$
\begin{align}
&S_1=B_{12}-B_{22}\\
&S_2=A_{11}+A_{12}\\
&S_3=A_{21}+A_{22}\\
&S_4=B_{21}-B_{11}\\
&S_5=A_{11}+A_{22}\\
&S_6=B_{11}+B_{22}\\
&S_7=A_{12}-A_{22}\\
&S_8=B_{21}+B_{22}\\
&S_9=A_{11}-A_{21}\\
&S_{10}=B_{11}+B_{12}
\end{align}
$$
Since we need to add or subtract $n/2 ×n/2$ matrices 10 times, this step does indeed take $n/2 ×n/2$ time.

##### Step 3

Using the submatrices created in step 1 and the 10 matrices created in step 2, recursively compute seven matrix products $P_1, P_2,\cdots,P_7$. Each matrix $P_i$ is $n/2 ×n/2$.

And the seven matrices are shown as follows:
$$
P_1=A_{11}\cdot S_1=A_{11}\cdot B_{12}-A_{11}\cdot B_{22} \\
P_2=S_2\cdot B_{22}=A_{11}\cdot B_{22}+A_{12}\cdot B_{22} \\
P_3=S_3\cdot B_{11}=A_{21}\cdot B_{11}+A_{22}\cdot B_{11} \\
P_4=A_{22}\cdot S_4=A_{22}\cdot B_{21}-A_{22}\cdot B_{11} \\
P_5=S_5\cdot S_6=A_{11}\cdot B_{11}+A_{11}\cdot B_{22}+A_{22}\cdot B_{11}+A_{22}\cdot B_{22} \\
P_6=S_7\cdot S_8=A_{12}\cdot B_{21}+A_{12}\cdot B_{22}-A_{22}\cdot B_{21}-A_{22}\cdot B_{22} \\
P_7=S_9\cdot S_{10}=A_{11}\cdot B_{11}+A_{11}\cdot B_{12}-A_{21}\cdot B_{11}-A_{21}\cdot B_{12}
$$

##### Step 4

Compute the desired submatrices $C_{11}, C_{12}, C_{21}, C_{22}$ of the result matrix $C$ by adding and subtracting various combinations of the $P_i$ matrices. We can compute all four submatrices in $\Theta(n^2)$ time.

The calculation process is shown as follows
$$
\begin{align}
C_{11}&=A_{11}\cdot B_{11}+A_{12}\cdot B_{21}\\
&=(A_{11}\cdot B_{11}+A_{11}\cdot B_{22}+A_{22}\cdot B_{11}+A_{22}\cdot B_{22})+(A_{22}\cdot B_{21}-A_{22}\cdot B_{11})\\
&{\;}{\;}{\;}{\;}-(A_{11}\cdot B_{22}+A_{12}\cdot B_{22})+(A_{12}\cdot B_{21}+A_{12}\cdot B_{22}-A_{22}\cdot B_{21}-A_{22}\cdot B_{22})\\
&=P_5+P_4-P_2+P_6
\end{align}
$$

$$
\begin{align}
C_{22}&=A_{21}\cdot B_{12}+A_{22}\cdot B_{22}\\
&=(A_{11}\cdot B_{11}+A_{11}\cdot B_{22}+A_{22}\cdot B_{11}+A_{22}\cdot B_{22})+(A_{11}\cdot B_{12}-A_{11}\cdot B_{22})\\
&{\;}{\;}{\;}{\;}-(A_{21}\cdot B_{11}+A_{22}\cdot B_{11})-(A_{11}\cdot B_{11}+A_{11}\cdot B_{12}-A_{21}\cdot B_{11}-A_{21}\cdot B_{12})\\
&=P_5+P_1-P_3-P_7
\end{align}
$$

$$
\begin{align}
C_{12}&=A_{11}\cdot B_{12}+A_{12}\cdot B_{22}\\
&=(A_{11}\cdot B_{12}-A_{11}\cdot B_{22})+(A_{11}\cdot B_{22}+A_{12}\cdot B_{22})\\
&=P_1+P_2
\end{align}
$$

$$
\begin{align}
C_{21}&=A_{21}\cdot B_{11}+A_{12}\cdot B_{21}\\
&=(A_{21}\cdot B_{11}+A_{22}\cdot B_{11})+(A_{22}\cdot B_{21}-A_{22}\cdot B_{11})\\
&=P_3+P_4
\end{align}
$$

Altogether, we add or subtract $n/2 ×n/2$ matrices eight times in step 4, and so this step indeed take $\Theta(n^2)$ time.

##### Conclusion 

Now we already have enough information to set up a recurrence for the running time of Strassen’s method. Let us

assume that once the matrix size n gets down to 1, we perform a simple scalar multiplication.

When $n > 1$, steps 1, 2, and 4 take a total of $\Theta(n^2)$ time, and step 3 requires us to perform seven multiplications of $n/2 ×n/2$ matrices. Hence, we obtain the following recurrence for the running time $T(n)$ of Strassen’s algorithm:
$$
T(n)=\begin{equation}
\begin{cases}
\Theta(1) & n=1 \\
7T(n/2)+\Theta(n^2) & n>1 
\end{cases}
\end{equation}\tag{8}
$$
Then by the master method

Since $a=7,b=2,f(n)=\Theta(n^2)$, and $n^{log_b^a}=n^{log_2 7}$, Rewriting $log_27$ as $lg 7$ and recalling that $2.80 < lg 7 < 2.81$, we see that $f(n)=O(n^{lg7-\varepsilon})$ for $\varepsilon=0.8$.

Thus, case 1 applies, and we have the solution $T(n)=\Theta(n^{lg7})$.





### Case 2

Then we consider the condition that n is any positive integer

#### Pseudo code

---

Suppose that $A,B$ has $n$ rows, and n satisfy that $2^m - c = n$, and $2^m>n>2^{(m-1)}$.

Then we constuct matrix $A' $and$B'$, which $A', B'$ has $2^m$ rows,
$$
A'=\left[\matrix{A &0 \\ 0&0 }\right],{\;}{\;}
B'=\left[\matrix{B &0 \\ 0&0 }\right]{\;}{\;}
$$
create 10 matrix which is defined by 
$$
\begin{align}
&S_1=B'_{12}-B'_{22}\\
&S_2=A'_{11}+A'_{12}\\
&S_3=A'_{21}+A'_{22}\\
&S_4=B'_{21}-B'_{11}\\
&S_5=A'_{11}+A'_{22}\\
&S_6=B'_{11}+B'_{22}\\
&S_7=A'_{12}-A'_{22}\\
&S_8=B'_{21}+B'_{22}\\
&S_9=A'_{11}-A'_{21}\\
&S_{10}=B'_{11}+B'_{12}
\end{align}
$$
Method Strassen($A'$ , $B'$)
$n = A'.rows$

$P_1=Strassen(A'_{11},B'_{12} − B'_{22}) $
$P_2=Strassen(A'_{11} + A'_{12},B'_{22}) $
$P_3=Strassen(A'_{21} + A'_{22},B'_{11})$
$P_4=Strassen(A'_{22},B'_{21} − B'_{11}) $
$P_5=Strassen(A'_{11} + A'_{22},B'_{11} + B'_{22}) $
$P_6=Strassen(A'_{12} − A'_{22},B'_{21} + B'_{22}) $

let $C'$ be a new $(2^m)\times(2^m)$ matrix
if $m==1$
    $c_{11}=a_{11}*b_{11}$
else partition $A, B$ and $C$ as above
    $C'_{11}= P_{5} + P_{4} − P_{2} + P_{6} $
    $C'_{12}= P_{1} + P_{2} $
    $C'_{21}= P_{3} + P_{4} $
    $ C'_{22}= P_{1} + P_{5} − P_{3} − P_{7} $
    for $i = 1$ to $n $
        for $j = 1$ to $n $
            $c_{ij} = c'_{ij}$
return $C $

---

#### Proof 

Suppose that $A$ ,$B$ has $n$ rows, and n satisfy that $2^m - c = n$, and $2^m>n>2^{(m-1)}$.

Then we constuct matrix $A' $and $B'$, which $A', B'$ has $2^m$ rows,
$$
A'=\left[\matrix{A &0 \\ 0&0 }\right],{\;}{\;}
B'=\left[\matrix{B &0 \\ 0&0 }\right]{\;}{\;}
$$
By the multiplication principle of partitioned matrices, we have
$$
C'=A'\cdot B'=
\left[\matrix{A &0 \\ 0&0 }\right]\cdot \left[\matrix{B &0 \\ 0&0 }\right]= \left[\matrix{C &0 \\ 0&0 }\right]
$$
where $C'$ has $2^m$ rows and $C$ has $n$ rows.

Since the construction of $A'$ and $B'$, tranformation from $C'$ to $C$ only take $\Theta(1)$ times, thus the time of computing $C$ and $C'$ is approximately same, we only need to consider the time of computing $C'$.

Since we only need to compute the nonzero term, thus 

Then consider the time of every step in the proof of case 1.

In step 1, still need to take $\Theta(1)$ time.

In step 2, we need to add or subtract $2^{m-1} ×2^{m-1}$ matrices 10 times, since every $2^{m-1} ×2^{m-1}$ only contain 

In step 3, we 

In step 4





# Part 2 Approach, result  and analysis of the experiments

**Note: All parts below we use both python and Java language to write our methods and test them.**

##   Unimproved method 

​		Firstly, we write the standard square matrix multiply method and Strassen's algorithm directly according to our pseudo code as python code.  And then we perform two tests: the one  use  10 matrices whose size is from n=1 to n=1000(For higher efficiency, we set the size interval as 100, which means we test matrices size: 1, 101, 201...901) to test the two algorithms' time complexity,  the other use 100 matrices whose size is from n=1 to n=100(interval 1) .  The running time data are show as figure 1.

![图片17](https://tva1.sinaimg.cn/large/008i3skNgy1gqxl93t9odj30hs0dcwet.jpg)

```
figure 1a: running time of two methods in python, size:1 to 1000, interval=100.
```

![图片18](https://tva1.sinaimg.cn/large/008i3skNgy1gqxla9huwfj30hs0dcjrm.jpg)

```
figure 1b: running time of two methods in python, size:1 to 100, interval = 1
```

### 	Results

From these two figure we get three observation result:  

1. figure 1a shows that from size n=1 to n=1000, Stranssen's algorithm take more time than square-matrix multiplication algorithm and around some size values the time required by the Strassen's method will jump up.  

2. figure 1b shows  details of the time jump and we find that in this size value range the cost time jump at about n=16, 32, 64. All  are approach to 2^n^ .

3. figure 1b shows another characteristic: the running time will slightly decrease during the two time jump, such as the time line between 32 and 64.

### Analysis

For result 1: Strassen's algorithm  need to perform recursive operation to decompose the matrix, in this process a large number of dynamic two-dimensional arrays needed to be created and preserved by JVM and python interpreter, in which allocating heap memory space will take up a lot of time.

So when the matrix gets larger, compared with addition and multiplication operations, allocating heap memory space will cost more time. so Strassen method cost more time than standard method, which is not as we analyzed before.

For result 2 and 3: When calculating matrices with size between n = 2^k^  to n = 2^k+1^ , Stressen's algorithm will supplement 0 to the matrix until its size is n'=2^(k+1)^. So the running time of matrices with size from n = 2^k^ + 1 to n = 2^k+1^ -1 will be almost equal and will jump up up at n = 2^k+1^ . What's more, the operations of supplement 0 also cost time and Stressen's algorithm will supplement less 0 into the matrix as the matrices' size is more appropriate the next 2^n^, which means it will cost less time at supplementing 0. Since all matrices with size in the (2^n^, 2^n+1^) range will almost cost the the same time for  addition and multiplication operation and the time for supplementing 0 will decrease with the matrix size increasing, the total running time of running the matrices will slightly decreasing in the  (2^n^, 2^n+1^) range.







## Improvement 1

One dimensional arrays

since the mathematical expression of the matrix, we wanted to two dimensional arrays to store the matrices naturally. But we consulting  articles and find that one dimensional array will cost less store space. From the last result, we find that recursive operation in Strassen's algorithm requires tcreating a large number of dynamic two-dimensional arrays, in which the allocation of heap memory space will take up a lot of computing time. Considering that when storing the same size of data, two-dimensional arrays take up much more memory than one-dimensional arrays, we choose one-dimensional array to store the matrix during the calculating process.



![图片19](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlbflazij307y0370so.jpg)



![图片32](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlq8w1suj30c803ejrd.jpg)



## Improvement 2

Lower bound optimization method

### Basic idea:

The implementation of strassen requires recursion. Recursion is implemented by calling the function itself. Each recursive call to the function does address saving, parameter passing, etc. This is implemented through a recursive working stack, and this process will takes up a lot of memory.

The more times we recurse, the more additional stack and heap processing is required, and the more memory is consumed. So we can set a boundary, when n is less than this bound, using standard matrix multiplication to compute the matrix without continuing divide-and-conquer recursion, which push many stuff into function stack.

In this improvement, we set a series of lower bound (16, 32, 64, and 128) for the Strassen's algorithm,  and test them with matrix with size n=1 to n=450 in both Java and python. And the running data are show as figure.

### part 1:

![图片20](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlci3ak4j30j20egaby.jpg)

```
Figure 2a.Observation of python 
```



![图片21](https://tva1.sinaimg.cn/large/008i3skNgy1gqxld5f8ejj30ju0ek75k.jpg)

```
Figure 2b.Observtion of Java
```

#### 	Analysis: 

​	From this figure, the strassen algorithm cost too much time when n is large. So, we optimize it using the lower bound optimization method.

​	An interesting observation here is that the jump is lower then raw Strassen method, and the line become more smooth. We guess it is because the zeros we need to append is not that much(to the next 2^n). For example, using a boundary of 32 for this method and test a n=120 matrix, the divide process is : 120 -> 60 ->30(which is lower than 32) -> direct compute with standard algorithm.

​	So we no need to append zeros for the n=120 case anymore, think about when n is large, it could save us a lot of time(like from 1024 to 2048).

### part 2:

 For further observe the detail information and the comparison   between improved Strassen's algorithm with different bound, we eliminate the unimproved Stassen's algorithm line.

![图片22](https://tva1.sinaimg.cn/large/008i3skNgy1gqxldtuw2ij30lu0gead0.jpg)

```
Figure 2c.Observation of python of different lower bound.
```

![图片23](https://tva1.sinaimg.cn/large/008i3skNgy1gqxleambq8j30ly0gg769.jpg)

```
Figure 2d.Observtion of Java
```

#### 	Results:

 From the examination, we found that the best lower bound for Python is 32, the best lower bound for Java is 128.

when observing the figure 2d, we noticed that all line have a  turning point at about n = 1500, which is contradicts what we've seen before that the running time will slightly decrease during the two time jump.

#### 	Analysis:

After we looked at it carefully, we found that this was caused by the test matrices size interval. We set the interval as 500 in this test, and 2^10^ =1024 are between the two test matrices size 1000 and 1500. The running time should jump at 1024 and then slightly decreasing as matrix size approach 2048, but we do not test the running time at 1024. So there will be abnormal inflection points in data fitting line. If we set a smaller interval, the fitting curve will be closer to the true value.(as the red dotted line show in figure需要作图).

## Improvement 3: Multi-Processing

### Basic idea:

​	Thread is the smallest unit of operation scheduling that an operating system can perform. It is contained within the process and is the actual operating unit within the process. A thread refers to a single sequential flow of control in a process. A process can have multiple threads concurrently, each of which performs different tasks in parallel. Multi-threading works by making the CPU switch between different threads to perform the computation, which can be used to reduce the idle CPU resources caused by blocking.

![图片24](https://tva1.sinaimg.cn/large/008i3skNgy1gqxley2qh5j30xg0imwfr.jpg)

```
Figure 3a.Just use 8 multi-process by for 8 sub-multiply operations(using strassen2 for the 8 mutily) 
```

​	In matrix multiplication, we need to multiply multiple sub-matrices, then we can split it up into multiple threads and run it in parallel. If we divide the matrix into four parts, and using the multiple threads, then the the time is closed to ($\frac{n}{2}$)^2.8^.

### 	part 1

​	So we write raw Strassen's algorithm with multiprocessing  and lower bound Strassen's algorithm in python, and test them with randomly generated matrices whose size is up to n=1000 and n = 450. The running time are show as figure 3b and 3c.

![图片25](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlfhnz4fj30hs0dcwf2.jpg)



```
Figure 3b.Raw Strassen's algorithm with multiprocessing 
```

![图片26](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlg01t7rj30fk0bcaas.jpg)



```
Figure 3c. Lower bound Strassen's algorithm with multy-processing.
```

#### Analysis

Figure 3b shows that only using multi-processing is not enough, because it do not solve the recursive variables and function stack accumulation at all. And it just is constant faster than the raw Strassen's algorithm.

Figure 3c shows that using multiprocessing is much more faster than only using the lower bound. However, notice that at the beginning, the Multi-Processing method is not very good and slower than lower Bound 32, this is because it takes some time to generate processes.

### Part 2:

So we test the multi-processing method with different lower-bound and the running time are showed bolow. 

![图片27](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlgi8k5ej30hs0dcwfq.jpg)

```
Figure 3d. Multi-processing method with different lower-bound, standard and raw strassen's algorithm
```

![图片28](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlgzh6zvj30hs0dc0u9.jpg)

```
Figure 3e.Multi-processing method with different lower-bound and standard(with without raw strassen's algorithm)
```

![图片29](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlh9se0oj30hs0dcmyh.jpg)

```
Figure 3f. MultiProcessing method with lowerBound 6 and 32.
```

![图片30](https://tva1.sinaimg.cn/large/008i3skNgy1gqxlhpc48uj30o60hyq4r.jpg)

```
Figure 3g. The crosspoint of Standard method and multi-processing method with 32 as lower bound.
```

![图片31](https://tva1.sinaimg.cn/large/008i3skNgy1gqxljesb1jj30hs0dcaah.jpg)



#### Analysis

From the figure 3d to 3f, we could find that the best lower bound for the multi-processing method in python is 32.

Then we test for the Standard method and multi-processing method with 32 as lower bound to find the threshold and complete the adapted method.







# Part 3 Threshold

Next, let's analyse the threshold in Python

From part 3, we determined the two optimal algorithms for Python:

One is the strassen algorithm using lower bound of 6 and multi-threading and the other one is Strassen algorithm using lower bound of 32 and multi-threading.

And this is the figure about the execution time of two optimal algorithms for Python.

![图片7](https://tva1.sinaimg.cn/large/008i3skNgy1gqxbb2409uj30o60hygnm.jpg)

Since we want to find the threshold in Python.

So we add the curve of standard matrix multiplicationdd the standard matrix square algorithm, and based on the optimal optimization algorithm to find the threshold.

![图片8](https://tva1.sinaimg.cn/large/008i3skNgy1gqxb804gyvj30ps0j6go8.jpg)

Finally, we get the adapted figure.

![图片9](https://tva1.sinaimg.cn/large/008i3skNgy1gqxbrj1xftj30q00jsjst.jpg)







Similarly, we analyse the threshold in Java

![图片15](https://tva1.sinaimg.cn/large/008i3skNgy1gqxht9a83xj30oy0iyada.jpg)

After optimizing strassen algorithm, we run the code to find threshold of which strassen algorithm is faster than standard matrix multiplication.

And we find that if $n < 400$, there is no algorithm faster than standard algorithm.



![图片16](https://tva1.sinaimg.cn/large/008i3skNgy1gqxhtm62v4j30qk0k6q4y.jpg)

For this reason, we choose the most efficitive one which lower bound is 64 to find the threshold.

In this picture, we can easily find that the threshold is larger than 850 and smllar than 1000.



# Part 4 Some interesting facts

## Print time

We find that print in the recursion significantly influence the execution time.

![图片10](https://tva1.sinaimg.cn/large/008i3skNgy1gqxh9fm6sjj30ju02fwel.jpg)

We just add a print here and it shows that it runs a lot of print in the recursive Strassen method.

![图片11](https://tva1.sinaimg.cn/large/008i3skNgy1gqxhahx9nwj307407hmx2.jpg)

![图片12](https://tva1.sinaimg.cn/large/008i3skNgy1gqxhcb0g4vj30hs0dct91.jpg)

~~~
figure 1: some data in the print result
figure 2: execution time of two strassen algorithms with print or without print
~~~



Just look at the execution time graph here, it apparently is a disaster adding not necessary lines in a recursive method, let along print need to interact with io, which take a lot of time.



## Compute is sleep

![图片13](https://tva1.sinaimg.cn/large/008i3skNgy1gqxhdwn3t4j30hs0dcaag.jpg)

~~~
figure: execution time of different algorithms in Python
~~~



When I got this graph, I was shocked about this result.

I tried to analyze it from algorithm at first, but i can not find any materials to explain this condition. And then I try to analyze this result in the aspect of compile language, but still come to nothing.

When I felt desperate and wanted to give up understanding this figure, I found that my partner had experienced simiar conditions in the Java, and his computer was sleeping when he got the same result, I realize that sleep would lower the computation of program, thus it need more time to calculate the data, and here was the funny result.



## GIL problem

### Introduction of two models

At first, we need to introduce two modules in Python:

1. Process: An execution of a program (the program is loaded into memory and the system allocates resources to run). Each process has its own memory space, data stack, etc. Processes can communicate with each other, but cannot share information.

2. Thread: All threads run in the same process and share the same runtime environment. Each individual thread has a program entry, sequential execution sequence, and program exit.

Thread execution can be commandeered, interrupted, or temporarily suspended (sleeping) to allow other threads to run. Each thread in a process shares the same data space.



Now we analyse the problem we count.

According to the theoretical analysis in part 3,  we think the execution time should be shorten after the optimization of multi-processing. 

But in fact we find that the algorithm optimized for multithreading actually takes longer to run than standard matrix multiplication.

### Data 

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gqxahh9lfkj30hs0dcq3k.jpg" alt="图片3" style="zoom:150%;" />

~~~
figure: execution time of different algorithms:
1. 
2. 
3. standard matrix multiplication algorithm
~~~

### Explanation 

Aftering some investigation and research, we find that the cause of the problem is the GIL of Python:

GIL stands for Global Interpreter Lock, is a decision made by Python at design time for data security. And in Python, each thread needs to fetch a GIL to execute code.

Then next figure explain the operation mechanism of GIL



![2-1ZS012105L23](https://tva1.sinaimg.cn/large/008i3skNgy1gqxjezh15jg30fa05f74b.gif)

~~~
figure: explaining how the GIL works
~~~



The above figure is an example of GIL in action in a Python program. Thread 1, 2, and 3 take turns to execute, and each thread will lock GIL at the beginning of execution to prevent other threads from executing. Similarly, after each thread finishes executing a segment, it releases the GIL to allow other threads to start using the resource.

Thus we can konw that when an interpreter executes Python code, it restricts thread access to the shared resource until the interpreter encounters an I/O operation or a certain number of operations.

So, while CPython's threading library directly encapsulates the system's native threads, CPython as a whole is a process, with only one thread getting a GIL running at any one time, while the other threads are waiting. This results in the fact that even in multicore CPUs, multithreading only switches between time sharing operations.

Thus, we can get two obvious conclusions in Python:

1. Mult-threading: using one CPU for all the threads created, slower for creating threads.
2. Multiprocessing: using enough CPU to run all the process created.

The Multiprocessing library compensates inefficiency of the Thread library for the GIL. Multiprocessing library uses multiple processes instead of multiple threads. Each process has its own separate GIL and they can run at the same time.

## Comparsion of Java and Python

From above, we found optimization algorithms in the Java language and Python language respectively and we have got the different thresholds of Java language and Python language.

We found that different compile languages affect the speed of the execution and the choice of threshold.

Additionally we wanted to compare the speed of the two languages and explore the deeper reasons.

### Data 

![图片6](https://tva1.sinaimg.cn/large/008i3skNgy1gqxb2qg3oej30su0m2adh.jpg)

~~~
figure: execution time of four different algorithms
1. 
2.
3.
4.
~~~

### Explanation 

From the above figure, we can find that the speed of execution in Java is more large than Python.

We find that there are some reasons for this condition:

1. Python is GIL (Global Interpreter Lock)
2. Python is an interpreted language, not a compiled language

3. Java is precompiled to build and written into machine language.

4. Python is executed by the interpreter, which interprets it line by line.

## Some operations in C++

Since we want to compare the execution speed of different compile languages, so we also try some matrix operations in C++.

### Data 

![图片1](https://tva1.sinaimg.cn/large/008i3skNgy1gqxb49km6wj30hs0dcmxf.jpg)

~~~
figure: execution time of standard matrix multiplication algorithm in C++
~~~

### Explanation 

From the figure, we can find that C is more quick than Python and Java. 

There are two main reasons.

1. C is a compiled language, while Java is a semi-compiled, semi-interpreted language
2. C will be precompiled into precompiled files, and then compiled into assembly language, binary files, which can deal with the machine directly

Finally, we want to konw the limit of speed of computing the matrix multiplication. 

Thus, we try to test the execution time of the power by openBLAS, which is one of the fastest way to execute the matrix multiplication.

### Data 

![图片5](https://tva1.sinaimg.cn/large/008i3skNgy1gqxb450ratj30hs0dcaab.jpg)

~~~
figure: execution time of OpenBLAS in C++
~~~



### Introduction of OpenBLAS

Mathematics is the foundation of science, and generally the items that involve algorithms are broken down to basic scientific calculations: single numbers, arrays, operations between matrices of various dimensions. 

BLAS is a standard mathematical computation library that defines an API for manipulation of matrix arrays. BLAS is an application program interface (API) standard for publishing numerical libraries for basic linear algebra operations. OpenBLAS is a concrete implementation of BLAS standard.

OpenBlas is an optimized BLAS computing library published under the BSD license (open source), which is an open source matrix computing library and contains a lot of matrix calculation algorithm with different precision and forms.


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

# Finished in 5.26
Pre is not as well as expected\
Results is good\
English presentation need to be improved
