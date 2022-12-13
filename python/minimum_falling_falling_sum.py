# Leetcode problem # 931. Minimum Falling Path Sum

"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


Example 1:
https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""

"""
My solution: In-place minimum sum

Intuition: For every column of every row, pick the smallest sum available from the rows above
- the same sum from the row above can be used for multiple columns

Once a row is processed, the values in the row are no longer needed later in the algorithm,
so making modifications can be done in-place.

Logic:
1. Iterate through each row in the matrix and find the smallest running sum for each column in the row
- For the first row, the smallest running sum of each column is itself
- For every row after, the smallest running sum is the comlumn itself + minimum of the following:
    i. value directly above
    ii. value diagonally left above
    iii. value diagonally right above
    * for values on the left and right edge, only consider the 2 valid values above it
2. Find the smallest running sum on the last row of the matrix

Runtime: O(N^2) where N is the length of the square matrix
Space: O(1), Modifications are done in-place
"""


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(0, len(matrix[0])):
                if col == 0:
                    matrix[row][col] += min(matrix[row - 1]
                                            [col], matrix[row - 1][col + 1])
                elif col == len(matrix[0]) - 1:
                    matrix[row][col] += min(matrix[row - 1]
                                            [col - 1], matrix[row - 1][col])
                else:
                    matrix[row][col] += min(matrix[row - 1][col - 1],
                                            matrix[row - 1][col], matrix[row - 1][col + 1])
        return min(matrix[len(matrix) - 1])
