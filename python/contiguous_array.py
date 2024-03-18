# leetcode problem # 525. Contiguous Array

"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""

"""
My solution: Prefix sum with dictionary

Intuition: In a subarray with an equal number of 0 and 1, the number of 0s equal the number of 1s
- These subarrays can be identified with prefix sums
    - When calculating the prefix sum, each 0 is valued as -1, and each 1 is valued as 1
    - The subarrays can be found when the prefix sum of one index matches with the prefix sum of another index
    - If the prefix sum is 0 at any point, the start of the array to that index is also a subarray with equal number of 0s and 1s
- To find the length of the longest subarray, use a dictionary to keep track of the first occurrence of each prefix sum
    - the longest is the one with the highest difference between the first and last occurrence indeces of the same prefix sum

Runtime: O(N) where N is the length of nums list
Space: O(N)
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        firstOccur = {}
        firstOccur[0] = -1
        curSum = 0
        longest = 0
        for idx, num in enumerate(nums):
            if num:
                curSum += 1
            else:
                curSum -= 1
            if curSum in firstOccur:
                if idx - firstOccur[curSum] > longest:
                    longest = idx - firstOccur[curSum]
            else:
                firstOccur[curSum] = idx
        return longest
