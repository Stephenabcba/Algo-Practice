# leetcode problem # 42. Trapping Rain Water

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

"""
My solution: Preprocessing

Idea: Process the each vertical block of water indivually
- add up the total amount of water trapped for the final amount
- the amount of water trapped in each horizonal unit is decided by 3 factors:
    1. the tallest wall to the left of the unit
    2. the tallest wall to the right of the unit
    3. the vertical height of the unit
    -> the actual amount trapped is the minimum of 1 and 2, subtracted by 3
        - if the vertical height of the unit is taller than either of the side walls,
        there is no water trapped

To find the height of the right wall, preprocess the list from right to left, keeping track
of the tallest wall to the right of each unit

Runtime: O(N) where N is the length of height list
Space: O(N)
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        rightWall = [0] * len(height)
        curHighest = 0
        for idx in range(len(height)-1, -1, -1):
            rightWall[idx] = curHighest
            curHighest = max(curHighest, height[idx])

        totalWater = 0
        leftHeight = 0

        for idx in range(len(height)):
            waterLevel = min(leftHeight, rightWall[idx]) - height[idx]
            if waterLevel > 0:
                totalWater += waterLevel
            leftHeight = max(leftHeight, height[idx])
        return totalWater
