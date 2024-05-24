# leetcode problem # 1255. Maximum Score Words Formed by Letters

"""
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.

Example 3:
Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.

Constraints:
1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
"""

"""
My solution: Backtracking

Preprocessing done to reduce complexity at runtime:
- The letters are grouped by the letter, and duplicates are marked by increase in frequency
    - this information is stored in a list, where index 0 is for "a", index 1 for "b", etc.
- Each word is also grouped by the letter
    - this information is also stored in a list
    - these lists are stored together in another list
- The score of a word is calculated
    - each score is an integer, and the scores are stored in a list
    - if the word cannot be made with the letters, it has a score of 0
    * exclude words with scores of 0
        - such words would not be stored in the list of scores and the list of letter counts of words

Main Recursion Logic:
- Base Case: Index out of bounds, all words have been checked
    -> return 0
- For the current word:
    1. find the best score possible when including the word
        - remove the letters of the words from the available letters
        - recurse to the next word
        - add the score of including the current word
        - replace the letters afterwards
        * if the available letters cannot make up the word, it is impossible to include the
        word in the current subset, recursion for including is skipped
    2. find the best score possible when excluding the word
        - recurse to the word without including the current word
    -> return the higher score from the two options above

At the end, return the highest score found from all recursions


Runtime: O(2^N)
Space: O(2^N)
"""


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        wordScores = []
        wordComps = []
        a = ord("a")

        letterCounts = [0] * 26

        for letter in letters:
            letterCounts[ord(letter) - a] += 1

        for word in words:
            wordComp = [0] * 26
            wordScore = 0
            for letter in word:
                wordScore += score[ord(letter) - a]
                wordComp[ord(letter) - a] += 1
            for idx, freq in enumerate(wordComp):
                if freq > letterCounts[idx]:
                    wordScore = 0
                    break
            if wordScore > 0:
                wordScores.append(wordScore)
                wordComps.append(wordComp)

        def recurse(wordIdx):
            if wordIdx >= len(wordComps):
                return 0

            canInclude = True
            for idx in range(26):
                letterCounts[idx] -= wordComps[wordIdx][idx]
                if letterCounts[idx] < 0:
                    canInclude = False

            includeScore = 0
            if canInclude:
                includeScore = wordScores[wordIdx] + recurse(wordIdx + 1)

            for idx in range(26):
                letterCounts[idx] += wordComps[wordIdx][idx]

            excludeScore = recurse(wordIdx + 1)

            return max(includeScore, excludeScore)

        return recurse(0)
