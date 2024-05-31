# leetcode problem # 260. Single Number III

"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""

"""
Solution Idea by hi-malik in leetcode solutions
https://leetcode.com/problems/single-number-iii/solutions/5233206/demon-level-explanation-3-approaches/

Note: a and b are the two numbers that only occur once

Step 1: XOR all values together (the result is saved as "xor")
- identifies a ^ b (XOR)
- since all other values occur twice and x ^ x = 0, XORing all values will yield a ^ b
Step 2: Find the bits that differentiate a and b
- In the XOR result from step 1, every 0-bit denotes that the bit in a and b are identical
- Every 1-bit denotes that the bit in a and b are different
-> The 1-bits can be used to differentiate a and b
- The rightmost difference in bits can be found with xor & (-xor) (bitwise AND operator)
    - the result is saved as "diffBit"
Step 3: Separate the numbers into two groups
- the groups are identified with x & diffBit (bitwise AND)
    - if the result is 0, add it to group 1
    - if the result is 1, add it to group 2
    - xor the value with the current value of the group
        - as identical values are placed in the same group, duplicate values cancel each other when
        XOR'd
-> a and b are identified as all other values cancel each other
Step 4: Return a and b


Runtime: O(N) where N is the length of nums
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = [0, 0]

        xor = 0
        for num in nums:
            xor ^= num

        diffBit = xor & (-xor)

        for num in nums:
            if diffBit & num == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num

        return ans
