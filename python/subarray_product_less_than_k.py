# leetcode problem # 713. Subarray Product Less Than K

"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""

"""
My solution: Sliding Window

The solution can quickly find all subarrays with products strictly less than k using a sliding window

Logic:
1. In every iteration, expand the sliding window to the right by 1 index
    - shrink the sliding window from the left side until the product of the sliding window is strictly less
    thank k, or when the sliding window has a size of 1
    - if the product of the sliding window is strictly less than k in this iteration, all subarrays
    that end with the newly added value fit the problem requirement
        - for a subarray of length x, there are x subarrays that fits this criteria
2. Return the total count at the end

Runtime: O(N) where N is length of nums
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0

        curProd = nums[0]

        if curProd < k:
            ans += 1

        left = 0
        right = 0

        while right < len(nums) - 1:
            right += 1
            curProd *= nums[right]
            while left < right and curProd >= k:
                left += 1
                curProd //= nums[left - 1]
            if curProd < k:
                ans += right - left + 1

        return ans


"""
Alternative Solution by Leetcode: binary search

The products of all values may be a large number, so the prefix sum array is
saved as sum of log of the values instead

The prefix sum array can be used to binary search for the largest subarray with product
less than K that begins with each value.

Runtime: O(N*logN)
Space: O(N)
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        logK = math.log(k)

        # Calculate prefix sum of logarithms of elements
        logs_prefix_sum = [0]
        for num in nums:
            logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))

        total_count = 0
        # Calculate subarray count with product less than k
        for i, log_num in enumerate(logs_prefix_sum):
            j = bisect.bisect(logs_prefix_sum, log_num + logK - 1e-9, i+1)
            total_count += j - i - 1
        return total_count
