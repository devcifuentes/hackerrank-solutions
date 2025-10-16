"""
Problem: Time Conversion
URL: https://www.hackerrank.com/challenges/time-conversion/problem
Difficulty: Easy
Category: Warmup

Description:
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock (midnight)
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock (noon)

Input Format:
A single string s that represents a time in 12-hour clock format
(i.e.: hh:mm:ssAM or hh:mm:ssPM)

Constraints:
All input times are valid

Output Format:
Convert and return the time in 24-hour format as a string.

Example 1:
Input: 07:05:45PM
Output: 19:05:45
Explanation: 7 PM + 12 = 19 hours in 24-hour format

Example 2:
Input: 12:01:00PM
Output: 12:01:00
Explanation: 12 PM stays as 12 in 24-hour format (noon)

Example 3:
Input: 12:01:00AM
Output: 00:01:00
Explanation: 12 AM becomes 00 in 24-hour format (midnight)

Example 4:
Input: 01:00:00AM
Output: 01:00:00
Explanation: 1 AM stays as 01 in 24-hour format

Conversion Rules Summary:
┌─────────────┬──────────────┐
│  12-Hour    │   24-Hour    │
├─────────────┼──────────────┤
│ 12:00:00AM  │  00:00:00    │ (midnight)
│ 01:00:00AM  │  01:00:00    │
│ 11:00:00AM  │  11:00:00    │
│ 12:00:00PM  │  12:00:00    │ (noon)
│ 01:00:00PM  │  13:00:00    │
│ 11:00:00PM  │  23:00:00    │
└─────────────┴──────────────┘

Pattern to observe:
- AM (except 12AM): Keep the hour as is
- 12AM: Convert to 00
- PM (except 12PM): Add 12 to the hour
- 12PM: Keep as 12

Approach:
TODO: Escribe aquí tu estrategia para resolver el problema
Pistas:
- Necesitas extraer: horas, minutos, segundos, y el período (AM/PM)
- Usa string slicing o split para separar las partes
- Maneja los casos especiales de 12AM y 12PM
1.
2.
3.

Time Complexity: O(?) - TODO: Analiza la complejidad
Space Complexity: O(?) - TODO: Analiza la complejidad
"""


def timeConversion(s):
    """
    Convert time from 12-hour format to 24-hour format.

    Args:
        s (str): Time in 12-hour format (hh:mm:ssAM or hh:mm:ssPM)

    Returns:
        str: Time in 24-hour format (hh:mm:ss)
    """
    h = s[:2]
    set = s[-2:]
    if set == 'PM' and str(h) != '12':
        military_hour = int(h) + 12
    elif set == 'AM' and h == '12':
        military_hour = '00'
    else:
        military_hour = h
    time = s.split(':',1)
    time[0] = military_hour
    time[1] = time[1][0:-2]
    string_time = str(time[0]) + ':' + str(time[1])
    return string_time


if __name__ == '__main__':
    # Read the time in 12-hour format
    s = input()

    # Convert and print the result
    result = timeConversion(s)
    print(result)