# leetcode problem # 2352. Equal Row and Column Pairs

"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
"""

"""
My solution: Use dictionary

use a dictionary to keep track of what rows have been seen, if there's duplicate rows, increase the count for that row
compare the columns to the rows in the dictionary, if any matches, increase the total count by the value in the dictionary
    - ex: if there's 2 rows that matches with the column, increase the count by 2
return the the total count at the end

Runtime: O(N^2) where N is the sidelength of the grid
Space: O(N^2)
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowCounts = {}

        for row in grid:
            tupleRow = tuple(row)
            if tupleRow not in rowCounts:
                rowCounts[tupleRow] = 0
            rowCounts[tupleRow] += 1

        totalPairs = 0

        for idx in range(len(grid[0])):
            curCol = []
            for rowVal in range(len(grid)):
                curCol.append(grid[rowVal][idx])
            tupleCol = tuple(curCol)
            totalPairs += rowCounts.get(tupleCol, 0)

        return totalPairs