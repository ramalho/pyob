# The 8 Queens Problem

This directory contains Object-Oriented solutions to the 8 Queens Problem, ported from examples in chapter 6 of Tim Budd's *Introduction to Object-Oriented Programming, 3e* (Addison-Wesley, 2002).

The key characteristic of these examples is that there is no central control. Each queen is assigned to a column, and moves in its column searching for a row where it cannot be attacked by any other queen. When it cannot find a safe row, it asks its neighboring queen to move and starts over. This produces the backtracking behavior that makes the 8 Queens problem famous in computing.

Here are notes about each of the programs in this directory.

## `queens.py`

This is the implementation to study first. If executed without arguments, it computes and displays a solution with 8 Queens:

```bash
$ python3 queens.py 
[(1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 3)]
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ ♛ │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │ ♛ │   │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │ ♛ │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │ ♛ │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │ ♛ │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │ ♛ │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │ ♛ │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │ ♛ │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┘
```

>  **Note:** the grid may or may not appear jagged, depending on the width of the BLACK CHESS QUEEN Unicode character (U+265B) in the display font. If it is jagged on your machine, change the value of `queen` in the first line of the `draw_row` function.

You may provide an integer argument to see a solution for a different number of queens. For example, `10`:

```bash
$ python3 queens.py 10
[(1, 1), (2, 8), (3, 2), (4, 9), (5, 6), (6, 3), (7, 10), (8, 4), (9, 7), (10, 5)]
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ ♛ │   │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │ ♛ │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │ ♛ │   │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │ ♛ │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │ ♛ │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │ ♛ │   │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │   │   │   │ ♛ │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │ ♛ │   │   │   │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │   │   │ ♛ │   │   │   │
├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
│   │   │   │   │ ♛ │   │   │   │   │   │
└───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
```

Because all queens start in row 1, and all move in the same way, the solution presented for each number of queens is always the same.

Interestingly, running `queens.py` with 14 queens raises `RecursionError` (using Python's default recursion limit of 1000), but with 15 queens there's no problem. This is due to the backtracking behavior of the queens, which is sensitive to the order in which they search for a safe a square in their columns.

## `queens_and_guard.py`

The `queens_and_guard.py` version uses a `Guard` instance as a sentinel: it is the neighbor of the first `Queen`. The `Guard` class implements three methods with simple hard-coded responses. This leverages polymorphism to avoid several checks that `queens.py` uses to handle the special case of the first `Queen`, which has no royal neighbor.

## `random_queens_and_guard.py`

In this implementation, each `Queen` moves back and forth through a random but fixed sequence of rows, so each run can produce a different solution. For example, it is known that for 8 queens there are 92 solutions, but with 4 queens there are only 2.

Because of the backtracking nature of the algorithm, different sequences of moves can produce more or less recursive calls. Starting with 10 queens, some runs do not conclude because Python raises a `RecursionError` (using the default recursion limit of 1000). 

## `drive_random_queens.py`

This script calls the `solve` function of the `random_queens_and_guard.py` module 500 times for each value of N Queens from 8 to 20. Each call either produces a solution or raises `RecursionError`. The succesful calls are counted and displayed as a percentage. This is a sample run, which took about 95 seconds on a Core i7 machine:

```bash
$ time python3 drive_random_queens.py 
 8: 100.0%
 9: 100.0%
10: 100.0%
11:  98.8%
12:  99.2%
13:  99.0%
14:  94.4%
15:  94.4%
16:  89.6%
17:  85.6%
18:  83.6%
19:  77.6%
20:  74.8%

real	1m34.955s
user	1m34.735s
sys	0m0.040s
```

In the example above, 100% of the attempts with 10 queens were successful, but for 20 queens the success rate was 74.8% — meaning that 25.2% of the calls hit Python's recursion limit and did not complete.

The table below shows results for 5 runs of `drive_random_queens.py`, demonstrating that most of the time `random_queens_and_guard.py` can solve for 10 queens, but sometimes it fails.


|   N   | run 1 | run 2 | run 3 | run 4 | run 5 |
|  ---: |  ---: |  ---: |  ---: |  ---: |  ---: |
|  **8**| 100.0%| 100.0%| 100.0%| 100.0%| 100.0%|
|  **9**| 100.0%| 100.0%| 100.0%| 100.0%| 100.0%|
| **10**| 100.0%| 100.0%| 100.0%| 100.0%|  99.8%|
| **11**| 100.0%|  99.6%|  99.4%|  98.0%|  99.2%|
| **12**|  99.2%|  99.4%|  99.0%|  99.4%|  99.6%|
| **13**|  98.2%|  98.6%|  97.8%|  98.2%|  98.8%|
| **14**|  96.2%|  96.6%|  95.8%|  95.8%|  96.0%|
| **15**|  95.4%|  96.0%|  94.4%|  92.2%|  95.4%|
| **16**|  92.8%|  90.2%|  91.6%|  90.8%|  92.2%|
| **17**|  85.4%|  88.4%|  88.8%|  86.6%|  88.6%|
| **18**|  85.2%|  84.6%|  83.0%|  85.4%|  82.2%|
| **19**|  76.4%|  76.2%|  82.0%|  77.6%|  78.2%|
| **20**|  73.6%|  70.0%|  74.0%|  76.8%|  72.6%|
