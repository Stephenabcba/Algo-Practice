# leetcode problem # 74. Search a 2D Matrix

"""
You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
https://assets.leetcode.com/uploads/2020/10/05/mat.jpg
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

"""
My solution: Binary Search twice

Due to the construction of the matrix, the values in each row are always larger than value in any previous
rows.
Moreover, the start of each row is in strictly increasing order from top to bottom.

A binary search can first be conducted to find the correct row that the target is in, then a second binary search
can be conducted to find the target.
Return True if target is found, False otherwise.

Runtime: O(logM + logN) where M is the number of rows and N is the number of columns in the matrix
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start < end:
            mid = ceil((start + end) / 2)
            if target >= matrix[mid][0]:
                start = mid
            else:
                end = mid - 1

        targetRow = end

        if target > matrix[targetRow][-1]:
            return False
        
        start = 0
        end = len(matrix[0])

        while start < end:
            mid = (start + end) // 2
            if target == matrix[targetRow][mid]:
                return True
            elif target > matrix[targetRow][mid]:
                start = mid + 1
            else:
                end = mid

        return False