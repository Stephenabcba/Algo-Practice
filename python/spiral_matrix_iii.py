# leetcode problem # 885. Spiral Matrix III

"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:
1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""

"""
My solution: Follow the Spiral

Observation: When travelling in a spiral, the traversed cells are constantly creating rectangles
- In the beginning, the rectangle has a length and width of 1 
- A turn is required if and only if a side of the rectangle is exceeded
    - this can happen when the current cell is in the grid or out of the grid
    - when the traversal moves out of the grid, multiple turns are usually needed
-> Follow the spiral, and make the turns as needed

Runtime: O(M * N) where M and N are the number of rows and columns
Space: O(1), memory usage does not depend on input
- this does not account for the space used for output
"""


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        edges = [cStart, rStart, cStart, rStart]
        limits = [cols - 1, rows - 1, 0, 0]

        ans = []
        dirIdx = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        curR = rStart
        curC = cStart

        def inBound(r, c):
            if limits[2] <= c <= limits[0]:
                if limits[3] <= r <= limits[1]:
                    return True
            return False

        def checkTurn(r, c):
            if dirIdx == 0:
                if c > edges[0]:
                    edges[0] += 1
                    return True
            elif dirIdx == 1:
                if r > edges[1]:
                    edges[1] += 1
                    return True
            elif dirIdx == 2:
                if c < edges[2]:
                    edges[2] -= 1
                    return True
            else:
                if r < edges[3]:
                    edges[3] -= 1
                    return True
            return False

        ans.append([curR, curC])
        for idx in range(cols * rows - 1):
            while not inBound(curR + directions[dirIdx][0], curC + directions[dirIdx][1]):
                dirIdx = (dirIdx + 1) % 4
                if dirIdx % 2:
                    curR = edges[dirIdx]
                else:
                    curC = edges[dirIdx]
            curR += directions[dirIdx][0]
            curC += directions[dirIdx][1]
            ans.append([curR, curC])
            if checkTurn(curR, curC):
                dirIdx = (dirIdx + 1) % 4

        return ans
