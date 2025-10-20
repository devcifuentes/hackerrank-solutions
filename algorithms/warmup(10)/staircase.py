"""
Problem: Staircase
URL: https://www.hackerrank.com/challenges/staircase/problem
Difficulty: Easy
Category: Warmup

Description:
Write a program that prints a staircase of size n using # symbols and spaces.
The staircase is right-aligned, which means:
- Its base and height are both equal to n
- The last line is not preceded by any spaces
- All lines are right-aligned

Input Format:
A single integer, n, denoting the size of the staircase.

Constraints:
0 < n ≤ 100

Output Format:
Print a staircase of size n using # symbols and spaces.
Note: The last line must have 0 spaces in it.

Example:
Input:
6

Output:
     #
    ##
   ###
  ####
 #####
######

Explanation:
The staircase is right-aligned, composed of # symbols and spaces,
and has a height and width of n = 6.

Line 1: 5 spaces + 1 hash
Line 2: 4 spaces + 2 hashes
Line 3: 3 spaces + 3 hashes
Line 4: 2 spaces + 4 hashes
Line 5: 1 space  + 5 hashes
Line 6: 0 spaces + 6 hashes


Approach:
1. Get n to set de heigth and base
2. loop # to n lines with replace function (n - i)
"""


def staircase(n):
    """
    Print a staircase of size n.

    Args:
        n (int): The size of the staircase

    Returns:
        None: Prints the staircase pattern
    """
    short = '#' * n

    for i in range(n):
        step = short.replace('#', ' ', n - i - 1)
        print(step)


if __name__ == '__main__':
    # Read the size of the staircase
    n = int(input().strip())
    # Call the function
    staircase(n)
