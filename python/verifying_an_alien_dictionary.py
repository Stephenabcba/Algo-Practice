# leetcode problem # 953. Verifying an Alien Dictionary

"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

"""
My Solution: Check each word against the next in the alien dictionary

Intuition:
Each word needs to be checked against the word after, if the current word
is not lexicographically smaller than the word after, the words are not
sorted.

Cases:
1. The word after is shorter than the current word, and all letters match
in the word -> list is not sorted correctly, return false
    - in the english dictionary an example would be: apple vs app
2. The first differing letter in the current word and the word after has
a smaller value in the current word -> list is correct on this word,
check the next word
    - in the english dictionary an example would be: app vs apz
3. The first differing letter in the current word and the word after has
a smaller value in the next word -> list is not sorted correctly, return
false
    - in the english dictionary an example would be: apz vs app
4. (Inherently applied by the logic) The current word is shorter than the word 
after, and all letters match in the word -> list is not sorted correctly, 
return false
    - in the english dictionary an example would be: app vs apple

If every word in the dictionary is lexicographically smaller than the word
after, the list is sorted correctly, return True

* It is unnecessary to check the last word against the word after, as there's
no word after the last word

To easily access which letter comes first in the alien dictionary, create
a dictionary where the letter is the key and the index of the letter in
the order is the value

Runtime: O(N*M) where N is the number of words in the list, and M is the
length of each word
    - However, it only occurs when every word in the list is identical,
    otherwise the logic would move on to the next word or return false
    on the first differing letter
Space: O(1), memory usage does not depend on input size
    - the main memory usage is the dictionary to hold the letter orders,
    and the size of the library is always 26 from problem constraints
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for idx, letter in enumerate(order):
            orderDict[letter] = idx

        curIdx = 0
        while curIdx < len(words) - 1:
            for idx in range(len(words[curIdx])):
                if idx >= len(words[curIdx + 1]):
                    return False
                if orderDict[words[curIdx][idx]] < orderDict[words[curIdx + 1][idx]]:
                    break
                if orderDict[words[curIdx][idx]] > orderDict[words[curIdx + 1][idx]]:
                    return False
            curIdx += 1
        return True
