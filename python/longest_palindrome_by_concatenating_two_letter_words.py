# leetcode problem # 2131. Longest Palindrome by Concatenating Two Letter Words

"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.
"""

"""
My Solution: Use dictionary

Observation: To be in the assembled palindrome, a two-letter word must pair with another two-letter word in reversed order
- Exception: optionally, there could be a two-letter word in the center where the first letter is the same as the second letter
    - ex: "bcaacb"
    - however, this is only if the word is not already paired
        - ex: "bcaacb" would not be used if there is another "aa" available
        - instead, "bcaaaacb" would be used

A dictionary can be used to keep track of seen words and retrieve them in constant time.
- in this implementation, the words are stored in the reversed order when it is not used
    - it is possible to store the words normally, and reverse the current word when searching

Logic:
1. Keep track of how many pairs have been found, and whether there are any two-letter words with identical letters
2. Create a dictionary to keep track of seen words
3. Iterate through each word in words list
    - If the matching pair exists, increment the number of pairs found
        - if the matching pair was a word with identical letters, decrement the variable accordingly
    - If the matching pair does not exist, store the current word in the dictionary
        - if the matching pair was a word with identical letters, increment the variable accordingly
        - there could be multiple copies of a word in the dictionary
4. Return the answer
- for each matching pair found, 4 letters are added to the palindrome
- if there is a word available with identical letters, 2 letters are added to the palindrom

Runtime: O(N) where N is the length of words array
Space: O(N) where N is the length of words array
"""


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mirrorPairs = 0
        identicalPairs = 0

        unpairedWords = {}

        for word in words:
            if word in unpairedWords and unpairedWords[word] > 0:
                if word[0] == word[1]:
                    identicalPairs -= 1
                mirrorPairs += 1
                unpairedWords[word] -= 1
            else:
                if word[0] == word[1]:
                    identicalPairs += 1

                reversedWord = word[::-1]
                if reversedWord not in unpairedWords:
                    unpairedWords[reversedWord] = 1
                else:
                    unpairedWords[reversedWord] += 1

        if identicalPairs > 0:
            return mirrorPairs * 4 + 2

        return mirrorPairs * 4
