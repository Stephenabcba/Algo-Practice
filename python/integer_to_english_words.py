# leetcode problem # 273. Integer to English Words

"""
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 2^31 - 1
"""

"""
My solution: Process 3 numbers at a time

In English words, the numbers are split into 3 numbers at a time
- Ex: 1,234,567 is split into:
    - 1 million
    - 234 Thousand
    - 567
- Most of the time, each place is separate from each other
    - 123 is pronounced as:
        - One Hundred
        - Twenty
        - Three

Special Cases:
- 0: the only time a 0 is pronounced is if num = 0
    - in all other cases, the 0 is skipped and not said
- 10-19: in the teens, two places are said together
    - ex: 17 is pronounced as "Seventeen", instead of "Ten Seven"

Idea:
- Process 3 numbers at a time
- Within the 3 numbers, process the hundreds place first, then tens, then ones
    - add the suffix at the end of the three numbers (Billion, Million, Thousand)
    - watch out for the special cases
- Return the converted English word version of the number

Runtime: O(1), time usage does not depend on input
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        places = [[9, "Billion"], [6, "Million"], [3, "Thousand"], [0, ""]]
        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        ones = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        out = []

        for power, name in places:
            curTrio = num // 10 ** power
            if curTrio > 0:
                hundreds = curTrio // 100
                curTrio %= 100
                if hundreds > 0:
                    out.append(ones[hundreds])
                    out.append("Hundred")

                ten = curTrio // 10
                if ten > 1:
                    out.append(tens[ten])
                    curTrio %= 10
                elif ten > 0:
                    out.append(teens[curTrio])
                    curTrio = 0

                if curTrio > 0:
                    out.append(ones[curTrio])

                if len(name) > 0:
                    out.append(name)
            num %= 10 ** power

        return " ".join(out)
