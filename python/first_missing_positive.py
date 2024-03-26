# leetcode problem # 41. First Missing Positive

"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""

"""
My solution: Using input as memory storage

This solution has very similar concepts to # 442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

Observations:
1. The highest lowest missing positive integer that could be in nums of length N is N + 1
    - ex: N = 3, nums could be [1,2,3] -> the missing number is 3 + 1 = 4
2. Values below 1 and above N cannot contribute to the lowest missing positive integer
    - 0 and negative values are not positive
    - values higher than N means that there are gaps from 1 to N
3. There could be duplicates in nums
    - Duplicates do not make a significant impact to the solution

Intuition:
- Observation 1 shows that values that could raise the lowest missing positive
    integer are constrained to the range [1,N]
- The input array nums has N values, with indeces [0, N-1]
-> The input could be used as memory storage, with a 1:1 mapping for each value

Obstacle: There are values outside the range
- As shown in observation 2, these values do not contribute to the solution
- Solution: Preprocess nums, and change all values outside the range to 1
    * make sure that 1 exists already in nums
        - if 1 didn't exist in nums, return 1 as the smallest missing positive integer

Logic:
1. Iterate and preprocess the array
    - change all values outside the range [1,N] to 1
    - check if 1 already exists in the array
        - if 1 doesn't exist, return 1
2. Iterate and mark values that exist
    - for each value X, make the value at index X-1 negative
    - the preprocessing done in step 1 ensures that X-1 is always a valid index in nums
3. Iterate again and find the first missing integer
    - Find the first index i where the value is positive
    - Return i+1
        - The values are 1-indexed while the actual array is 0-indexed

Runtime: O(N) where N is length of nums
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        containsOne = False

        for idx in range(len(nums)):
            if nums[idx] == 1:
                containsOne = True
            elif nums[idx] < 1 or nums[idx] > len(nums):
                nums[idx] = 1

        if not containsOne:
            return 1

        for num in nums:
            idx = abs(num) - 1
            nums[idx] = - abs(nums[idx])

        ans = 0

        while ans < len(nums) and nums[ans] < 0:
            ans += 1

        return ans + 1
