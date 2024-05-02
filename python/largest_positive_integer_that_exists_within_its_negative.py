# leetcode problem # 2441. Largest Positive Integer That Exists With Its Negative

"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Example 1:
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Example 2:
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Example 3:
Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
nums[i] != 0
"""

"""
My solution: Set

Logic:
- Keep a set of all seen numbers
- Initialize the largest k to -1
- While iterating:
    - Check if the opposite counterpart of a number is in the set
        - if it is, and the value of the number is higher than the saved k value,
            update k with the current number
    - Store the number seen in a set
- Return the value k

Runtime: O(N) where N is the length of nums
Space: O(N)
"""


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numSet = set()

        largest = -1

        for num in nums:
            if -num in numSet and abs(num) > largest:
                largest = abs(num)

            numSet.add(num)

        return largest
