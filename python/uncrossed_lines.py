# leetcode problem # 1035. Uncrossed Lines

"""
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.


Example 1:
https://assets.leetcode.com/uploads/2019/04/26/142.png
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2

Constraints:
1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
"""

"""
My solution: Dynamic Programming

Idea: greedily connect the lines when the numbers match up
- increment the pointer on both lists when they match
- increment one of the pointers and check again when they don't match
Problem: which pointer should be incremented when the numbers don't match?
-> try both combinations

Iterative DP solution:
At any state, there's only 1-2 available steps
- if the numbers match, the only step is to increment both pointers and increase the number of connected lines
- if the numbers don't match, either increment num1 or increment nums2
-> At any state that's not a first step, there's at most 3 steps that can be taken to reach the current state
    - choose the path that makes the most connections

Runtime: O(M * N) where M and N are lengths of lists nums1 and nums2 respectively
Space: O(M * N)
"""


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        memo = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

        for idx1 in range(0, m + 1):
            for idx2 in range(0, n + 1):
                if idx1 > 0 and idx2 > 0:
                    memo[idx2][idx1] = max(
                        memo[idx2][idx1], memo[idx2 - 1][idx1], memo[idx2][idx1 - 1])
                if idx1 < m and idx2 < n:
                    if nums1[idx1] == nums2[idx2]:
                        memo[idx2 + 1][idx1 + 1] = memo[idx2][idx1] + 1

        return memo[n][m]
