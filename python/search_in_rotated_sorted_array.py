# leetcode problem # 33. Search in Rotated Sorted Array

"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""

"""
My solution: Binary Search twice

To more easily conduct the binary search on the sorted array, first find where the array
was rotated.
- if the last value in nums is smaller than the first value in nums, the array is rotated.
- binary searched can be used to find the smallest value in the rotated sorted array
    - at the start of binary search, the smallest value seen is the last value in nums
    - if the middle value is larger than the smallest value seen, the start is to the right of middle
    - otherwise, the start is equal to or to the left of middle

After the start of the array is found, the binary search can be conducted, after rotating the values
to check every time
- the start and end are still initiated at 0 and len(nums), respectively
- the middle will be calculated normally
- however, rotate the middle first before checking the values in nums against the target
    - the rotated index is (middle + rotation + len(nums)) % len(nums)

Runtime: O(logN) where N is the length of nums
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotation = 0
        if nums[-1] < nums[0]:
            curMin = nums[-1]
            start = 0
            end = len(nums)
            while start < end:
                middle = (start + end) // 2
                if nums[middle] > curMin:
                    start = middle + 1
                else:
                    end = middle
                    curMin = nums[middle]

            rotation = start

        start = 0
        end = len(nums)

        while start <= end:
            middle = (start + end) // 2
            rotatedIndex = (middle + rotation + len(nums)) % len(nums)
            if start == end:
                if rotatedIndex < len(nums) and target == nums[rotatedIndex]:
                    return rotatedIndex
                else:
                    break
            if target == nums[rotatedIndex]:
                return rotatedIndex
            elif target < nums[rotatedIndex]:
                end = middle
            else:
                start = middle + 1

        return -1