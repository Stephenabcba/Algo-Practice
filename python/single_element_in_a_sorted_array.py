# leetcode problem # 540. Single Element in a Sorted Array

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""

"""
My solution:Binary search

Observation:
In a sorted list where every element appears exactly twice, every even (2n) indexed value should be
the same as the odd (2n+1) value after it.

When performing binary search, check whether the values before the middle follow the observation.
- if the values do follow the observation, the one element that appears exactly once occurs after 
the middle.
- otherwise, the one element that appears exactly once occurs before the middle.

Runtime: O(logN) where N is the number of values in nums list
Space: O(1), memory usage doesn't depend on input
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while high > low:
            mid = (high + low) // 2

            if mid % 2 == 0:
                if mid == len(nums) - 1:
                    return nums[mid]
                if nums[mid] == nums[mid + 1]:
                    low = mid + 2
                else:
                    high = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 2

        return nums[low]
