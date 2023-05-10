# leetcode problem # 59. Spiral Matrix II

"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
"""

"""
My solution: Generate empty matrix then fill

Generate an empty matrix of size N x N, so it's easier to fill with values

Traverse in the spiral order and fill in the values accordingly

Runtime: O(N ^ 2) where N is the input integer n
Space: O(1), besides the output matrix, the memory usage does not depend on input
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for __ in range(n)]

        curVal = 1
        rowStart = 0
        rowEnd = n
        colStart = 0
        colEnd = n
        direction = 0

        while curVal <= n ** 2:
            if direction == 0:
                for idx in range(colStart, colEnd):
                    ans[rowStart][idx] = curVal
                    curVal += 1
                rowStart += 1
            elif direction == 1:
                for idx in range(rowStart, rowEnd):
                    ans[idx][colEnd - 1] = curVal
                    curVal += 1
                colEnd -= 1
            elif direction == 2:
                for idx in range(colEnd - 1, colStart - 1, -1):
                    ans[rowEnd - 1][idx] = curVal
                    curVal += 1
                rowEnd -= 1
            elif direction == 3:
                for idx in range(rowEnd - 1, rowStart - 1, -1):
                    ans[idx][colStart] = curVal
                    curVal += 1
                colStart += 1
            direction += 1
            direction %= 4
        return ans
