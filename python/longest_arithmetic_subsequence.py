# leetcode problem # 1027. Longest Arithmetic Subsequence

"""
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Example 1:
Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].

Constraints:
2 <= nums.length <= 1000
0 <= nums[i] <= 500
"""

"""
Leetcode's solution: Dynamic Programming

Idea:
- Improve from the brute force method of finding the initial pairs and attempting to
expand the arithmetic sequence for the rest the the array
    - The brute force method takes O(N^2) for every pair and O(N) for each sequence, leading to
    O(N^3) total runtime
- Instead, save the previously found sequences, and try to expand the sequence when new pairs are encountered
    - the information is saved in a DP dictionary
        - the key is the right most number in the sequence and the common difference
        - the value is the length of the sequence
    - at the end, find the longest saved sequence length

Runtime: O(N^2)
Space: O(N^2)
"""

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for right in range(len(nums)):
            for left in range(0, right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1   
        
        return max(dp.values())