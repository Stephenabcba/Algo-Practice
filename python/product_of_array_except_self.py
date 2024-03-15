# leetcode problem # 238. Product of Array Except Self

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

"""
My solution: 2 passes prefix and suffix

Observation: The value of any item in the output array is the product of all values before the item multiplied
by all the values after the item
- product of all values before can be found with a prefix product (similar to prefix sum, but multiplying each value)
- product of all values after can be found with a suffix product, iterating backwards
=> In total, the output array can be completed in two full passes

Runtime: O(N) where N is length of nums
Space: O(1), memory usage does not depend on input
    - the memory usage of output is not counted

This solution satisfies the follow up requirement of using O(1) extra space, and does not use the division
operation
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        curProd = 1

        for idx in range(len(nums)):
            ans[idx] *= curProd
            curProd *= nums[idx]

        curProd = 1
        for idx in range(len(nums) - 1, -1, -1):
            ans[idx] *= curProd
            curProd *= nums[idx]

        return ans
