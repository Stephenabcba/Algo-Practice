# leetcode problem # 1915. Number of Wonderful Substrings

"""
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"

Example 2:
Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"

Example 3:
Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"

Constraints:
1 <= word.length <= 10^5
word consists of lowercase English letters from 'a' to 'j'.
"""

"""
My attempt: Failed due to time limit exceeded

- Check every substring of every length to see if there are any matches

Runtime: O(N ^ 2) where N is the length of word
Space: O(N)
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        letterCount = defaultdict(int)
        history = [letterCount.copy()]

        for letter in word:
            letterCount[letter] += 1
            history.append(letterCount.copy())

        ans = len(word)

        for substringLen in range(2, len(word) + 1):
            for startIdx in range(len(word) - substringLen + 1):
                hasOdd = False
                isValid = True
                for letter, count in history[startIdx + substringLen].items():
                    if (count - history[startIdx][letter]) % 2:
                        if hasOdd:
                            isValid = False
                            break
                        else:
                            hasOdd = True
                if isValid:
                    ans += 1

        return ans


"""
My solution: Bit manipulation

Use the first 10 bits to store whether there are even or odd number of occurrence of each letter
- the 0 bit is used to store information about "a", 2 bit for "b", and so on
- the value can be stored as an integer, and manipulated using bitwise operations
- these integers is used as a key in the dictionary, storing the number of times they occurred

Checking whether there are wonderful strings ending at the current letter:
- Using the integer data from above, a string is wonderful if there is at most 1 change in bits from the current letter
    - add the count to the total count if such instance exists

Runtime: O(N) where N is the length of word
- Even though the logic runs with nested loops, the inner loop runs exactly 10 times every iteration, making the runtime O(10*N)
Space: O(1), memory usage does not depend on input
- the dictionary is limited to 2^10, or 1024 entries
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitData = 0
        aOrd = ord("a")
        history = defaultdict(int)
        history[0] += 1

        ans = 0

        for letter in word:
            idx = ord(letter) - aOrd
            bitData ^= 1 << idx
            ans += history[bitData]
            for bitChange in range(11):
                ans += history[bitData ^ (1 << bitChange)]
            history[bitData] += 1

        return ans
