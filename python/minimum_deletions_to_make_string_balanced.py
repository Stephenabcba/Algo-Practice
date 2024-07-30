# leetcode problem # 1653. Minimum Deletions to Make String Balanced

"""
You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Example 1:
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

Constraints:
1 <= s.length <= 10^5
s[i] is 'a' or 'b'
"""

"""
My solution: Two lists

For each letter, consider both the cases of keeping or deleting it
- If the letter is 'a', there can be no 'b' before it
- If the letter is 'b', there can be no 'a' after it
-> keep 2 lists of results, either ending with a or ending with b
    - if the letter at idx is 'a', increment the value at idx of the list ending with a
    - if the letter at idx is 'b', increase the value at idx of the list ending with b
        - the value is higher of the idx - 1 of list ending with a and the idx - 1 of the list ending with b
            - add 1 to either of those values

Runtime: O(N) where N is the length of string s
Space: O(N)
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        endingWithA = [0] * n
        endingWithB = [0] * n

        for idx in range(n):
            if s[idx] == "a":
                if idx == 0:
                    endingWithA[0] = 1
                else:
                    endingWithA[idx] = endingWithA[idx - 1] + 1
                    endingWithB[idx] = endingWithB[idx - 1]
            else:  # b
                if idx == 0:
                    endingWithB[0] = 1
                else:
                    endingWithA[idx] = endingWithA[idx - 1]
                    endingWithB[idx] = max(
                        endingWithA[idx - 1], endingWithB[idx - 1]) + 1

        return min(n - endingWithA[-1], n - endingWithB[-1])


"""
Modification: Eliminating List

Upon referencing leetcode solutions, it was discovered that the lists were not necessary.
-> in all cases, each iteration only depends on the values of the previous iteration; all iterations before do not need to be saved

Runtime: O(N)
Space: O(1)
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        endingWithA = 0
        endingWithB = 0

        for idx in range(n):
            if s[idx] == "a":
                if idx == 0:
                    endingWithA = 1
                else:
                    endingWithA += + 1
            else:  # b
                if idx == 0:
                    endingWithB = 1
                else:
                    endingWithB = max(endingWithA, endingWithB) + 1

        return min(n - endingWithA, n - endingWithB)
