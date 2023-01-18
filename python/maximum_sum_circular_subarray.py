# leetcode problem # 918. Maximum Sum Circular Subarray

"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
"""

"""
My Attempt: Failed due to N^2 runtime

Concept:
- Check every possible subarray (skip length N as they would all have the same sum)
    - start at any given index and process every subarray with length from 1 to N-1
- To access the subarray sum in constant time, preprocess the prefix sum of the array.

Runtime: O(N^2) where N is length of nums array
Space: O(N)
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sums = [0]
        curSum = 0
        for num in nums:
            curSum += num
            sums.append(curSum)
        totalSum = sum(nums)
        ans = totalSum
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                cur = -sums[i] + sums[(i + j) % len(nums)]
                if i + j >= len(nums):
                    cur += totalSum
                ans = max(cur, ans)
        return ans


"""
Solution By Leetcode: Calculate the Minimum Subarray

"As mentioned before, we know that the maximum "normal sum" is the Maximum Subarray problem 
which can be found with Kadane's. As such, we can focus on finding the "special sum".

Instead of thinking about the "special sum" as the sum of a prefix and a suffix, we can 
think about it as the sum of all elements, minus a subarray in the middle. In this case, 
we want to minimize this middle subarray's sum, which we can calculate using Kadane's algorithm as well."
https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/2868539/Figures/918/918_Maximum_Sum_Circular_Subarray.png

In summary, the solution modifies Kadane's algorithm such that the minimum sum is also calculated
- if the normal sum from Kadane's algorithm returns a non-negative value, it is the answer
- if the minimum sum equals the sum of every value in nums, all values in the array is non-positive
    -> return the largest number in the array (it could be negatie)
- otherwise, return the sum - the minimum sum, which is essentially removing a subarray from the nums array


Runtime: O(N) where N is length of nums array
Space: O(1), memory usage does not scale with input
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        curMin = 0
        curSum = 0
        maxSum = nums[0]
        minSum = nums[0]

        for num in nums:
            curMax = max(curMax, 0) + num
            maxSum = max(maxSum, curMax)
            curMin = min(curMin, 0) + num
            minSum = min(minSum, curMin)
            curSum += num

        return maxSum if curSum == minSum else max(maxSum, curSum - minSum)
