# leetcode problem # 1647. Minimum Deletions to Make Character Frequencies Unique

"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
Input: s = "aab"
Output: 0
Explanation: s is already good.

Example 2:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:
Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
"""

"""
My solution: Count and delete

Logic:
1. Make a count of each letter in the string
2. Sort the counts from smallest to largest
3. Compress the list of counts into a stack
    - each item in the stack has two elements: value and count
        - the value is the frequency of a letter that appeared
        - the count is the number of times that frequency exists in the list of counts
    - the stack remains sorted, where the top of the stack always has the largest value (regardless of count)
4. Iterate until the stack is empty:
    i. pop from the top of the stack
        - if the count of the popped item > 1, letters must be removed
        - if the count == 1, nothing needs to be done
    ii. remove count - 1 letters
        - keep track of the total number of removed values
    iii. add the decremented values back to the stack
        - if the decremented value is 0, don't add them back
        - if the decremented value is already at the top of the stack, add to that item
        - otherwise, add a new item to the top of the stack as [value - 1, count - 1]
5. return the total number of removed letters

Runtime: O(N + k log k) where N is the length of the input string s, and k is the number of available characters
- since k is a constant of 26 in this problem, this could be simplied to O(N)
Space: O(k)
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = [0] * 26

        for letter in s:
            frequencies[ord(letter) - ord('a')] += 1

        frequencies.sort()

        freqStack = []

        curVal = -1
        curCount = 0

        for frequency in frequencies:
            if frequency > 0:
                if frequency == curVal:
                    curCount += 1
                else:
                    if curCount > 0:
                        freqStack.append([curVal, curCount])
                    curVal = frequency
                    curCount = 1
        freqStack.append([curVal, curCount])

        ans = 0

        while len(freqStack) > 0:
            curVal, curCount = freqStack.pop()
            if curCount > 1:
                ans += curCount - 1
                if curVal - 1 > 0:
                    if len(freqStack) > 0 and freqStack[-1][0] == curVal - 1:
                        freqStack[-1][1] += curCount - 1
                    else:
                        freqStack.append([curVal - 1, curCount - 1])

        return ans