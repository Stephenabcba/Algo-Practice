# leetcode problem # 463. Island Perimeter

"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:
https://assets.leetcode.com/uploads/2018/10/12/island.png
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""

"""
My solution: Recursive Traversal

Find the first square of the island in the grid, then explore the island starting from that grid
- For every square of the island found, check the 4 sides
    - if a side is neighboring water, add 1 to the perimeter
    - if a side is neighboring an unexplored part of the island, explore that square

- To keep track of which squres are visited, create another matrix the same size as the grid
    - if a land tile is visited, mark it as visited in the matrix

- It is possible to create a solution that just iterates through every square on the island and check all 4 sides
of each land tile

Runtime: O(M*N) where M and N are the number of rows and columns in the grid
Space: O(M*N)
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in grid[0]] for __ in grid]

        def traverse(row, col):
            perimeter = 0

            visited[row][col] = True

            if row - 1 < 0 or grid[row - 1][col] == 0:
                perimeter += 1
            elif not visited[row - 1][col]:
                perimeter += traverse(row - 1, col)

            if col - 1 < 0 or grid[row][col - 1] == 0:
                perimeter += 1
            elif not visited[row][col - 1]:
                perimeter += traverse(row, col - 1)

            if row + 1 > len(grid) - 1 or grid[row + 1][col] == 0:
                perimeter += 1
            elif not visited[row + 1][col]:
                perimeter += traverse(row + 1, col)

            if col + 1 > len(grid[0]) - 1 or grid[row][col + 1] == 0:
                perimeter += 1
            elif not visited[row][col + 1]:
                perimeter += traverse(row, col + 1)

            return perimeter

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return traverse(row, col)

        return 0
