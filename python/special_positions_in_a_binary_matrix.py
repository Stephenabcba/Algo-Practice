# leetcode problem # 1582. Special Positions in a Binary Matrix

"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
https://assets.leetcode.com/uploads/2021/12/23/special1.jpg
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
"""

"""
My solution: Pre-process

To quickly check whether a position is special, count the number of 1's in each row and column
- if a row/column has more than 1 1's, none of the positions in that row/column can be special

Pass through the matrix a second time to find all the special positions.


Runtime: O(M * N) where M and N are the number of rows and columns in the matrix
Space: O(M + N)
"""


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSums = [0 for _ in mat]
        colSums = [0 for __ in mat[0]]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                rowSums[row] += mat[row][col]
                colSums[col] += mat[row][col]

        ans = 0
        for row in range(len(mat)):
            if rowSums[row] == 1:
                for col in range(len(mat[0])):
                    if colSums[col] == 1 and mat[row][col] == 1:
                        ans += 1

        return ans
