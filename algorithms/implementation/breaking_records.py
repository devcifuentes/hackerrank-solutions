"""
Problem: Breaking the Records
URL: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
Difficulty: Easy
Category: Algorithms - Implementation

Description:
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.

Example:
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]

Scores are in the same order as the games played. She tabulates her results as follows:

Count  Game  Score  Minimum  Maximum  Min  Max
  0      0     10      10       10      0    0
  1      1      5       5       10      1    0
  2      2     20       5       20      1    1
  3      3     20       5       20      1    1
  4      4      4       4       20      2    1
  5      5      5       4       20      2    1
  6      6      2       2       20      3    1
  7      7     25       2       25      3    2
  8      8      1       1       25      4    2

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

Function Description:
Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):
- int scores[n]: points scored per game

Returns:
- int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records,
  and index 1 is for breaking least points records.

Input Format:
The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective values of scores[i].

Constraints:
1 <= n <= 1000
0 <= scores[i] <= 10^8

Sample Input 0:
9
10 5 20 20 4 5 2 25 1

Sample Output 0:
2 4

Explanation 0:
She broke her best record twice (after games 2 and 7) and her worst record four times (after games 1, 4, 6, and 8),
so we print 2 4 as our answer. Note that she did not break her record for best score during game 3, as her score
during that game was not strictly greater than her best record at the time.

Sample Input 1:
10
3 4 21 36 10 28 35 5 24 42

Sample Output 1:
4 0

Explanation 1:
She broke her best record four times (after games 1, 2, 3, and 9) and her worst record zero times
(no score during the season was lower than the one she earned during her first game), so we print 4 0 as our answer.
"""


def breakingRecords(scores):
    print(scores)
    high = scores[0]
    low = scores[0]
    h_counter = 0
    l_counter = 0
    for score in scores:
        if score > high:
            high = score
            h_counter += 1
            print(f'score: {score} -> new high score: {high}')

        if score < low:
            low = score
            l_counter += 1
            print(f'score: {score} -> new low score: {low}')
    print(f'high: {high}, low: {low}')
    print(f'h_counter: {h_counter}, l_counter: {l_counter}')
    result = [h_counter, l_counter]
    return result


if __name__ == '__main__':
    '''
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    '''
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
