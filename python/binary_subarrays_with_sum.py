# leetcode problem # 930. Binary Subarrays With Sum

"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
1 <= nums.length <= 3 * 10^4
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""

"""
My solution: Keep a queue of zeros

Observation: The number of leading and trailing 0's can lead to more combination of subarrays
- the 0's "sandwiched" between the 1's do not lead to more ways

Idea: keep track of M + 1 clusters of 0's around the current smallest subarray with the goal sum
- M is the goal integer
- all smallest subarrays (except the special case shown below) must begin and end with 1's
    - if goal is 1, the smallest subarray is [1]
    - if goal is 2, the smallest subarray could be [1,0,0,0,0,0,0,0,0,0,0,0,0,1], but it cannot be
    [1,1,0] or [0,1,1]
- there are M - 1 clusters of 0's in between all the 1's in the smallest subarrays
    - there are 2 additional clusters, 1 before and 1 after the smallest subarrays
- in between consecutive 1's, there's a cluster of size zero
- When the algorithm comes across a new 1 when the goal is reached, remove the 1 from the very far
left of the current subarray, and remove the leading cluster of 0's
    - the cluster to the right of the removed 1 now becomes the leading cluster
    - a new cluster is created to the right of the subarray, to keep count of 0's to come
- When the subarray has reached the goal sum, there is at least 1 subarray that can reach the goal
    - +1 to the total number of ways
    - the size of the cluster containing the leading 0's are all other ways the subarray can reach the goal
        - add to the total number of ways

Special case: goal is 0
- To reach the sum goal of 0, a subarray cannot contain any 1's
-> There is no "leading 0's" before a 1, all combinations must be clusters of 0's
    - in the current counting method, the accessed count of 0's is the
    current cluster instead of the previous cluster
        - skip the additional +1 to avoid double counting


Runtime: O(N) where N is the length of nums list
Space: O(M) where M is the integer goal
"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ways = 0
        zeros = deque([0])
        curSum = 0

        for num in nums:
            if num == 0:
                zeros[-1] += 1
            else:
                if curSum < goal:
                    curSum += 1
                zeros.append(0)
                if len(zeros) > goal + 1:
                    zeros.popleft()
            if curSum == goal:
                ways += zeros[0]
                if goal > 0:
                    ways += 1
        return ways
