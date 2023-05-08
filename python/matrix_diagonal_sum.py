# leetcode problem # 1572. Matrix Diagonal Sum

"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


Example 1:
https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5

Constraints:
n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""

"""
My solution: 1 loop

On every row, 1-2 numbers are added to the sum
    - only the row where the secondary diagonal's value coincides with the primary
    diagonal have 1 value added to the sum
On the i-th row, the i-th value and n - i - 1'th value are added to the sum.
The sum can be calculated with a single loop. 

Runtime: O(N) where N is the length of matrix
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for idx in range(len(mat)):
            ans += mat[idx][idx]
            if idx != len(mat) - idx - 1:
                ans += mat[idx][len(mat) - idx - 1]
        return ans
