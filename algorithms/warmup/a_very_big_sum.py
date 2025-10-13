"""
Problem: A Very Big Sum
URL: https://www.hackerrank.com/challenges/a-very-big-sum/problem
Difficulty: Easy
Category: Algorithms - Warmup

Description:
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that
some of those integers may be quite large.

Input Format:
The first line of the input consists of an integer n.
The next line contains n space-separated integers contained in the array.

Constraints:
1 ≤ n ≤ 10
0 ≤ ar[i] ≤ 10^10

Output Format:
Return the integer sum of the elements in the array.

Example:
Input:
5
1000000001 1000000002 1000000003 1000000004 1000000005
Output:
5000000015

Max Score: 10
"""


def aVeryBigSum(ar):
    """
    Loop the array and calculate the sum of the elements
    or directly sum the elements
    """
    res = 0
    # Simply return the sum of both numbers
    for element in ar:
        res += element
        #print(res)
    print("Result 1 =",res)

    res2 = sum(ar)
    print("Result 2 =", res2)
    return res


if __name__ == '__main__':
    #ar_count = int(input().strip())
    ar_count = 5
    #ar = list(map(int, input().rstrip().split()))
    ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

    res = aVeryBigSum(ar)
    print(res)