# leetcode problem # 1424. Diagonal Traverse II

"""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.


Example 1:
https://assets.leetcode.com/uploads/2020/04/08/sample_1_1784.png
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:
https://assets.leetcode.com/uploads/2020/04/08/sample_2_1784.png
Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= sum(nums[i].length) <= 10^5
1 <= nums[i][j] <= 10^5
"""

"""
My solution: Keep a list of indexes

Idea:
- Create a list of indexes, starting at row 0 and eventually expand to all rows
    - for every iteration before all rows have been added, add a new row to the list
- Each iteration, take the first available number from each row saved in the list, starting
from the largest row
- If all values in a row are used, remove it from the list

Runtime: O(N) where N is the total size of nums
Space: O(M) where M is the number of rows in nums
"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []

        stack = [[0, 0]]

        maxRow = 0

        while len(stack) > 0:
            for idx in range(len(stack) - 1, -1, -1):
                ans.append(nums[stack[idx][0]][stack[idx][1]])
                stack[idx][1] += 1
                if stack[idx][1] == len(nums[stack[idx][0]]):
                    stack.pop(idx)
            if maxRow < len(nums) - 1:
                maxRow += 1
                stack.append([maxRow, 0])

        return ans
