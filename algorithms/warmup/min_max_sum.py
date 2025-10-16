"""
Problem: Mini-Max Sum
URL: https://www.hackerrank.com/challenges/mini-max-sum/problem
Difficulty: Easy
Category: Warmup

Description:
Given five positive integers, find the minimum and maximum values that can be calculated
by summing exactly four of the five integers. Then print the respective minimum and
maximum values as a single line of two space-separated long integers.

Input Format:
A single line of five space-separated integers.

Constraints:
1 ≤ arr[i] ≤ 10^9

Output Format:
Print two space-separated integers on one line:
- The minimum sum (sum of 4 smallest numbers)
- The maximum sum (sum of 4 largest numbers)

Note:
The output can be greater than a 32-bit integer, so use appropriate data types.
Beware of integer overflow!

Example:
Input:
1 2 3 4 5

Array: [1, 2, 3, 4, 5]

Possible sums of 4 elements:
- Sum everything except 1: 2 + 3 + 4 + 5 = 14
- Sum everything except 2: 1 + 3 + 4 + 5 = 13
- Sum everything except 3: 1 + 2 + 4 + 5 = 12
- Sum everything except 4: 1 + 2 + 3 + 5 = 11
- Sum everything except 5: 1 + 2 + 3 + 4 = 10

Minimum sum: 10 (exclude the largest number, 5)
Maximum sum: 14 (exclude the smallest number, 1)

Output:
10 14

Example 2:
Input:
1 3 5 7 9

Minimum sum: 1 + 3 + 5 + 7 = 16
Maximum sum: 3 + 5 + 7 + 9 = 24

Output:
16 24

Approach:
1. get the sum of the numbers
2. get the min and max of the numbers
3. get max and min sum minus plus max and min
"""


def miniMaxSum(arr):
    """
    Calculate and print the minimum and maximum sums of 4 out of 5 integers.

    Args:
        arr (List[int]): Array of exactly 5 integers

    Returns:
        None: Prints two space-separated integers (min_sum and max_sum)
    """
    max_sum = sum(arr) - min(arr)
    min_sum = sum(arr) - max(arr)
    print(min_sum, max_sum)

    pass


if __name__ == '__main__':
    # Read the array of 5 integers
    arr = list(map(int, input().rstrip().split()))
    # Call the function
    miniMaxSum(arr)