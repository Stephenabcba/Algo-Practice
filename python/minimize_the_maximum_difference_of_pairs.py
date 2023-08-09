# leetcode problem # 2616. Minimize the Maximum Difference of Pairs

"""
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

Example 1:
Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Example 2:
Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= p <= (nums.length)/2
"""

"""
My solution: sort then binary search

To minimize difference, a number should be paired with values close to it.
-> sort the array so that values close together are grouped.

Perform binary search on the range of 0 to max(nums) - min(nums)
- If there are enough pairs from the guess, the actual minimum is less than or equal to the guess
- Otherwise, the actual minimum is higher than the guess


Runtime: O(N* logM) where N is length of nums and M is the difference between the max and min of nums
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        low = 0
        high = nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            curVal = -1
            pairCount = 0
            for num in nums:
                if curVal < 0:
                    curVal = num
                else:
                    if num - curVal <= mid:
                        pairCount += 1
                        curVal = -1
                    else:
                        curVal = num

            if pairCount >= p:
                high = mid
            else:
                low = mid + 1

        return low