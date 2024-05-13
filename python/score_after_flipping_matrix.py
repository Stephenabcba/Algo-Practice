# leetcode problem # 861. Score After Flipping Matrix

"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Example 1:
https://assets.leetcode.com/uploads/2021/07/23/lc-toogle1.jpg
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
"""

"""
My solution: Maximize 1s in each column

Properties of binaries:
1. The value of a bit is larger than sum of all bits after it
    - ex: 1000 (8) is larger than 0111 (7)
2. The value of a bit is always the same in the same place
    - ex: 0100 == 0100
    - ex2: 1011 + 0100 == 1111 + 0000
        - moving the second bit (the bit with a value of 4) yields the same sum

Goal to maximize the output:
1. Ensure the largest bits of all numbers are all 1s
2. Maximize the number of 1 bits in each column

Implementation:
1. Flip any row with leading 0's
2. Iterate through each column after the first
    - count the number of 1's in the column
    - if the number of 1's is less than half of the number of rows, flip
    the column
    - calculate the value represented in the column and add to total
        - each 1 bit holds a value depending on its position in the row
        - multiply the value of 1 bit by the count of 1 bits
3. Return the total value


Runtime: O(M*N) where M and N are the number
Space: O(1), memory usage does not depend on input
- The input matrix is altered during iteration
"""


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            if grid[row][0] == 0:
                for col in range(cols):
                    grid[row][col] = 1 if grid[row][col] == 0 else 0

        total = 0
        total += (1 << cols - 1) * rows

        for col in range(1, cols):
            colOnes = 0
            for row in range(rows):
                colOnes += grid[row][col]
            colOnes = max(colOnes, rows - colOnes)
            total += (1 << (cols - col - 1)) * colOnes

        return total
