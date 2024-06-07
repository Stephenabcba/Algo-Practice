# leetcode problem # 648. Replace Words

"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""

"""
My solution: Tree of dictionaries

The words in a dictionary can be stored as a tree of letters, where the first letter is storted in the first level in the tree, and the second is letter is stored
in the second level in the tree
- To denote an end of a word, "." is used as a child node at that location
- From the root of the tree to each ".", a word in the dictionary can be reconstructed
-> This tree can be implemented with nested dictionaries(python data structure)
    * as the problem wants shortest roots, a longer root is omitted if it has another shorter root as its prefix 
        - ex: if the dictionary contains "a" and "ab", "ab" does not need to be stored

After the dictionary is organized, the words in the sentence can be separated and compared against the dictionary
- if the word has a root in the dictionary, insert the root in the new sentence
- otherwise, insert the full word in the new sentence

Runtime: O(N * W + M * W) where N is the number of entries in the dictionary, M is the number of words in the sentence, and W is the length of the words
Space: O(N * W + M * W)
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictTree = {}

        for word in dictionary:
            curDict = dictTree
            for letter in word:
                if "." in curDict:
                    break
                if letter not in curDict:
                    curDict[letter] = {}
                curDict = curDict[letter]
            curDict["."] = "."

        new = []
        start = 0
        stop = 0
        for idx, letter in enumerate(sentence):
            if letter == " ":
                word = sentence[start:stop]
                curDict = dictTree
                rootLength = 0
                for ch in word:
                    if "." in curDict:
                        break
                    if ch in curDict:
                        rootLength += 1
                        curDict = curDict[ch]
                    else:
                        rootLength = -1
                        break
                if rootLength < 1:
                    new.append(word)
                else:
                    new.append(word[:rootLength])
                start = idx + 1
                stop = idx + 1
            else:
                stop += 1

        word = sentence[start:stop]
        curDict = dictTree
        rootLength = 0
        for ch in word:
            if "." in curDict:
                break
            if ch in curDict:
                rootLength += 1
                curDict = curDict[ch]
            else:
                rootLength = -1
                break
        if rootLength < 1:
            new.append(word)
        else:
            new.append(word[:rootLength])

        return " ".join(new)
