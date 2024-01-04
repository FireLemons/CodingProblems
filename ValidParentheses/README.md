# Valid Parentheses
## Problem
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3  
Output: `["((()))","(()())","(())()","()(())","()()()"]`

Example 2:

Input: n = 1  
Output: `["()"]`

## Running
Python 3 must be installed.

In a unix environment cd where this readme is and run `./valid_parentheses.py <n>`.  
For example: `./valid_parentheses.py 6`

## Results
```
time ./valid_parentheses_binary_sequence.py 15
9694845

real	0m38.504s
user	0m37.704s
sys	0m0.740s

time ./valid_parentheses_tree_traversal.py 15
9694845

real	1m1.467s
user	1m0.651s
sys	0m0.768s

time ./valid_parentheses_binary_sequence_custom_hamming.py 15
9694845

real	0m47.333s
user	0m46.543s
sys	0m0.776s
