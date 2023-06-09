# leetcode problem # 744. Find Smallest Letter Greater Than Target

"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

Constraints:
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""

"""
My solution: binary search

As the letter array is sorted, binary search can be applied to find the first letter
lexicographically greater than target

To compare two letters lexicographically, their character codes can be compared
-> in python, a letter's character code can be found using ord()

An initial check is done to ensure that there is at least 1 letter lexicographically 
larger than target in letters
    -> if all letters are smaller than target, return letters[0]

Runtime: O(logN) where N is the length of the letters list
Space: O(1) memory usage does not depend on input
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) >= ord(letters[-1]):
            return letters[0]
        
        start = 0
        end = len(letters)

        while start < end:
            middle = (start + end) // 2
            if ord(target) < ord(letters[middle]):
                end = middle
            else:
                start = middle + 1
        return letters[start]