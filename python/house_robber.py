# leetcode problem # 198. House Robber

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

"""
My solution: dynamic programming

Intuition: The problem can be broken into smaller parts
- The robber has 2 choices regarding the last 2 houses
    1. The robber may rob the last house + largest sum of money robbed from all houses besides the last 2 houses
        - if the robber robs the last house, the second last house cannot be robbed
    2. Alternately, the robber may also rob the second last house + largest sum of money robbed from all houses besides 
        the last 3 houses
- One of these two choices above will yield the largest sum of money robbed, but it is inconclusive which is larger at this point
- However, the logic above can be repeated to find the largest sum from all houses besides the last N houses, until the base case
of the largest sum of money robbed from only the first house or only the second house
    -> the largest sum at that point is the house with more money out of the first and second

Implementation:
- Rob every house sequentially
    - Keep track of the largest sum of money robbed from all previous houses except the last processed house
        - to rob the current house, the previous house cannot be robbed
    - After the current house is robbed, update the largest sum
        - robbing the previous house can yield a higher sum
    - When robbing the next house, the sum from robbing the current house becomes the previous sum

Runtime: O(N) where N is the length of input array nums
Space: O(1) memory usage does not scale with input
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        largestSum = 0
        prevSum = 0

        for num in nums:
            curSum = largestSum + num
            largestSum = max(prevSum, largestSum)
            prevSum = curSum

        return max(curSum, largestSum)
