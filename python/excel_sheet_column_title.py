# leetcode problem # 168. Excel Sheet Column Title

"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 231 - 1
"""

"""
My solution: Calculating 1-indexed 26-Base

Observation:
1. The letters can be mapped to 26 different numerical values, 
    - "A" corresponds to 1, and "Z" corresponds to 26
2. The numerical system for the column title is 1-indexed
    - the smallest value could be repeated in an 1-indexed system
        - in a 0-indexed system, 000 is not a valid value
        - in an 1-indexed system, 111 is a valid value
    - The smallest value in the numerical system (1) has inherent non-zero value and must
        be accounted for
        - As such, processing the number system as a 0-based system would cause issues

Example:
input: 703 -> output: "AAA"
- explanation: 703 is broken into 1 * 26^0 + 1 * 26^1 + 1 * 26^2

Processing 1-based indexing in a 0-based indexing system:
- process from right to left (smallest to largest)
- for each place:
    - find the coefficient value, where coefficient = (columnNumber - 1) % 26
    - convert the coefficient to the corresponding letter
    - subtract the coefficient from columnNumber
    - divide columnNumber by 26 and remove the decimals

Runtime: O(logN) where N is the input integer columnNumber
Space: O(1), memory usage does not scale with input except for the output variable
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber > 0:
            coefficient = (columnNumber - 1) % 26
            ans = chr(coefficient + ord("A")) + ans
            columnNumber -= coefficient
            columnNumber = columnNumber // 26

        return ans