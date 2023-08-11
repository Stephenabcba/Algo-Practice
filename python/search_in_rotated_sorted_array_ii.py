# leetcode problem # 81. Search in Rotated Sorted Array II

"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""

"""
My solution: Clean up then binary search

Logic:
1. Remove duplicates
2. Binary search for the rotation pivot
3. Binary search for target

Upon further inspection, this solution is worse than linear search.

Runtime: O(N)
Space: O(N)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        prev = None
        cleanedNums = []
        for num in nums:
            if num != prev:
                cleanedNums.append(num)
            prev = num
        if cleanedNums[-1] == cleanedNums[0] and len(cleanedNums) > 1:
            cleanedNums.pop()

        rotation = 0


        if cleanedNums[-1] < cleanedNums[0]:
            low = 0
            high = len(cleanedNums)
            lowest = cleanedNums[-1]
            while low < high:
                mid = (low + high) // 2
                if cleanedNums[mid] <= lowest:
                    high = mid
                else:
                    low = mid + 1
            rotation = low

        low = 0
        high = len(cleanedNums)

        while low < high:
            mid = (low + high) // 2
            rotatedMid = (mid + rotation) % len(cleanedNums)
            if cleanedNums[rotatedMid] == target:
                return True
            elif cleanedNums[rotatedMid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if cleanedNums[(low + rotation) % len(cleanedNums)] == target:
            return True
        return False