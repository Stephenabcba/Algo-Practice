# leetcode problem # 2812. Find the Safest Path in a Grid

"""
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

A cell containing a thief if grid[r][c] = 1
An empty cell if grid[r][c] = 0
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.


Example 1:
https://assets.leetcode.com/uploads/2023/07/02/example1.png
Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

Example 2:
https://assets.leetcode.com/uploads/2023/07/02/example2.png
Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Example 3:
https://assets.leetcode.com/uploads/2023/07/02/example3.png
Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Constraints:
1 <= grid.length == n <= 400
grid[i].length == n
grid[i][j] is either 0 or 1.
There is at least one thief in the grid.
"""

"""
My solution: BFS

Using BFS, the safeness factor of each location in the grid can be found
- Initialize the queue with all locations with thieves, then explore the grid with BFS

Using BFS again, the safest path can be found from the top left to the bottom right
- to ensure that the safest path is taken through each location, a tiered queue is used
    - every new block to be explored is grouped by the safeness factor, and the safest blocks
    are explored first

BFS can be skipped if there's a thief at the start or the end location

Return the safest path at the end, or 0 if there is no path from start to end without going through
a thief

Runtime: O(N^2) where N is the sidelengths of the grid
Space: O(N^2)
"""


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        rows, cols = len(grid), len(grid[0])
        mapSafeness = [[-1 for _ in range(cols)] for __ in range(rows)]

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    mapSafeness[row][col] = 0
                    queue.append((row, col, 0))
                grid[row][col] = -1

        while len(queue) > 0:
            cRow, cCol, safeness = queue.popleft()
            if cRow - 1 >= 0 and mapSafeness[cRow - 1][cCol] < 0:
                mapSafeness[cRow - 1][cCol] = safeness + 1
                queue.append((cRow - 1, cCol, safeness + 1))
            if cCol - 1 >= 0 and mapSafeness[cRow][cCol - 1] < 0:
                mapSafeness[cRow][cCol - 1] = safeness + 1
                queue.append((cRow, cCol - 1, safeness + 1))
            if cRow + 1 < rows and mapSafeness[cRow + 1][cCol] < 0:
                mapSafeness[cRow + 1][cCol] = safeness + 1
                queue.append((cRow + 1, cCol, safeness + 1))
            if cCol + 1 < cols and mapSafeness[cRow][cCol + 1] < 0:
                mapSafeness[cRow][cCol + 1] = safeness + 1
                queue.append((cRow, cCol + 1, safeness + 1))

        grid[0][0] = mapSafeness[0][0]
        queue = [deque() for _ in range(grid[0][0])]
        queue[-1].append((0, 0))

        while len(queue) > 0:
            cRow, cCol = queue[-1].popleft()
            safeness = grid[cRow][cCol]
            if cRow - 1 >= 0 and mapSafeness[cRow - 1][cCol] > 0 and grid[cRow - 1][cCol] < 0:
                grid[cRow - 1][cCol] = min(safeness,
                                           mapSafeness[cRow - 1][cCol])
                queue[grid[cRow - 1][cCol] - 1].append((cRow - 1, cCol))
            if cCol - 1 >= 0 and mapSafeness[cRow][cCol - 1] > 0 and grid[cRow][cCol - 1] < 0:
                grid[cRow][cCol - 1] = min(safeness,
                                           mapSafeness[cRow][cCol - 1])
                queue[grid[cRow][cCol - 1] - 1].append((cRow, cCol - 1))
            if cRow + 1 < rows and mapSafeness[cRow + 1][cCol] > 0 and grid[cRow + 1][cCol] < 0:
                grid[cRow + 1][cCol] = min(safeness,
                                           mapSafeness[cRow + 1][cCol])
                queue[grid[cRow + 1][cCol] - 1].append((cRow + 1, cCol))
            if cCol + 1 < cols and mapSafeness[cRow][cCol + 1] > 0 and grid[cRow][cCol + 1] < 0:
                grid[cRow][cCol + 1] = min(safeness,
                                           mapSafeness[cRow][cCol + 1])
                queue[grid[cRow][cCol + 1] - 1].append((cRow, cCol + 1))
            while len(queue) > 0 and len(queue[-1]) == 0:
                queue.pop()

        return max(grid[-1][-1], 0)
