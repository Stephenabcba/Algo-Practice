# leetcode problem # 712. Minimum ASCII Delete Sum for Two Strings

"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""

"""
Solution by leetcode: Bottom-up dynamic programming (Space-optimized)

The bellman equation for the recurrance relation logic is as follows:
C(i,j) =    0                                                   if i = 0 and j = 0
            A(s2[j-1]) + C(i, j-1)                              if i = 0
            A(s1[i-1]) + C(i-1, j)                              if j = 0
            C(i-1, j-1)                                         if s1[i-1] = s2[j-1]
            min(A(s1[i-1]) + C(i-1, j), A(s2[j-1]) + C(i,j-1))  otherwise

Where A(x) is the ASCII value of character x
and C(i, j) is computeCost(i,j), which returns the minimum ascii delete sum for s1 up to index i and s2 up to index j

Implement the bellman equation to find the answer, which is C(m, n)

Space Optimization: After close analysis (by leetcode editor), the values of each row only directly depends on
the values of the previous row (and no other rows), and thus only 1 row of dp needs to be saved.
- the old rows can be discarded after the current row has been processed.

* https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/editorial/
The editorial shows the entire thought process of starting with the brute force solution then optimizing
to the current solution.

Runtime: O(M * N), where M and N are the lengths of s1 and s2, respectively
Space: O(min(M, N))
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # Make sure s2 is smaller string
        if len(s1) < len(s2):
            return self.minimumDeleteSum(s1 = s2, s2 = s1)
        
        # Case for empty s1
        m, n = len(s1), len(s2)
        curr_row = [0] * (n + 1)
        for j in range(1, n + 1):
            curr_row[j] = curr_row[j - 1] + ord(s2[j - 1])
        
        # Compute answer row-by-row
        for i in range(1, m + 1):
            
            diag = curr_row[0]
            curr_row[0] += ord(s1[i - 1])

            for j in range(1, n + 1):
                
                # If characters are the same, the answer is top-left-diagonal value
                if s1[i - 1] == s2[j - 1]:
                    answer = diag
                
                # Otherwise, the answer is minimum of top and left values with
                # deleted character's ASCII value
                else:
                    answer = min(
                        ord(s1[i - 1]) + curr_row[j],
                        ord(s2[j - 1]) + curr_row[j - 1]
                    )

                # Before overwriting curr_row[j] with the answer, save it in diag
                # for the next column
                diag = curr_row[j]
                curr_row[j] = answer
        
        # Return answer
        return curr_row[-1]