"""
Problem: Simple Array Sum
Link: https://www.hackerrank.com/challenges/simple-array-sum/problem
Difficulty: Easy
Category: Warmup

Description:
Given an array of integers, find the sum of its elements.

Example:
Input: ar = [1, 2, 3, 4, 10, 11]
Output: 31

Constraints:
- 0 < n ≤ 1000
- 0 < ar[i] ≤ 1000

Input Format:
The first line contains an integer, n , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Approach:
Calculate de total sum of the array.

Time Complexity: O(n) - n = array size
Space Complexity: O(1) - no extra space

MaxScore:10
"""


def simpleArraySum(ar):
    """
    Calculate the sum of all elements in the array.

    Args:
        ar (list): Array of int

    Returns:
        int: Total sum of all elements in the array

    Score Obtained: 10
    """
    return sum(ar)


# Alternative Solution without use sum()
def simpleArraySum_alternative(ar):
    """
    Calculate the sum with a explicit loop.
    Usefull to demostrate the basic concepto without built-in functions.

    Args:
        ar (list): Array of int

    Returns:
        int: Total Sum of the elements

    Score Obtained: 10
    """
    total = 0
    for num in ar:
        total += num
    return total


if __name__ == '__main__':
    # Entrada del problema
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    # Calcular y mostrar resultado
    result = simpleArraySum(ar)
    print(result)