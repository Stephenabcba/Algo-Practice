# leetcode problem # 1657. Determine if Two Strings Are Close

"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
1 <= word1.length, word2.length <= 10^5
word1 and word2 contain only lowercase English letters.
"""

"""
My solution: Use dictionaries

Observations:
1. The number of letters in total cannot be changed by the two operations
-> Word1 must be the same length as word 2 for them to be similar
2. Letters that do not exist in the word cannot be used
-> The letters that make up word1 and word 2 must be the same
    - ex. if word1 has "a", word2 must have "a", and vice versa
3. operation 1 is able to move any letter in a word anywhere
-> order of letters in word1 and word2 do not matter
4. operation 2 can't swap to a letter that does not exist in the word
-> The frequency distribution of letters must be the same
    - however, the letter that holds a specific frequency can be different
        - observation 2 must still be met
    - ex. "aabbb" is similar to "bbaaa"
        - operation 2 can be performed
    - ex2. "aaa" is not similar to "ccc"
        - observation 2 is violated, it is impossible to change from one word to another
    - ex3. "aaabc" is not similar to "abbcc"
        - observation 4 is violated, word1 has 3 "a"s, but
            word2 has no letters that occurred 3 times.

Logic: Ensure that the observations are true
* From observation 3, the words can be simplified into frequencies stored in a dictionary,
    as their relative order does not matter
1. Ensure observation 1 is true, compare the lengths of the words
    - if the lengths are not the same, return False
2. Iterate through each word and count the number of each letter in the word
    - this information can be stored in a dictionary
3. Ensure observation 2 is true, compare the letters that exist in each word
    - if the dictionaries have different lengths, the words are not composed
        of the same letters; return False
4. Ensure observation 4 is true, compare the frequencies that exist in each word
    - this can be done by creating a new dictionary, and count the number of times each frequency
        occurs
    - if word1 and word2 have differences in frequencies, return False
5. If none of the steps above returned False, the two words are similar. Return True.

Runtime: O(N) where N is the number of letters in word1 and word2
Space: O(1), memory usage is based on the number of available characters, which is
    a constant of 26 in this case.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Make sure that both words have the same length
        if len(word1) != len(word2):
            return False

        # build the dictionaries of the letters in each word
        word1Letters = {}
        word2Letters = {}

        for letter in word1:
            word1Letters[letter] = word1Letters.get(letter, 0) + 1

        for letter in word2:
            word2Letters[letter] = word2Letters.get(letter, 0) + 1

        # check that the dictionaries have the same length
        # combined with the iteration of all letters in word1Letters below,
        # when both checks pass, word1Letters and word2Letters have the same letters
        if len(word1Letters) != len(word2Letters):
            return False

        # build up the frequency counts dictionary while each letter is being processed too
        frequencyCounts = {}

        for letter in word1Letters:
            if letter not in word2Letters:
                return False
            frequencyCounts[word1Letters[letter]] = frequencyCounts.get(
                word1Letters[letter], 0) + 1
            frequencyCounts[word2Letters[letter]] = frequencyCounts.get(
                word2Letters[letter], 0) - 1

        # at this point, if the words are similar, all values in the key-value
        # pairs of frequencyCounts should be 0
        for frequency in frequencyCounts.values():
            if frequency != 0:
                return False

        return True
