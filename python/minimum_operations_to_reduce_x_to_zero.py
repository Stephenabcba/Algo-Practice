# leetcode problem # 1658. Minimum Operations to Reduce X to Zero

"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.


Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""

"""
My solution: Binary search the ending value

Idea: Iterate through the nums list, using each index as the starting index of values to keep
- all values before the starting index are removed, decreasing x.
- binary search for the ending index for the values to keep
    - all values after the ending index are removed, decreasing x
    - there is at most 1 ending index for each starting index

Prefix sum can be used to quickly find the sum of the values removed

Runtime: O(N * logN) where N is the length of nums
Space: O(N)
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [0]
        n = len(nums)
        
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        if x == prefix[-1]:
            return n

        ans = float('inf')

        for idx in range(n + 1):
            low = idx + 1
            high = n
            while low <= high:
                mid = (low + high) // 2
                outcome = prefix[idx] + prefix[-1] - prefix[mid]
                if outcome == x:
                    operations = idx + n - mid
                    if operations < ans:
                        ans = operations
                    break
                elif outcome < x:
                    high = mid - 1
                else:
                    low = mid + 1

            
        return ans if ans != float('inf') else -1
    

"""
Solution by leetcode user vanAmsen: Sliding Window
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/solutions/4066422/96-51-sliding-window/

Original problem: find the smallest number of values to remove to make x become 0
Reframed problem: find the longest subarry in nums that reaches target
    - target = sum(nums) - x
    - the answer to the original problem is len(nums) - longest subarray length

Create a sliding window to capture the subarray
- if the sum within the sliding window is too small, expand the sliding window to the right
- if the sum within the sliding window is too large, shorten the sliding window from the left
- if the sum equals the target, check if the current subarray length is the longest
    - keep track of the longest subarray length with sum equals target


Runtime: O(N)
Space: O(1)
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n = sum(nums) - x, len(nums)
        
        if target == 0:
            return n
        
        max_len = cur_sum = left = 0
        
        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len else -1