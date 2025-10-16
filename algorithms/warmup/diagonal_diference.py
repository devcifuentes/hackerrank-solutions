"""
Problem: Diagonal Difference
URL: https://www.hackerrank.com/challenges/diagonal-difference/problem
Difficulty: Easy
Category: Warmup

Description:
Given a square matrix, calculate the absolute difference between the sums
of its diagonals.

Input Format:
The first line contains a single integer, n, the number of rows and columns
in the square matrix.
Each of the next n lines describes a row and consists of n space-separated integers.

Constraints:
-100 ≤ arr[i][j] ≤ 100

Output Format:
Return the absolute difference between the sums of the matrix's two diagonals
as a single integer.

Example:
Input:
3
11 2 4
4 5 6
10 8 -12

Matrix:
11  2   4
4   5   6
10  8  -12

Left-to-right diagonal (primary): 11 + 5 + (-12) = 4
Right-to-left diagonal (secondary): 4 + 5 + 10 = 19
Absolute difference: |4 - 19| = 15

Output: 15

Approach:
1. Initialize two variables to store the sum of each diagonal
2. Iterate through the matrix only once (single loop)
3. For primary diagonal: add arr[i][i] (where row index = column index)
4. For secondary diagonal: add arr[i][n-1-i] (where row + column = n-1)
5. Return the absolute difference using abs()
"""


def diagonalDifference(arr):
    '''
    Calculates the absolute difference between two diagonals
    :param arr:
    :return: int

    step1: sum of diagonal 1 -> positions 1,1 + 2,2 + 3,3 + n,n
    step2: sum of diagonal 2 -> positions 1,(n - i -1) + 2,(n - i -1) + 3,(- i -1) + n,(n - i -1)
    step3: absolute difference between diagonals
    '''
    #print(arr)
    rd1 = 0
    rd2 = 0
    for i in range(len(arr)):
        rd1 = rd1 + arr[i][i]
        rd2 = rd2 + arr[i][len(arr) - i - 1]
        print(arr[i])
    print("rd1 = " + str(rd1))
    print("rd2 = " + str(rd2))
    return rd1 - rd2


if __name__ == '__main__':
    # Leer el tamaño de la matriz

    n = int(input().strip())

    # Leer la matriz
    
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Calcular y mostrar el resultado
    result = diagonalDifference(arr)
    print(abs(result))