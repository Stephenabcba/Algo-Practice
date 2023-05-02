# leetcode problem # 1822. Sign of the Product of an Array

"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).


Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

Constraints:
1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""

"""
My solution: Find the product then find the sign

Follow the instructions to find the sign

Possible Improvements:
As the magnitude of the product doesn't matter (the answer has magnitudes of only 0 and 1)
it is not necessary to save a large integer of the value
Instead, the problem can just track the negative numbers (as it flips the product from positive
to negative and vice versa) and 0 (the product must be 0 if one of the values is 0)

Runtime: O(N) where N is the length of list nums
Space: O(1) memory usage does not depend on input
"""


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num

        if product > 0:
            return 1
        elif product < 0:
            return -1
        return 0
