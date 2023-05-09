# leetcode problem # 54. Spiral Matrix

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

"""
My solution: Process 1 row/column at a time

The spiral cycles through the 4 sides:
- top row going right
- right column going down
- bottom row going left
- left column going up

After adding the values to the answer list, the values in the
row / column would not be accessed again, so the boundaries of the
remaining values can be modified
- at any given time, the remaining values would form a rectangle, and can be
marked with its 4 vertices

Runtime: O(M * N) where M and N are the sidelengths of the matrix
Space: O(1), excluding the output, memory usage does not depend on input.
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        colStart = 0
        m = len(matrix)
        rowEnd = m
        n = len(matrix[0])
        colEnd = n

        ans = []
        direction = 0
        while len(ans) < m * n:
            if direction == 0:
                for idx in range(colStart, colEnd):
                    ans.append(matrix[rowStart][idx])
                rowStart += 1
            elif direction == 1:
                for idx in range(rowStart, rowEnd):
                    ans.append(matrix[idx][colEnd - 1])
                colEnd -= 1
            elif direction == 2:
                for idx in range(colEnd - 1, colStart - 1, -1):
                    ans.append(matrix[rowEnd - 1][idx])
                rowEnd -= 1
            elif direction == 3:
                for idx in range(rowEnd - 1, rowStart - 1, -1):
                    ans.append(matrix[idx][colStart])
                colStart += 1
            direction += 1
            direction %= 4

        return ans
