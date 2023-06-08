# leetcode problem # 1351. Count Negative Numbers in a Sorted Matrix

"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""

"""
My solution: brute force count all the negatives

go through each value and count the negative numbers

Runtime: O(M*N) where M and N are the sidelengths of the grid
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negativeCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    negativeCount += 1

        return negativeCount
    
"""
Solution by leetcode: Linear Traversal

Making use of the fact that the grid is sorted in both directions, the logic can be done
in linear time
    - if a value is negative in row i col j, the values in row i col j + x and row i + x col j must all be
    negative

Runtime: O(M + N) where M and N are the sidelengths of the grid
Space: O(1)
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        currRowNegativeIndex = n - 1

        # Iterate on all rows of the matrix one by one.
        for row in grid:
            # Decrease 'currRowNegativeIndex' so that it points to current row's last positive element.
            while currRowNegativeIndex >= 0 and row[currRowNegativeIndex] < 0:
                currRowNegativeIndex -= 1
            # 'currRowNegativeIndex' points to the last positive element,
            # which means 'n - (currRowNegativeIndex + 1)' is the number of all negative elements.
            count += (n - (currRowNegativeIndex + 1))
        return count