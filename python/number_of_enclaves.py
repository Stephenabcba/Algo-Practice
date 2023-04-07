# leetcode problem # 1020. Number of Enclaves

"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


Example 1:
https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""


"""
My solution: DFS with 2 return values

Modifying the DFS solution for 1254. Number of Closed Islands, the algorithm can count the number of land tiles
on the valid islands.
- In the first solution, the algorithm returns True if the land could be an island, and False if the land cannot be
a closed island
    - by modifying the return value, the solution can keep track of the number of tiles in the island
        - the function would return a tuple, containing the boolean from the original return value, and a second integer
        keeping track of the number of tiles on the island
            - the integer would be the sum of the return values of traversal in all 4 directions, +1 for the tile itself.
                - if the tile is already visited or is in water, return (True, 0)
            - if the coordinates are out of bounds, return (False, 0)
            - if any of the tiles invalidates the closed island condition, return (False, 0)

Runtime: O(N * M) where N is the number of columns and M is the number of rows in the grid.
Space: O(N * M)
"""


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in grid[0]] for __ in grid]
        numRows = len(grid)
        numCols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= numRows or c < 0 or c >= numCols:
                return (False, 0)
            if visited[r][c]:
                return (True, 0)
            visited[r][c] = True
            if grid[r][c] == 0:
                return (True, 0)

            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            if up[0] and down[0] and left[0] and right[0]:
                return (True, up[1] + down[1] + left[1] + right[1] + 1)

            return (False, 0)

        ans = 0

        for row in range(numRows):
            for col in range(numCols):
                if not visited[row][col] and grid[row][col] == 1:
                    ans += dfs(row, col)[1]

        return ans
