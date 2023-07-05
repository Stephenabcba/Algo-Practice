# leetcode problem # 1493. Longest Subarray of 1's After Deleting One Element

"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

"""
My solution: Running sum

Idea:
- Since exactly 1 value will be deleted, ideally a 0 is deleted to connect two chains of 1's
    to create the longest chain
- To find the longest chain after deleting one value, keep track of the length of the last chain,
    the length of the current chain, and the length of the longest chain so far
    - check if the current chain + the last chain is longer than the longest chain
        - update if needed
    - when a 0 is encountered, the past chain can no longer be connected to the upcoming chain
        -> the past chain can be removed
    - the current chain can be used as the past chain to connect to the upcoming chain
        -> the current chain becomes the past chain
    - the upcoming chain will be the one being counted
        -> the upcoming chain becomes the current chain

Edge Case: if nums only contains 1's, one 1 must be deleted
    - remove 1 from the max count if the max count matches with length of nums

Runtime: O(N) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pastCount = 0
        maxCount = 0
        curCount = 0

        for num in nums:
            if num == 0:
                pastCount = curCount
                curCount = 0
            else:
                curCount += 1
            if curCount + pastCount > maxCount:
                maxCount = curCount + pastCount


        if maxCount == len(nums):
            maxCount -= 1
        return maxCount