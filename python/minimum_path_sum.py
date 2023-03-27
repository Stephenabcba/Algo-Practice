# leetcode problem # 64. Minimum Path Sum

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""

"""
My solution: Space-Optimized DP

Intuition:
Given the problem movement constraints (only right or down), the minimum path to any square
is the value of the square + the minimum of the minimum path to the square above or to the left
(if either are available)
- edge cases:
    1. the square is on the top edge; the minimum path is only from the left
    2. the square is on the left edge; the minimum path is only from the top

Solution: starting from the top left, iterate through each square (left->right, top->bottom)
until the bottom left is reached. Keep track of the minimum path to every square in a DP matrix.
The minimum path of the bottom right square is the value at the bottom right of the DP matrix.

Space Optimization: With the current iteration pattern, only the minimum path to the previous row
needs to be saved. Instead of using an entire matrix, 1 DP row can be used instead, replacing values
during iteration.
The minimum path of the bottom right square is the last value of the DP row at the end of iteration.

Runtime: O(M*N) where M is the number of rows and N is the number of columns
Space: O(N)
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        history = [0 for _ in grid[0]]

        history[0] = grid[0][0]
        for idx, val in enumerate(grid[0]):
            if idx > 0:
                history[idx] = history[idx - 1] + val

        for row in range(1, len(grid)):
            for idx, val in enumerate(grid[row]):
                if idx == 0:
                    history[idx] = history[idx] + val
                else:
                    history[idx] = min(history[idx - 1], history[idx]) + val

        return history[-1]
