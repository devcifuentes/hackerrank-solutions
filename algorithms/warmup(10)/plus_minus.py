"""
Problem: Plus Minus
URL: https://www.hackerrank.com/challenges/plus-minus/problem
Difficulty: Easy
Category: Warmup

Description:
Given an array of integers, calculate the ratios of its elements that are positive, negative,
and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal
places, though answers with absolute error of up to 10^-4 are acceptable.

Input Format:
The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].

Constraints:
0 < n ≤ 100
-100 ≤ arr[i] ≤ 100

Output Format:
Print the following 3 lines, each to 6 decimals:
1. Proportion of positive values
2. Proportion of negative values
3. Proportion of zeros

Example:
Input:
6
-4 3 -9 0 4 1

Array: [-4, 3, -9, 0, 4, 1]
Positive numbers: 3, 4, 1 → 3 elements
Negative numbers: -4, -9 → 2 elements
Zero: 0 → 1 element

Ratios:
Positive: 3/6 = 0.500000
Negative: 2/6 = 0.333333
Zero: 1/6 = 0.166667

Output:
0.500000
0.333333
0.166667

Approach:
1. Create 3 variables to assign the number of occurrences of each case
2. Loop de array and push +1 to the corresponding variable
3. Get each ratio

"""


def plusMinus(arr):
    """
    Calculate and print the ratios of positive, negative, and zero values in an array.

    Args:
        arr (List[int]): Array of integers

    Returns:
        None: Prints three lines with ratios to 6 decimal places
    """
    p = 0
    n = 0
    c = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        elif arr[i] == 0:
            c += 1

    return ["{:.6f}".format(p / len(arr)), "{:.6f}".format(n / len(arr)), "{:.6f}".format( c / len(arr))]


if __name__ == '__main__':
    # Read the size of the array
    '''
    n = int(input().strip())

    # Read the array elements
    arr = list(map(int, input().rstrip().split()))
    '''
    arr = [-4, 3, -9, 0, 4, 1]
    # Call the function
    #plusMinus(arr)
    res = plusMinus(arr)
    print(res[0])
    print(res[1])
    print(res[2])

