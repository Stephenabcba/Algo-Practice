# leetcode problem # 1219. Path with Maximum Gold

"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""

"""
My solution: DFS

Check each path in the 4 direction, and choose the path with the largest gold yield
- to avoid traversing to the same cell multiple times, temporarily set the current cell to 0
    - reset the value after checking the 4 directions


Runtime: O(g * 4^ g + M * N) where g is the number of gold cells, M and N are the number of rows and columns
Space: O(g)
"""


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        highest = 0

        def traverse(row, col):
            temp, grid[row][col] = grid[row][col], 0
            total = 0

            if row - 1 >= 0 and grid[row - 1][col] != 0:
                total = max(total, traverse(row - 1, col))
            if row + 1 < rows and grid[row + 1][col] != 0:
                total = max(total, traverse(row + 1, col))
            if col - 1 >= 0 and grid[row][col - 1] != 0:
                total = max(total, traverse(row, col - 1))
            if col + 1 < cols and grid[row][col + 1] != 0:
                total = max(total, traverse(row, col + 1))
            total += temp
            grid[row][col] = temp
            return total

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    highest = max(highest, traverse(row, col))

        return highest
