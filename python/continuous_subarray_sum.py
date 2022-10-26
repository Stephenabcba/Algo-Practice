# leetcode problem # 523. Continuous Subarray Sum

"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
"""

"""
My attempt: failed due to exceeding time limit

Logic: 
1. preprocessing the sum from the start to the current value
- This way, it takes constant time to find the sum from any given continuous range.
2. Check every possible continuous subarray combinations to see if any sum is a multiple of k.

Runtime: O(N^2) where N is the length of the nums array
Space: O(N) where N is the length of the nums array
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = [0]
        curSum = 0
        for num in nums:
            curSum += num
            sums.append(curSum)

        for numElements in range(2, len(nums) + 1):
            for startIdx in range(len(nums) - numElements + 1):
                if (sums[startIdx + numElements] - sums[startIdx]) % k == 0:
                    return True

        return False


"""
Solution in leetcode solutions: hash map

Instead of checking that (pref[r + 1] - pref[l]) % k == 0, check that pref[l] % k == pref[r + 1] % k
- the equations are mathematically equivalent
- make sure that l < r so that the sum contains at least 2 terms.

Instead of storing the prefix sum in a linear array, a hash map (dictionary) is used instead
- The keys are s % k, and the values are the current index + 1
    - this ensures that the subarray size is at least 2
- If a future subarray sum has the same s % k and the subarray size is at least 2, return True
- If none of the sums returned true, return False

Runtime: O(N) where N is the length of the nums array
Space: O(min(N, K)) where N is the length of the nums array, and K is the input value k
- As the keys are modulo'd before saving, there is at most K values in the dictionary if N > K
- if N < K, there would be at most N values in the dictionary.
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: 0}

        s = 0

        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True

        return False
