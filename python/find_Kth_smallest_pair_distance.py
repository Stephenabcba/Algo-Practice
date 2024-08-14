# leetcode problem # 719. Find K-th Smallest Pair Distance

"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5

Constraints:
n == nums.length
2 <= n <= 10^4
0 <= nums[i] <= 10^6
1 <= k <= n * (n - 1) / 2
"""

"""
Solution By leetcode: Binary Search + Sliding Window

Idea: Make a guess with binary search, then confirm with sliding window
- This requires a sorted array
- The sliding window counts the pairs in linear time, making the solution time-efficient

* although the problem limits i < j, this limit is not broken when nums is sorted
    - the limit mostly dictates that i and j are distinct, and not counted twice

Runtime: O(N * logM + N * logN) where N is the number of elements and M is the maximum possible distance
Space: O(N)
    - the space usage depends on the sorting algorithm used, and Python's default sorting algorithm takes O(N) space
"""


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        array_size = len(nums)

        # Initialize binary search range
        low = 0
        high = nums[array_size - 1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            # Count pairs with distance <= mid
            count = self._count_pairs_with_max_distance(nums, mid)

            # Adjust binary search bounds based on count
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    # Count number of pairs with distance <= max_distance using a moving window
    def _count_pairs_with_max_distance(
        self, nums: List[int], max_distance: int
    ) -> int:
        count = 0
        array_size = len(nums)
        left = 0

        for right in range(array_size):
            # Adjust the left pointer to maintain the window with distances <=
            # max_distance
            while nums[right] - nums[left] > max_distance:
                left += 1
            # Add the number of valid pairs ending at the current right index
            count += right - left
        return count
