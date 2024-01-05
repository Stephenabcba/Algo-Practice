# leetcode problem # 300. Longest Increasing Subsequence

"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

"""
My solution: Greedy & Binary Search

Logic: keep a list of included values in the LIS
- The list is sorted at all times
- If a new value is larger than all values in the list, then add it to the end
- Otherwise, use the new value to replace a value in the list
    - The replaced value is the smallest value in the list
    - The search process can be done with binary search

At the end, return the length of the list generated above

This solution does fit the followup of running in O(n log(n)) time complexity.
- the algorithm iterates through the entire list, running the inner loop N times
- each iteration, the inner loop either adds a new value to the end, or replaces a value already included
    - this proces takes O(logn) time
-> Combined together, the algorithm takes O(n log(n)) time

Runtime: O(N logN) where N is the length of nums list
Space: O(N)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]

        for num in nums[1:]:
            if num > stack[-1]:
                stack.append(num)
            else:
                low = 0
                high = len(stack)

                while low < high:
                    mid = (low + high) // 2
                    if stack[mid] >= num:
                        high = mid
                    else:
                        low = mid + 1
                if stack[low] > num:
                    stack[low] = num

        return len(stack)
