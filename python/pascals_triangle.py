# leetcode problem # 118. Pascal's Triangle

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""

"""
My solution: Nested Loop

Iterate for each row:
- if the value is on the side, it is 1
- otherwise, the value is the sum of pascal[row-1][col-1] + pascal[row-1][col]

At each row N (1-indexed), there are N values in the row.

Runtime: O(N^2) where N is the input integer numRows
Space: O(1), memory usage does not depend on input
    - excludes output memory usage
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(len(ans), numRows):
            ans.append([])
            for col in range(row + 1):
                if col == 0 or col == row:
                    ans[row].append(1)
                else:
                    ans[row].append(ans[row - 1][col - 1] + ans[row - 1][col])

        return ans