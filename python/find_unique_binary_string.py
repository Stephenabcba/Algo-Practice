# leetcode problem # 1980. Find Unique Binary String

"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""

"""
My solution: Make N+1 guesses

The number of possible numbers given the length N is 2^N
However, the nums list only contains N values
=> making N+1 guesses guarantees that at least one of the guesses is not in nums

Runtime: O(N^2) where N is the length of nums list
Space: O(N), the guesses take up strings of size N
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for i in range(len(nums) + 1):
            binNum = bin(i)[2:].zfill(len(nums))
            if binNum not in nums:
                return binNum
