# leetcode problem # 12. Integer to Roman

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= num <= 3999
"""

"""
My solution: process the symbols from largest to smallest

Observations:
1. When converting from decimal value to Roman numerals, the largest possible Roman numeral is always used
- ex: to express 1000, the symbol "M" is used, rather than "DD" or "CCCCCCCCCC"
-> Check each symbol one by one to see if the remainder is larger than the symbol, and reduce the remainder

2. Most Symbols can occur at most once:
- ex: "DD", "XCXC", "LL", etc. would never occur
* This treats symbols like "D" and "CD" as distinct symbols
    - ex: "DCD" is an acceptable Roman numeral for 900
- Exceptions: Power of 10s; these can occur more than once
    - "III" (3), "CCC" (300), "MMM" (3000) are all valid Roman numerals

Combining the two observations above, a solution logic can be produced:
1. List out all the symbols and their respective values from largest to smallest
- This information is stored in a list of lists
    - the inner list stores the respective information of a symbol
    - the inner list also keeps track of whether the symbol is repeatable
2. Iterate through each symbol and reduce the remainder value accordingly
    - as the conversion is completed when the remainder is 0, iteration can end early if remainder is 0.
    - if the remainder is over the value of the current symbol:
        - append the symbol to the string
        - reduce the remainder according to the value of the symbol
        - if the symbol can be repeated, add as many symbols as possible
            - in implementation, this is done with integer division and modulo
3. Return the converted Roman numeral once conversion is done.

Runtime: O(1); runtime does not scale with input
- unless the loop ends early, the logic will process every symbol regardless of what the input value is.
Space: O(1); space does not scale with input
- unless the loop ends early, the logic will process every symbol regardless of what the input value is.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""

        symbols = [
            [1000, "M", True],
            [900, "CM", False],
            [500, "D", False],
            [400, "CD", False],
            [100, "C", True],
            [90, "XC", False],
            [50, "L", False],
            [40, "XL", False],
            [10, "X", True],
            [9, "IX", False],
            [5, "V", False],
            [4, "IV", False],
            [1, "I", True]
        ]

        idx = 0
        while num > 0 and idx < len(symbols):
            symbol = symbols[idx]
            if num >= symbol[0]:
                if symbol[2]:
                    ans += num // symbol[0] * symbol[1]
                    num = num % symbol[0]
                else:
                    ans += symbol[1]
                    num -= symbol[0]
            idx += 1

        return ans
