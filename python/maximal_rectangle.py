# leetcode problem # 85. Maximal Rectangle

"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

"""
My solution: Check each rectangle

For each space in the matrix, find all rectangles that end with that space as the bottom
right corner, and find the rectangle with the largest area

Runtime: O(M^2 * N) where M is the number of rows and N is the number of columns
Space: O(M * N)
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        horizontalLengths = [[0 for _ in matrix[0]] for __ in matrix]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    if col == 0:
                        horizontalLengths[row][col] = 1
                    else:
                        horizontalLengths[row][col] = horizontalLengths[row][col - 1] + 1

        maxArea = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                width = horizontalLengths[row][col]
                for rowLen in range(1, row + 2):
                    width = min(
                        width, horizontalLengths[row - rowLen + 1][col])
                    maxArea = max(maxArea, rowLen * width)
        return maxArea


"""
Solution by Mohammed_Raziullah_Ansari: Stack-Based
1. Initialization:
- Initialize a stack stack to keep track of indices of bars in the histogram.
- Initialize max_area to store the maximum rectangle area found.
2. Iterate Through Each Bar:
- Traverse each bar's height in the height array from left to right.
3. Stack Operations:
- For each bar at index i:
    - While the stack is not empty and the current bar's height (height[i]) is less than the height of the bar represented by the index on top of the stack (height[stack[-1]]):
        - Pop the top index j from the stack.
        - Calculate the area with the popped bar's height:
            - h = height[j]
            - w = i - stack[-1] - 1 (if stack is not empty), otherwise w = i
            - area = h * w
        - Update max_area with the maximum of max_area and area.
4. Final Maximum Area:
- After processing all bars in the height array:
    - Check if the stack is not empty:
        - Pop each remaining index j from the stack and calculate the area similarly to step 3.
5. Return Result:
    - max_area will hold the value of the largest rectangle that can be formed within the histogram.
Runtime: O(M*N)
Space: O(M + N)
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        # Include an extra element for easier calculation
        heights = [0] * (cols + 1)
        max_area = 0

        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            # Calculate max area using histogram method
            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
