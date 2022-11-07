# leetcode problem # 1323. Maximum 69 Number

"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

Constraints:
1 <= num <= 10^4
num consists of only 6 and 9 digits.
"""

"""
My solution: Find the largest 6

As the problem only allows 1 change and wants the largest number, the solution is to
    make a change to the number that satisfies these requirements.

Observations:
1. Changing a value from 9 to 6 will never raise the value of the number
    - thus, if a change is made, a 6 must be changed to a 9
    - it is possible that no changes are made
        - ex. 9999, 999 are both the largest possible number without any changes already
2. making the change from 6 to 9 at a larger place will result in a larger value
    - ex.  6666 -> 9666 is a larger change than 6666 -> 6696

Solution: Find the largest 6 and change it
- if there's no change to be made, just return the number

Runtime: O(log N) where N is the input num
Space: O(1), memory usage does not scale with input size
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        place = 1000
        while place > 0:
            digit = (num // place) % 10
            print(num, digit, place)
            if digit > 0:
                if digit == 6:
                    return num + 3 * place
            place = place // 10
        return num
