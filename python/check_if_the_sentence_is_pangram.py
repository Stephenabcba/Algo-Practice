# leetcode problem # 1832. Check if the Sentence Is Pangram

"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

"""
My solution: Check each letter until all 26 letters are found

Basic Idea: check each letter in sentence string and keep track of what letters have occurred.
- If all 26 letters have been processed, return True
- If not all 26 letters have been processed by the end of the sentence, return False

Keeping track of what has been sighted: Use a boolean array
- the letter "a" is at index 0
- the letter "z" is at index 25
- if the program encounters an unprocessed letter, set the corresponding boolean in the array to True
    - ex: the first time the program encounters "a", set array[0] to True
- in addition, keep a count of how many unique letters have been spotted
    - everytime a new boolean is set to True, increment this count
    - when the count reaches 26, the sentence is a pangram


Runtime: O(N) where N is the number of letters in the string sentence

Space: O(1), memory usage does not depend on input size
- No matter what size the input is, the program will create a list of length 26 (for each letter in the alphabet)
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        occurrence = [False for i in range(26)]
        distinctCount = 0
        aPos = ord("a")

        for letter in sentence:
            position = ord(letter) - aPos
            if not occurrence[position]:
                occurrence[position] = True
                distinctCount += 1
                if distinctCount >= 26:
                    return True

        return False
