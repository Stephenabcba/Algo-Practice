# leetcode problem # 896. Monotonic Array

"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false

Constraints:
1 <= nums.length <= 10^5
-105 <= nums[i] <= 10^5
"""

"""
My solution: two flags

Idea: Create two flags that will be turned off
- both flags are initialized to True
- the first flag is for the array increasing
    - if any value in the array is decreasing from the previous value, set this flag to False
- the second flag is for the array decreasing
    - fi any value in the array is increasing from the previous value, set this flag to False
- If either flag is True at the end, the array is monotonic
- If both flags are False at the end, the array is not monotonic
- The iteration can stop early if both flags are already False

Runtime: O(N) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = True

        for idx in range(len(nums)):
            if idx > 0:
                if nums[idx] > nums[idx - 1]:
                    isDecreasing = False
                elif nums[idx] < nums[idx - 1]:
                    isIncreasing = False
            if not isDecreasing and not isIncreasing:
                break

        return isDecreasing or isIncreasing