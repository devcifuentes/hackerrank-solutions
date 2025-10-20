"""
Problem: Solve Me First
URL: https://www.hackerrank.com/challenges/solve-me-first/problem
Difficulty: Easy
Category: Warmup

Description:
Complete the function solveMeFirst to compute the sum of two integers.

Input Format:
Two integers, a and b.

Constraints:
1 ≤ a, b ≤ 1000

Output Format:
Return the sum of the two integers.

Example:
Input: a = 7, b = 3
Output: 10

Approach:
Simple addition of two integers. No special algorithm needed.

MaxScore:1
"""


def solveMeFirst(a, b):
    """
    Function to compute the sum of two integers more tahn 0 less than 1000.


    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: Sum of a and b
        error: If a and b are less than 0 or more than 1000

    Score obtained: 1
    """
    if (a < 0) or (b < 0) or (a > 100 or b > 100):
        error = "Invalid data"
        return error
    return a + b


if __name__ == '__main__':
    # Read input values
    num1 = int(input())
    num2 = int(input())

    # Calculate and print the result
    res = solveMeFirst(num1, num2)
    print(res)
