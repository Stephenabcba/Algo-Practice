# leetcode problem # 1704. Determine if String Halves Are Alike

"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.


Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""


"""
My solution: count the vowels in the first half and the second half

Intuition: As the problem asks for whether the first and second half
have the same number of vowels, count the number of vowels in each half
and compare.

Modification: As the output only concerns whether the counts are equal,
the first half and the second half can share a counter variable
- if the first half has a vowel, add 1 to the counter
- if the second half has a vowel, subtract 1 from the counter
- at the end, if the counter == 0, the first and second half
have the same number of vowels, return True
    - otherwise, return False

Runtime: O(N) where N is the number of letters in string s
Space: O(1), memory usage does not scale with input
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        vowelCount = 0
        midIdx = len(s) // 2
        for idx in range(len(s) // 2):
            if s[idx] in vowels:
                vowelCount += 1
            if s[midIdx + idx] in vowels:
                vowelCount -= 1
        return vowelCount == 0
