# leetcode problem # 1877. Minimize Maximum Pair Sum in Array

"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

Example 1:
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

Example 2:
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

Constraints:
n == nums.length
2 <= n <= 10^5
n is even.
1 <= nums[i] <= 10^5
"""

"""
My solution: sort then pair

To minimize pair sums, pair the largest number with the smallest number, the second largest number with the second smallest number, and so on.
To find the maximum and minimum quickly each iteration, sort the numbers list first before processing

The answer is the largest sum of the pairs arranged in the logic above

Runtime: O(N * logN) where N = length of nums list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maxSum = 0

        for idx in range(len(nums)//2):
            pairSum = nums[idx] + nums[-(idx + 1)]
            if pairSum > maxSum:
                maxSum = pairSum

        return maxSum
