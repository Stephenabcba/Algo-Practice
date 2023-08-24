# leetcode problem # 68. Text Justification

"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""

"""
My solution: Group words with minimal space then add padding

To create a valid line with as many words as possible, a minimum of 1 space is needed between
every word in the line
- if the line cannot fit the next word, build current line into a string and add it to the answer
    - add extra spaces for padding if needed

Logic for deciding where to place the spaces for padding:
1. If the line only contains 1 word
    - add all the space padding to the end
2. If the line is the last line
    - add 1 space between every word, then the remaining spaces at the end
3. All other lines with multiple words:
    - calculate the minimum number of spaces to add
        - this is equal to the leftover spaces divided by (the number of words - 1)
            - the value is floored to remove decimals
    - calculate the remaining spaces if only the minimum spaces are used
    - between each word, add the minimum spaces
        - if there are remaining spaces to be added, add 1 more space

Runtime: O(N) where N is the number of words
Space: O(N)
"""

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        curLen = 0
        curLine = []

        for word in words:
            if len(word) + curLen + len(curLine) > maxWidth:
                if len(curLine) == 1:
                    ans.append(curLine[0] + " " * (maxWidth - curLen))
                else:
                    numSpaces = maxWidth - curLen
                    separateCount = len(curLine) - 1
                    commonSpace = numSpaces // separateCount
                    extraSpace = numSpaces - commonSpace * separateCount
                    newString = ""
                    for idx, text in enumerate(curLine):
                        newString += text
                        if idx < len(curLine) - 1:
                            newString += " " * commonSpace
                            if extraSpace > 0:
                                newString += " "
                                extraSpace -= 1
                    ans.append(newString)
                curLine = [word]
                curLen = len(word)
            else:
                curLine.append(word)
                curLen += len(word)

        newString = ""
        for idx, word in enumerate(curLine):
            newString += word
            if idx < len(curLine) - 1:
                newString += " "
        newString += " " * (maxWidth - len(newString))
        ans.append(newString)

        return ans