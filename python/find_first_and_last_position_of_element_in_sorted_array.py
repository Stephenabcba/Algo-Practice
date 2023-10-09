# leetcode problem # 34. Find First and Last Position of Element in Sorted Array

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""

"""
My solution: 2 Binary Searches

Since nums is sorted, a target value can be found in logrithmic time.
Using 2 binary searches, the start and end range of the target can be found.

LOGIC:
Binary Search 1: Check for target existing in nums and looking for start
- Starting range is 0 to len(nums)
- If the binary search guess is lower than target, increase the lower bound to guess + 1
- Otherwise, decrease upper bound to guess
* The guess is the floored value of the mid range

Check: If the first binary search didn't find target, target is not in nums; return [-1,-1]

Binary Seach 2: Look for end range of target
- Starting range is result of first search to len(nums) - 1
- If the binary search guess is higher than target, decrease the upper bound to guess - 1
- Otherwise, increase lower bound to guess
* The guess is the ceiling value of the mid range

Runtime: O(logN) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        ans = [start]
        end = len(nums) - 1

        while start < end:
            mid = (start + end + 1) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid

        ans.append(end)

        return ans