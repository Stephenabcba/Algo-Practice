# leetcode problem # 75. Sort Colors

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

"""
My solution: Counting Sort

Idea: Count the number of red, white, and blue objects, then distribute them accordingly
- the first portion of nums will be filled with red objects, the second portion with white objects, and third
portion with blue objects

Runtime: O(N) where N is the length of nums
Space: O(1), memory usage does not depend on input

The solution takes two passes, which does not satify the followup
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colorCounts = [0] * 3

        for num in nums:
            colorCounts[num] += 1

        colorIdx = 0
        for idx in range(len(nums)):
            while colorCounts[colorIdx] < 1:
                colorIdx += 1
            nums[idx] = colorIdx
            colorCounts[colorIdx] -= 1


"""
Solution: Dutch National Flag Problem
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
The pseudo code was converted to python by me

Idea: using 3 flags (i, j, and k), the values can be swapped to sort the colors
- all values from 0 to i (not including i) are red
- all values from i to j (not including j) are white
- all values from k + 1 to the end are blue
- all values from j to k (including j) have yet to be sorted
- if the current object is red, swap it with the object at index i
    - increment i as the red portion has grown
    - increment j to check the next object
- if the current object is white, leave it in place
    - increment j to check the next object
- if the current object is blue, swap it with the object at k
    - decrement k as the blue portion has grown
    - the swapped value needs to be checked again, so j has not changed

Runtime: O(N) where N is the length of nums
Space: O(1), memory usage does not depend on input

This satisfies the followup to complete the sorting in one pass with constant space usage
"""


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1

        while j <= k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
