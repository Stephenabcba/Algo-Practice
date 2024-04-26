# leetcode problem # 1289. Minimum Falling Path Sum II

"""
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:
https://assets.leetcode.com/uploads/2021/08/10/falling-grid.jpg
Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:
Input: grid = [[7]]
Output: 7

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""

"""
My solution: Keep track of the 2 smallest sums at each row

Observation: The choices at each row are only limited by the columns
chosen by the previous rows
-> Only need to keep the lowest 2 sums at 2 different columns
    - if the next row has a column that matches with the lowest sum, it can
    choose the second lowest instead

Logic:
1. Keep track of the 2 lowest sums up to the previous row
    - also keep track of the column the sums ended with
2. Iterate through each row
    i. keep track of the 2 lowest sums of the row, and their associated columns
    ii. iterate through each column in the row 
        - if the current column number does not match with the previous smallest sum's, add the current value to
            that of the previous smallest sum
        - otherwise, add the current value to the previous second smallest sum
        - update the 2 lowest sums of the row with the current sum if needed
    ii. update the overall lowest sums with the outcome of the current row
3. Return the smallest sum at the end


Runtime: O(N^2) where N is the width (or height) of the grid
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        smallest = 0
        smallestIdx = -1
        secondSmallest = 0
        secondSmallestIdx = -1

        for row in range(len(grid)):
            newSmallest = 10000000
            newSmallestIdx = -1
            newSecondSmallest = 10000000
            newSecondSmallestIdx = -1
            for col in range(len(grid)):
                cur = grid[row][col]
                if col == smallestIdx:
                    cur += secondSmallest
                else:
                    cur += smallest

                if cur < newSmallest:
                    newSecondSmallest = newSmallest
                    newSecondSmallestIdx = newSmallestIdx
                    newSmallest = cur
                    newSmallestIdx = col
                elif cur < newSecondSmallest:
                    newSecondSmallest = cur
                    newSecondSmallestIdx = col
            smallest = newSmallest
            smallestIdx = newSmallestIdx
            secondSmallest = newSecondSmallest
            secondSmallestIdx = newSecondSmallestIdx

        return smallest
