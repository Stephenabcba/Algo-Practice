# leetcode problem # 974. Subarray Sums Divisible by K

"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
2 <= k <= 10^4
"""

"""
Solutions by leetcode: Optimization from prefix sum (originally written in C++)

The solution begins with utilizing prefix sum and checking every
sum pair (i,j) where i < j.
    - The sum is divisible by k if (prefixSum[j] - prefixSum[i]) % k == 0
However, the solution above has a O(N^2) runtime, which is too long when
the input has up to 10^4 numbers

Optimization:
- (prefixSum[j] - prefixSum[i]) % k == 0 is only true if prefixSum[j] % k == prefixSum[i] % k
- Thus, the prefix sums can be done in one-pass
    - when sequentially processing the numbers, the algorithm only needs to check the number
        of groups that have previously processed to the same remainder

Runtime: O(N) where N is the number of numbers in nums
Space: O(N)
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixMod = 0
        result = 0

        modGroups = {}
        modGroups[0] = 1

        for num in nums:
            prefixMod = (prefixMod + num % k + k) % k
            result += modGroups.get(prefixMod, 0)
            modGroups[prefixMod] = modGroups.get(prefixMod, 0) + 1

        return result
