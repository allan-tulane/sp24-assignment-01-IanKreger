

# CMPS 2200 Assignment 1

**Name:**___Ian Kreger______________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes because there is a constant c that can be multiplied to $2^{n+1}. 2^(n+1) is the same as 2^n * 2 which is \in O(2^n)$. 
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No. $2^{2^n} grows much faster than 2^n. There is no constant c that can be multiplied to 2^n that will equal 2^2^n when n is a large value.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No. The limit when n is approaching infinity of $n^{1.01}/(\mathrm{log}^2n) is infinity which shows that $n^{1.01} grows faster that \mathrm{log}^2 n at high n values. 
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes. It is the same reason as in part C. $n^{1.01} grows faster than \mathrm{log}^2 n at high n values. 
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No. As n increase in value the square root of n will grow faster than (\mathrm{log} n)^3
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes it is the same reason as in part E. At some point the square root function will be grow faster than the (\mathrm{log} n)^3.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function calculates the fibonnaci number for the given term x. If x is 6 it gives the 6 term in the fibonnaci sequence. This function recursively calls and adds (x-1) and (x-2). This function continues to use recursion until x is either 1 or 0 in which the function returns itself, which will be 1 or 0. The result is the fibonnaci number that corresponds with the term x.
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work is O(n) and the span is also O(n). The work is O(n) because the function iterates a loop one time. The worst outcome for span is the sequence is the whole list which is O(n)
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  The work is O(n) and the span is O(log n)
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  
 
.  Work and span did not change. Work is still O(n) and span is still O(log n)
.  
.  
.  
.  
.  
.  
.  

