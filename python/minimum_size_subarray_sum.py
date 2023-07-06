# leetcode problem # 209. Minimum Size Subarray Sum

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

"""
My solution: Binary Search with prefix sum

Idea: Make a guess for what the minimum length is, and check it
- to make finding the sum of any subarray in O(1) time, a prefix sum array is created
    - the sum of any subarray is prefix[end] - prefix[start]
- to check if the guessed length could form the target sum, check all subarrays with the guessed length
    - if the guessed length could reach the target sum, the minimum length is at most the guessed length
    - otherwise, the minimum length is at least the guessed length + 1

Runtime: O(N * logN) where N is the length of nums list
Space: O(N)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum = [0]
        curSum = 0

        for num in nums:
            curSum += num
            prefixSum.append(curSum)

        if curSum < target:
            return 0

        start = 1
        end = len(nums)

        while start < end:
            mid = (start + end) // 2
            hasTarget = False
            for idx in range(0, len(nums) - mid + 1):
                if prefixSum[idx + mid] - prefixSum[idx] >= target:
                    hasTarget = True
                    break
            
            if hasTarget:
                end = mid
            else:
                start = mid + 1

        return start


"""
Solution by leetcode: sliding window

Idea:
- as all the values are positive, the sum would not go down when adding more values to a subarray
- include values from the right into the sliding window
- when the sum in the sliding window exceeds target, try to remove values from the left side of the sliding
    window to reduce the size of the sliding window
- keep track of the minimum length and return at the end
    - if the entire array never reached the target sum, return 0

Runtime: O(N)
Space: O(1)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0
