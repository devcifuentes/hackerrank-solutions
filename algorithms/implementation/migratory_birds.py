"""
Problem: Migratory Birds
URL: https://www.hackerrank.com/challenges/migratory-birds/problem
Difficulty: Easy
Category: Algorithms - Implementation

Description:
Given an array of bird sightings where every element represents a bird type id, determine the id of the
most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest
of their ids.

Example:
arr = [1, 1, 2, 2, 3]

There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

Function Description:
Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):
- int arr[n]: the types of birds sighted

Returns:
- int: the lowest type id of the most frequently sighted birds

Input Format:
The first line contains an integer, n, the size of arr.
The second line describes arr as n space-separated integers, each a type number of the bird sighted.

Constraints:
5 <= n <= 2 * 10^5
It is guaranteed that each type is 1, 2, 3, 4, or 5.

Sample Input 0:
6
1 4 4 4 5 3

Sample Output 0:
4

Explanation 0:
The different types of birds occur in the following frequencies:
- Type 1: 1 bird
- Type 2: 0 birds
- Type 3: 1 bird
- Type 4: 3 birds
- Type 5: 1 bird

The type number that occurs at the highest frequency is type 4, so we print 4 as our answer.

Sample Input 1:
11
1 2 3 4 5 4 3 2 1 3 4

Sample Output 1:
3

Explanation 1:
The different types of birds occur in the following frequencies:
- Type 1: 2
- Type 2: 2
- Type 3: 3
- Type 4: 3
- Type 5: 1

Two types have a frequency of 3, and the lower of those is type 3.
"""


def migratoryBirds(arr):
    print(f'Array of birds: {arr}')
    res_arr = [0] * (max(arr) + 1)
    print(res_arr)
    for b in arr:
        res_arr[b] += 1

    max_count = 0
    bird_type = 0

    for i in range(1,len(res_arr)):
        print(i, res_arr[i])
        if res_arr[i] > max_count:
            max_count = res_arr[i]
            bird_type = i

    print(f'Result is bird type {bird_type} with {max_count} times')
    return bird_type


if __name__ == '__main__':
    '''
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    '''
    arr = [1, 4, 4, 4, 5, 3]

    result = migratoryBirds(arr)
    print(result)
