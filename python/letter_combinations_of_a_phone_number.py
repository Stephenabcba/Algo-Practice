# leetcode problem # 17. Letter Combinations of a Phone Number

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

"""
My solution: Recursion / Backtracking

Recursively build up all combinations of the letters 1 by 1, using a list to keep track of the
current letters included.
- if the combination is complete (the number of letters matches length of digits), copy the contents
of the list to a string and add it to the answer list
- after all combinations with the current letter has been created, remove the letter from the current letters
and add a new letter

Runtime: O(K^N * N) where K is the number of letters that a number is mapped to, and N
is the number of digits
- it takes O(N) time to convert the current list to a string
Space: O(N)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMapping = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        ans = []

        if len(digits) == 0:
            return ans

        def buildCombinations(curIdx, curLetters):
            for letter in letterMapping[digits[curIdx]]:
                curLetters.append(letter)
                if len(curLetters) == len(digits):
                    ans.append("".join(curLetters))
                else:
                    buildCombinations(curIdx + 1, curLetters)
                curLetters.pop()

        buildCombinations(0, [])

        return ans