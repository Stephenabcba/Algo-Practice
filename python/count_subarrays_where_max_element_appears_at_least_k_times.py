# leetcode problem # 2962. Count Subarrays Where Max Element Appears at Least K Times

"""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= k <= 10^5
"""


"""
My Solution: Sliding Window

Observation: All other subarrays can be viewed as extensions of all "core" subarrays
containing exactly k values of X, where X is the largest value in nums
    - these "core" subarrays begin and end with X

Logic:
1. Preprocess the array to find the largest value X, then find the indeces of all occurrences of X, 
and save these indeces to an array
2. Process the array with a sliding window
    - if there are Q values to the left of the "core", there are Q + 1 subarrays that meet the requirement
        - this includes the core value itself
    - if there are R values to the right of the "core" until the next occurrence of X, then there are
    (Q + 1) * (R) more subarrays that meets the requirement
3. Count all subarrays to the right of the last window, if they exist
4. Return the final count

Runtime: O(N) where N is the length of nums
Space: O(N)
"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        largest = max(nums)

        allLargest = []
        for idx, num in enumerate(nums):
            if num == largest:
                allLargest.append(idx)

        if len(allLargest) < k:
            return 0

        left = 0
        right = k - 1

        ans = 0

        while right < len(allLargest):
            ans += allLargest[left] + 1
            if right < len(allLargest) - 1:
                ans += (allLargest[left] + 1) * \
                    (allLargest[right + 1] - allLargest[right] - 1)

            left += 1
            right += 1

        if allLargest[-1] < len(nums) - 1:
            ans += (allLargest[left - 1] + 1) * \
                (len(nums) - 1 - allLargest[-1])

        return ans
