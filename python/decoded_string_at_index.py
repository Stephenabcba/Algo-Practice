# leetcode problem # 880. Decoded String at Index

"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 10^9
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
"""

"""
My solution: reorganize the decoded string then process

The decoded string can be saved as a list of lists
- the inner list has 3 components:
    1. the added string after the previous multiplication
    2. the length of the string to be repeated (addedstring + multiplied string)
    3. the number of times to multiply the string by
* note: "a23" means "a" repeated 2 times, then repeated 3 times, resulting in 6 "a"

The string only needs to be decoded until the decoded string has length longer than k

To find the letter at k:
1. decrease k by 1 (to get the 0-based index)
2. take k to the modulo of the second value of the last item in the list created above
3. if k is within the last few indeces included by added string, find the corresponding letter at the index and return
4. remove the last item from the list and repeat steps 2 and 3 as needed


Runtime: O(N) where N is the length of string s
Space: O(N)
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        renderedLength = 0

        deconstructedString = []

        curString = ""
        curMultiplier = 1
        curIdx = 0
        while renderedLength < k:
            if curIdx < len(s):
                curChar = s[curIdx]
                if curChar.isalpha():
                    if curMultiplier > 1:
                        totalLength = len(curString)
                        if len(deconstructedString) > 0:
                            totalLength += deconstructedString[-1][1] * deconstructedString[-1][2]
                        deconstructedString.append([curString, totalLength, curMultiplier])
                        renderedLength = deconstructedString[-1][1] * deconstructedString[-1][2]
                        curString = ""
                        curMultiplier = 1
                    curString += curChar
                else:
                    curMultiplier *= int(curChar)
                curIdx += 1
            else:
                totalLength = len(curString)
                if len(deconstructedString) > 0:
                    totalLength += deconstructedString[-1][1] * deconstructedString[-1][2]
                deconstructedString.append([curString, totalLength, curMultiplier])
                renderedLength = deconstructedString[-1][1] * deconstructedString[-1][2]

        k -= 1
        found = False
        ans = ""

        while not found:
            k = k % deconstructedString[-1][1]
            if k >= deconstructedString[-1][1] - len(deconstructedString[-1][0]):
                k -= deconstructedString[-1][1] - len(deconstructedString[-1][0])
                ans = deconstructedString[-1][0][k]
                found = True

            deconstructedString.pop()

        return ans