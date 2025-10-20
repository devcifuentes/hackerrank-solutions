"""
Problem: Compare the Triplets
URL: https://www.hackerrank.com/challenges/compare-the-triplets/problem
Difficulty: Easy
Category: Algorithms - Warmup

Description:
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale
from 1 to 100 for three categories: problem clarity, originality, and difficulty.

The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

- If a[i] > b[i], then Alice is awarded 1 point.
- If a[i] < b[i], then Bob is awarded 1 point.
- If a[i] = b[i], then neither person receives a point.

Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.

Input Format:
The first line contains 3 space-separated integers, a[0], a[1], and a[2], the respective values in triplet a.
The second line contains 3 space-separated integers, b[0], b[1], and b[2], the respective values in triplet b.

Constraints:
1 ≤ a[i] ≤ 100
1 ≤ b[i] ≤ 100

Output Format:
Return an array of two integers, the first being Alice's score and the second being Bob's score.

Example:
Input:
5 6 7
3 6 10
Output:
1 1

Max Score: 10
"""


def compareTriplets(a,b):
    """
    Verify the len of two arrays, must be the same
    Loop the arrays and compare by pairs.
    Save the score while loop them in new array

    Score Obtained: 10
    """

    if len(a) != len(b):
        return "error in an array size"

    res = [0,0]
    for i in range(len(a)):
        if a[i] > 100 or b[i] > 100:
            return "error in an element of array, more than 100"
        if a[i] > b[i]:
            res[0] += 1
        elif a[i] < b[i]:
            res[1] += 1

    return res


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)