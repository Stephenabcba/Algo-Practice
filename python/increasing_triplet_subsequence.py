# leetcode problem # 334. Increasing Triplet Subsequence

"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""

"""
My solution: Reduce the values

Intuition: Reduce the values of candidates for subsequence whenever possible.
- By greedily reducing the first value whenever possible allows the second and the third value to be lower
    - ex: if the sequence is [100000,1,2,3]:
        - by reducing num1 from 100000 to 1, [1,2,3] is now an allowed subsequence
        - if num1 remained 100000, [100000,2,3] is invalid
- Even if num1 was reduced, a new value must still be larger than num2 to create a valid subsequence
    - ex: if the sequence is [2,5,1,6], the final valid subsequence found is [1,5,6]
        - however, it is still true that the subsequence [2,5,6] exists in the array and is the answer
    - ex2: if the sequence is [2,5,1,4], no valid subsequence would be found
        - 4 < 5, so the subsequence [1,5,4] would not be recognized.

Logic:
- Iterate over each value in the array from start to finish
    - If a value is smaller than the first number, change the first number to the value
    - If the value is larger than the first number but smaller than the second number, change the second number to the value
    - If the value is larger than the second number, there must exist a valid subsequence that fits criteria, return True.
- After iteration, if no valid subsequence is found, return False

* This is approach is unable to provide the correct subsequence when returning True
    - the first value could've been changed before the third value is found

Runtime: O(N) where N is the number of numbers in nums array
Space: O(1), data usage does not depend on input size
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = float('inf')
        num2 = float('inf')

        for num in nums:
            if num <= num1:
                num1 = num
            elif num <= num2:
                num2 = num
            else:
                return True

        return False
