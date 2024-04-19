# leetcode problem # 200. Number of Islands

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

"""
My solution: Breadth-First Search

Idea: Iterate through each square of the grid, and count the number of islands found
- Explore each island found before the next iteration, and mark the squares of the island as visited
- If a square of unvisited land is found during iteration, a new island is found

Both BFS and DFS will explore the islands, BFS is arbitrarily chosen here

Runtime: O(M * N) where M and N are the number of rows and columns in grid
Space: O(M * N)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for __ in grid]

        islands = 0

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    queue.append((row, col))
                    visited[row][col] = True
                    islands += 1
                    while len(queue) > 0:
                        r, c = queue.popleft()
                        if r - 1 >= 0 and grid[r - 1][c] == "1" and not visited[r - 1][c]:
                            queue.append((r - 1, c))
                            visited[r - 1][c] = True
                        if c - 1 >= 0 and grid[r][c - 1] == "1" and not visited[r][c - 1]:
                            queue.append((r, c - 1))
                            visited[r][c - 1] = True
                        if r + 1 < rows and grid[r + 1][c] == "1" and not visited[r + 1][c]:
                            queue.append((r + 1, c))
                            visited[r + 1][c] = True
                        if c + 1 < cols and grid[r][c + 1] == "1" and not visited[r][c + 1]:
                            queue.append((r, c + 1))
                            visited[r][c + 1] = True

        return islands
