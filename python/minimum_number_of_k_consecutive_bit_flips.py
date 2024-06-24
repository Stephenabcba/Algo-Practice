# leetcode problem # 995. Minimum Number of K Consecutive Bit Flips

"""
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:
Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

Constraints:
1 <= nums.length <= 10^5
1 <= k <= nums.length
"""

"""
My solution: use a queue to track the flips

Idea: Greedily try to flip all 0-bits from left to right
- The bits take into account the previous flips done
    - if the value in nums is 0, but 3 flips have been done within the past k values, the current value
    does not need to be flipped again
- to keep track of the flips previously done, a queue is used
    - when all k values have been flipped, remove the value from queue
    - the queue holds the index at which the values should be removed

Runtime: O(N) where N is the length of nums
Space: O(k) where k is the input integer k
"""


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        flips = 0
        q = deque()
        for idx in range(N - k + 1):
            while len(q) > 0 and idx >= q[0]:
                q.popleft()
            if (nums[idx] + len(q)) % 2 == 0:
                flips += 1
                q.append(idx + k)

        for idx in range(N - k, N):
            while len(q) > 0 and idx >= q[0]:
                q.popleft()
            if (nums[idx] + len(q)) % 2 == 0:
                return -1
        return flips


"""
Solution By leetcode: Constant Space with sliding window

A variable holds the number of flips within the sliding window
- the variable is incremented when a flip is needed
    - the value at the index is also changed to 2 to mark a flip
- the variable is decremented when i-k == 2
    - at index i, the flips starting at i-k have been all completed

If a flip is needed and i + k exceeds len(nums), the flip cannot be done; return -1

Runtime: O(N)
Space: O(1)
"""


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        current_flips = 0  # Tracks the current number of flips
        total_flips = 0  # Tracks the total number of flips

        for i in range(len(nums)):
            # If the window slides out of the range and the leftmost element is
            #  marked as flipped (2), decrement current_flips
            if i >= k and nums[i - k] == 2:
                current_flips -= 1

            # Check if the current bit needs to be flipped
            if (current_flips % 2) == nums[i]:
                # If flipping would exceed array bounds, return -1
                if i + k > len(nums):
                    return -1
                # Mark the current bit as flipped
                nums[i] = 2
                current_flips += 1
                total_flips += 1

        return total_flips
