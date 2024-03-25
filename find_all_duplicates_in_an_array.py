# leetcode problem # 442. Find All Duplicates in an Array

"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []


Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""

"""
Solution by CS_MONKES on leetcode: Use the input array as signs to mark

Idea: Make use of the constraint that the values in nums are limited from 1 to N
- for every value X, change the value at index X-1 to negative
    - if the value at index X-1 is already negative, X was seen before
        -> add X to the output array
    - since N is defined as the length of the array, X-1 would never be out of bounds
    * as the sign is used as a marker, get the amplitude X by taking the absolute value


Runtime: O(N) where N is length of nums array
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            checkIdx = abs(num) - 1

            if nums[checkIdx] < 0:
                ans.append(abs(num))
            else:
                nums[checkIdx] = - nums[checkIdx]

        return ans
