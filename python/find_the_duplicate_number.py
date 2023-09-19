# leetcode problem #287. Find the Duplicate Number

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

"""
My solution: Binary Search

Idea: Make a guess at what the duplicate number is, then check
- checking process:
    - go through nums and count the number of values that are smaller than or equal to the guess
    - if there are more values smaller than or equal to the guess, the duplicate value must be smaller than
        or equal to the guess
    - otherwise, the duplicate value must be greater than the guess
- using binary search, exactly half of the range is eliminated each guess, which minimizes the number of guesses
    on average
- it may take O(logN) guesses to get to the solution
- it takes O(N) time to check each time


Followup 1: There are exactly N integers in the range 1 to N. If there are N + 1 integers with the
range from 1 to N, there must be a duplicate number

Followup 2: The binary search solution takes O(N * logN) time, which does not satisfy the linear runtime complexity
- some concepts for linear solution is listed at the bottom

Runtime: O(N * logN) where N is the range of nums (or len(nums) - 1)
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            lowerCount = 0
            for num in nums:
                if num <= mid:
                    lowerCount += 1
            if lowerCount > mid:
                high = mid
            else:
                low = mid + 1

        return low

"""
Other solutions that takes linear time (from leetcode solutions)
1. Sum of Set Bits
    - initialize the answer to 0 (00000000... in binary)
    - for every binary bit where the sum at the bit for the array is greater than the sum at the bit for [1,n] (inclusive), set the answer at the bit to 1
    - after the operations, the decimal representation of answer is the duplicated value
2. Cycle detection
    - treat the nums array as an SLL
        - each index is a "node"
        - the value at the given index is the "next" of the "node"
        - ex: nums[9] = 5 -> the node at 9 has next of 5, the node at 5 has next of nums[5]
    - use the SLL cycle dectection to find the cycle 
        - runner (hare) will move 2 "nodes" every iteration
        - walker (tortoise) will move 1 "node" every iteration
        - where runner and walker meets denotes a cycle
        - after runner and walker meets, reset walker to the start, and runner moves 1 "node" at a time now
        - where runner and walker meets again is the entrance to the cycle, which is also the duplicated value
"""