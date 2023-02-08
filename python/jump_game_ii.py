# leetcode problem # 45. Jump Game II

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""

"""
My solution: keep track of the shortest steps required to reach each value in the list

Intuition:
Take a jump to every reachable value from the current value.
If the jump takes fewer than the previous attempts to get to the value, update it.

Optimization:
Check the jump values backwards, if the number of steps previously used
to get to the value is equal to lower, skip the rest of the jumps in this
iteration.
- due to problem constraints, it always takes equal or fewer steps to reach
any values to the left of the current value

Runtime: O(N) where N is the number of values in the nums list
Space: O(N)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        stepsRequired = [100000 for _ in nums]
        stepsRequired[0] = 0

        for idx, num in enumerate(nums):
            for stride in range(min(idx + num, len(nums) - 1), idx, -1):
                if stepsRequired[idx] + 1 < stepsRequired[stride]:
                    stepsRequired[stride] = stepsRequired[idx] + 1
                else:
                    break

        return stepsRequired[-1]
