"""
Problem: Between Two Sets
URL: https://www.hackerrank.com/challenges/between-two-sets/problem
Difficulty: Easy/Medium
Category: Algorithms - Implementation /

Description:
There will be two arrays of integers.
Determine all integers that satisfy the following two conditions:
1.- The elements of the first array are all factors of the integer being considered
2.- The integer being considered is a factor of all elements of the second array

Determina todos los numeros que satisfacen las siguientes dos condiciones:
Los elementos del primer array son todos multiplo del numero
Cada numero es un multiplo de todos los elementos del segundo array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
Example:
    a = [2,6]
    b = [24,36]

There are two numbers between the arrays: 6 and 12.
6%2 = 0, 6%6 = 0, 24%6 = 0 and 36%6=0 for the first value.
12%2 = 0, 12%6 = 0  and 24%12 = 0, 36&12 = 0  for the second value.
Return 2.

Function Description
Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
getTotalX has the following parameter(s):
int a[n]: an array of integers
int b[m]: an array of integers
Returns
int: the number of integers that are between the sets
Input Format
The first line contains two space-separated integers, n and m, the number of elements in arrays a and b.
The second line contains n distinct space-separated integers a[i] where 0 <= i < m.
The third line contains m distinct space-separated integers b[j] where 0<= j < m.
Constraints
- 1 <= n,m <= 10
- 1 <= a[i] <= 100
- 1 <= b[j] <= 100


Sample Input
2 3
2 4
16 32 96
Sample Output
3

Explanation
2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.
4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.
"""
from functools import reduce
from typing import List
import math


def getTotalX(a: List[int], b: List[int]) -> int:
    results = []
    max_loop = (min(b) // max(a)) + 1
    print(f'MCM {reduce(math.gcd, b)}')
    min_comun_multiple_a = reduce(math.lcm, a)
    print(min_comun_multiple_a)
    print(f'mcm {min_comun_multiple_a}')
    max_comun_miltuple_b = reduce(math.gcd, b)
    print(f'max loop {max_loop}')
    for i in range(1 , max_loop):
        print(f'Lopp: {i}')
        r = i * max(a)
        print(f'Step1 {r}')

        if min_comun_multiple_a <= r and max_comun_miltuple_b % r == 0:
            print(f'Step2: {r}')
            results.append(r)

    return len(results)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))
    result = getTotalX(arr, brr)
    print(f'result: {result}')
