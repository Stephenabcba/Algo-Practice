# leetcode problem # 1091. Shortest Path in Binary Matrix

"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.


Example 1:
https://assets.leetcode.com/uploads/2021/02/18/example1_1.png
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
https://assets.leetcode.com/uploads/2021/02/18/example2_1.png
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

"""
My solution: BFS

In essence, the problem is a shortest path graph problem.
Using BFS, the logic can find the shortest path from the top left square to any square in the grid, including the bottom right square
- Due to the nature of BFS, the first time a square is "seen" is a shortest path from the initial square to the target square
** Note that DFS will also find a path from start to end, but in general graphs DFS will not always find the shortest path.


Runtime: O(N ^ 2) where N is the side length of the grid
Space: O(N ^ 2)
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in grid[0]] for __ in grid]
        distances = [[-1 for _ in grid[0]] for __ in grid]
        maxRows = len(grid)
        maxCols = len(grid[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        if grid[0][0] == 1:
            return -1
        else:
            distances[0][0] = 1

        queue = [(0, 0)]
        queueIdx = 0
        visited[0][0] = True

        while queueIdx < len(queue):
            curRow, curCol = queue[queueIdx]
            for direction in directions:
                row = curRow + direction[0]
                col = curCol + direction[1]
                if row >= 0 and col >= 0 and row < maxRows and col < maxCols:
                    if not visited[row][col]:
                        visited[row][col] = True
                        if grid[row][col] == 0:
                            distances[row][col] = distances[curRow][curCol] + 1
                            queue.append((row, col))
            queueIdx += 1
        return distances[-1][-1]