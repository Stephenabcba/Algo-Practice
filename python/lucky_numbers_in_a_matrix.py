# leetcode problem # 1380. Lucky Numbers in a Matrix

"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""

"""
My solution: Check Each row

Idea: Find the smallest value of each row, then check if the value is the largest in its column

Runtime: O(M*N) where M and N are the number of rows and columns of the matrix, respectively
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        luckyNumbers = []
        m = len(matrix)
        n = len(matrix[0])

        for idx, row in enumerate(matrix):
            smallestRowIdx = 0
            for jdx, col in enumerate(row):
                if col < row[smallestRowIdx]:
                    smallestRowIdx = jdx
            largestColIdx = 0
            for kdx in range(m):
                if matrix[kdx][smallestRowIdx] > matrix[largestColIdx][smallestRowIdx]:
                    largestColIdx = kdx
            if largestColIdx == idx:
                luckyNumbers.append(matrix[largestColIdx][smallestRowIdx])

        return luckyNumbers
