# leetcode problem # 840. Magic Squares In Grid

"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

Example 1:
https://assets.leetcode.com/uploads/2020/09/11/magic_main.jpg
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
https://assets.leetcode.com/uploads/2020/09/11/magic_valid.jpg
while this one is not:
https://assets.leetcode.com/uploads/2020/09/11/magic_invalid.jpg
In total, there is only one magic square inside the given grid.

Example 2:
Input: grid = [[8]]
Output: 0

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""

"""
My solution: Check Every 3x3 with preprocessing

Preprocessing:
1. Find the sum of every row of 3 cells
2. Find the sum of every column of 3 cells
3. Find the sum of every diagonal of 3 cells
4. Find the sum of every diagonal (opposite direciton) of 3 cells
-> By preprocessing, redundant checks are eliminated during iteration

Checking:
1. Make sure that the 3x3 only contains distint values from 1-9
2. Make sure that the sums across all rows, columns, and diagonals are the same
    - the values can be taken from those saved during preprocessing

Runtime: O(M * N) Where N and M are the number of rows and columns
Space: O(M * N)
"""


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0

        rowSums = [[-1 for _ in range(m)] for __ in range(n)]
        colSums = [[-1 for _ in range(m)] for __ in range(n)]
        diagSums = [[-1 for _ in range(m)] for __ in range(n)]
        revDiagSums = [[-1 for _ in range(m)] for __ in range(n)]

        for row in range(n):
            rowSum = grid[row][0] + grid[row][1] + grid[row][2]
            rowSums[row][0] = rowSum
            for col in range(1, m - 2):
                rowSum -= grid[row][col - 1]
                rowSum += grid[row][col + 2]
                rowSums[row][col] = rowSum

        for col in range(m):
            colSum = grid[0][col] + grid[1][col] + grid[2][col]
            colSums[0][col] = colSum
            for row in range(1, n - 2):
                colSum -= grid[row - 1][col]
                colSum += grid[row + 2][col]
                colSums[row][col] = colSum

        for row in range(n - 2):
            for col in range(m - 2):
                diagSums[row][col] = grid[row][col] + \
                    grid[row + 1][col + 1] + grid[row + 2][col + 2]

        for row in range(n - 2):
            for col in range(2, m):
                revDiagSums[row][col] = grid[row][col] + \
                    grid[row + 1][col - 1] + grid[row + 2][col - 2]

        ans = 0
        for row in range(n - 2):
            for col in range(m - 2):
                numCheck = [0] * 10
                for idx in range(3):
                    for jdx in range(3):
                        cur = grid[row + idx][col + jdx]
                        if cur > 9:
                            numCheck[0] += 1
                        else:
                            numCheck[cur] += 1
                isValid = True
                if numCheck[0] > 0:
                    isValid = False
                for idx in range(1, 10):
                    if numCheck[idx] != 1:
                        isValid = False
                        break

                if isValid:
                    target = rowSums[row][col]
                    if target == rowSums[row + 1][col] == rowSums[row + 2][col] == colSums[row][col] == colSums[row][col + 1] == colSums[row][col + 2] == diagSums[row][col] == revDiagSums[row][col + 2]:
                        ans += 1

        return ans
