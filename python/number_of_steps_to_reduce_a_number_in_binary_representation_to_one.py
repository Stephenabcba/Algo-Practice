# leetcode problem # 1404. Number of Steps to Reduce a Number in Binary Representation to One

"""
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
Input: s = "1"
Output: 0

Constraints:
1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
"""

"""
My solution: Work from right to left

Keep track of the carryover value from previous iterations
Case where the next carryover value is 0:
- If the value at the current bit + the carryover value is 0, divide by 2 (1 step, carryover value = 0)
Case where the next carryover value is 1:
- If the value is 1, add 1 and then divide by 2 (2 steps, carryover value = 1)
- If the value is 2, divide by 2 (1 step, carryover value = 1)
-> In all cases, at least 1 step is needed for each bit (dividing by 2)

Special Case: Last Bit (left-most bit):
- if the value of the bit + the carryover value is 1, no action is needed
- if the value is 0 or 2, 1 extra step is needed
    - if the value is 0, add 1
    - if the value is 2, divide by 1

Count the number of steps taken and return the total at the end

Runtime: O(N) where N is the length of string s
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def numSteps(self, s: str) -> int:
        carryBit = 0
        idx = len(s) - 1
        steps = 0

        while idx > 0:
            if s[idx] == "1" or carryBit == 1:
                if s[idx] == "0" or carryBit == 0:
                    steps += 1
                carryBit = 1
            else:
                carryBit = 0
            steps += 1
            idx -= 1

        carryBit += int(s[0])
        if carryBit % 2 == 0:
            steps += 1
        return steps
