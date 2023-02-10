# leetcode problem # 1162. As Far from Land as Possible

"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.


Example 1:
https://assets.leetcode.com/uploads/2019/05/03/1336_ex1.JPG
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
https://assets.leetcode.com/uploads/2019/05/03/1336_ex2.JPG
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

"""
Solution by Leetcode: Dynamic Programming

Intuition:
- In essence, the problem is looking for the highest minimum distance from a block of water to a block of land
- If all other distances are known, the minimum distance from a given square to the closest land is 1 + the minimum of
the squares above, below, left, right


Other notes:
- All lands have a 0 distance from land
- Due to iteration constraints, if iterating from top left to bottom right, the distances below and to the right of each
square is unknown
    - if iteration from bottom right to top left, the distances above and to the left of each square is unknown
-> perform 2 passes through the matrix, once from top left to bottom right, and once from bottom right to top left to
find the distances from all 4 directions
    - On the first pass, only check the neighboring squares above and to the left of the current square
    - On the second pass, the distance calculated on each square is the real minimum distance from the block to land
        - find the maximum of these distances on the second pass

Runtime: O(N ^ 2) where N is the side length of the matrix grid
Space: O(N ^ 2)
"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxDistance = rows + cols + 1

        dist = [[maxDistance for col in range(cols)] for row in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    dist[i][j] = 0
                else:
                    dist[i][j] = min(dist[i][j], min(
                        dist[i - 1][j] + 1 if i > 0 else maxDistance, dist[i][j - 1] + 1 if j > 0 else maxDistance))

        ans = float('-inf')

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                dist[i][j] = min(dist[i][j], min(dist[i + 1][j] + 1 if i < rows -
                                 1 else maxDistance, dist[i][j + 1] + 1 if j < cols - 1 else maxDistance))

                ans = max(ans, dist[i][j])

        return -1 if ans == maxDistance or ans == 0 else ans
