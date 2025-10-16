"""
Problem: Arrays - DS
URL: https://www.hackerrank.com/challenges/arrays-ds/problem
Difficulty: Easy
Category: Data Structures - Arrays

Description:
An array is a type of data structure that stores elements of the same type in a
contiguous block of memory. In an array, A, of size N, each memory location has
some unique index, i (where 0 <= i < N), that can be referenced as A[i] or A[i].

Given an array of integers, print the integers in reverse order.

Note: If you've already solved our C++ domain's Arrays Introduction challenge,
you may want to skip this.

Function Description:
Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):
- int A[n]: the array to reverse

Returns:
- int[n]: the reversed array

Input Format:
The first line contains an integer, N, the number of integers in A.
The second line contains N space-separated integers that make up A.

Constraints:
1 <= N <= 10^3
1 <= A[i] <= 10^4, where A[i] is the ith integer in A.

Sample Input:
4
1 4 3 2

Sample Output:
2 3 4 1
"""


def reverseArray(a):
    reversedArray = []
    for i in range(len(a)):
        pos = len(a) - i - 1
        reversedArray.append(a[pos])
    return reversedArray


if __name__ == '__main__':
    # arr_count = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 4, 3, 2]
    res = reverseArray(arr)
    print(' '.join(map(str, res)))
