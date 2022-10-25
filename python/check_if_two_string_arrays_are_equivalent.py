# leetcode problem # 1662. Check If Two String Arrays are Equivalent

"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.


Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1 <= word1.length, word2.length <= 10^3
1 <= word1[i].length, word2[i].length <= 10^3
1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
word1[i] and word2[i] consist of lowercase letters.
"""

"""
My solution: Individually increment indexing on each list

Simplified Problem: Comparing two strings are equivalent
Sample input: "abcd" and "abcd"
Solution:
1. Check that both strings are equal in length
- if the strings do not have the same length, it is impossible for them to be equal
2. Compare the strings character by character
- Iterate from character 0 to character N - 1
- if any charcters are mismatched, the strings are not equal
3. If steps 1 and 2 completed without returning, the strings are equal
- Return True

Extending to this problem:
As the strings are now broken up into separate strings of unknown length, some extra steps are needed.
- The solution must be able to find the n-th letter in reasonable time (where n spans from 0 to to the length of the combined word)
    - In this solution, 4 indeces are used; 2 for each string array
        - For each string array, keep track of index of the current string and index of the character within the string
            - After each iteration, increment the index for the character within the string
            - If all characters are used in the string, move to the next string and start from the first character
            - If any current string index reaches len(string array), the string has reached the end
                - if the other string did not reach its end, the string arrays are not equivalent
                - otherwise, the string arrays are equivalent
    - Like the simplified problem, the strings are not equivalent if any characters are mismatched
- Alternatively, the algorithm can concatenate the strings and use the solution for simplified problem.

Runtime: O(N + M) where N and M are the lengths of word1 and word2, respectively
Space: O(1), memory usage does not depend on input size.
"""


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1Idx = 0
        word2Idx = 0
        word1LetterIdx = 0
        word2LetterIdx = 0

        while word1Idx < len(word1) and word2Idx < len(word2):
            if word1[word1Idx][word1LetterIdx] != word2[word2Idx][word2LetterIdx]:
                return False
            if word1LetterIdx + 1 < len(word1[word1Idx]):
                word1LetterIdx += 1
            else:
                word1Idx += 1
                word1LetterIdx = 0

            if word2LetterIdx + 1 < len(word2[word2Idx]):
                word2LetterIdx += 1
            else:
                word2Idx += 1
                word2LetterIdx = 0

        if word1Idx < len(word1) or word2Idx < len(word2):
            return False
        return True
