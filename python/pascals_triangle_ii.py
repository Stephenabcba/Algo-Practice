# leetcode problem # 119. Pascal's Triangle II

"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33
"""

"""
My solution: Work row by row

Follow the definition of pascal's triangle to find the correct answer.
For the j-th index of the i-th row (0 < j < len(row) - 1), the value is the sum of j-1 and j of the i-1 row

A copied is made of the previous row every iteration to have the correct values added.

Runtime: O(N^2) where N is the integer rowIndex
Space: O(N)
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for row in range(rowIndex):
            prev = ans[:]
            for col in range(1,row + 1):
                ans[col] += prev[col - 1]
            ans.append(1) 

        return ans
    
"""
Slight space improvement without making a copy every row

by working backwards within each row, the previous row do not need to be copied.

Space: O(1)
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for row in range(rowIndex):
            for col in range(row, 0, -1):
                ans[col] += ans[col - 1]
            ans.append(1) 

        return ans