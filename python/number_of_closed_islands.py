# leetcode problem # 1254. Number of Closed Islands

"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.


Example 1:
https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

"""
My solution: DFS

DFS is a good option to traverse through all the connected land and check if the criteria is met
for a closed island
The main condition for a closed island is that the land does not touch any of the edges
- as long as the island does not touch an edge anywhere, it is a closed island.
    -> if the traversal travels out of bounds, the island is touching an edge, and thus is not a closed island
- when the traversal meets water, it can stop traversing, but is undetermined on whether the island is closed

DFS is initiated on all unvisited lands to check whether each one is a closed island
- as DFS traverses through all sections of connected lands, DFS would not be initiated more than
once on the same island

Runtime: O(N * M) where N is the number of rows and M is the number of columns in the grid
Space: O(N * M)
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in grid[0]] for __ in grid]
        numRows = len(grid)
        numCols = len(grid[0])

        def traverse(r, c):
            if r < 0 or r >= numRows or c < 0 or c >= numCols:
                return False
            if visited[r][c]:
                return True
            visited[r][c] = True
            if grid[r][c] == 1:
                return True
            up = traverse(r - 1, c)
            down = traverse(r + 1, c)
            left = traverse(r, c - 1)
            right = traverse(r, c + 1)
            return up and down and left and right

        ans = 0

        for row in range(numRows):
            for col in range(numCols):
                if not visited[row][col] and grid[row][col] == 0:
                    if traverse(row, col):
                        ans += 1

        return ans
