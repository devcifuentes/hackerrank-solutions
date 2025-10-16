"""
Problem: Birthday Cake Candles
URL: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
Difficulty: Easy
Category: Warmup

Description:
You are in charge of the cake for a child's birthday. You have decided the cake will have
one candle for each year of their total age. They will only be able to blow out the tallest
of the candles. Count how many candles are tallest.

In other words: Find the number of occurrences of the maximum element in the array.

Input Format:
The first line contains a single integer, n, the size of candles array.
The second line contains n space-separated integers, where each integer describes
the height of candles[i].

Constraints:
1 ≤ n ≤ 10^5
1 ≤ candles[i] ≤ 10^7

Output Format:
Return the number of candles that are tallest.

Example 1:
Input:
4
3 2 1 3

Array: [3, 2, 1, 3]
The maximum candle height is 3.
There are 2 candles with height 3.

Output:
2

Example 2:
Input:
4
4 4 1 3

Array: [4, 4, 1, 3]
Candle heights visualization:
    *  *
    *  *
    *  *     *
    *  *  *  *
    4  4  1  3

The tallest candles are 4 units high.
There are 2 candles with this height.

Output:
2

Example 3:
Input:
5
1 1 1 1 1

All candles have the same height (1).
The child can blow out all 5 candles.

Output:
5

Approach:
1. get the max number of the array
2. count max number on the array
3.

"""


def birthdayCakeCandles(candles):
    """
    Count how many candles are the tallest.

    Args:
        candles (List[int]): Array of candle heights

    Returns:
        int: Number of tallest candles
    """
    tallest = max(candles)
    print(tallest)
    no_candles = candles.count(tallest)
    print(no_candles)
    return no_candles


if __name__ == '__main__':
    # Read the number of candles
    '''
    candles_count = int(input().strip())

    # Read the candle heights
    candles = list(map(int, input().rstrip().split()))
    '''
    candles = [3, 2, 1, 3]
    # Call the function and print result
    result = birthdayCakeCandles(candles)
