# leetcode problem # 2348. Number of Zero-Filled Subarrays

"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

"""
My solution: Count and math

Observation:
- In a zero-filled array of length n, there are 1 subarray of length n, 2 subarrays of length n - 1
..., n - 1 subarrays of length 2, n subarrays of length 1
- ex: [0,0,0,0,0] , length = 5
    - there is 1 subarray of length 5, [0,0,0,0,0]
    - there are 2 subarrays of length 4, [0,0,0,0,x] and [x,0,0,0,0]
    - there are 3 subarrays of length 3, [0,0,0,x,x], [x,0,0,0,x], and [x,x,0,0,0]
    - there are 4 subarrys of length 2, [0,0,x,x,x], [x,0,0,x,x], [x,x,0,0,x], and [x,x,x,0,0]
    - there are 5 subarrays of length 1, [1,x,x,x,x], [x,1,x,x,x], [x,x,1,x,x], [x,x,x,1,x], and [x,x,x,x,1]
- Using the formula for finding the sum of all integers from 1 to n, there are a total of n * (n+1) / 2 subarrays

Intuition:
- Find all the continuous zero-filled subarrays at their maximum lengths, and then calculate the number of subarrays
contained in those subarrys
- ex: nums = [0,0,0,0,1,0,0] has two main zero-filled subarrays: [0,0,0,0] and [0,0]
    - there are 4 * 5 / 2 = 10 subarrys in [0,0,0,0]
    - there are 2 * 3 / 2 = 3 subarras in [0,0]
    -> there are 13 total zero-filled subarrays in nums

Runtime: O(N) where N is the number of values in nums list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0

        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                if zeroCount > 0:
                    ans += zeroCount * (zeroCount + 1) // 2
                zeroCount = 0
        if zeroCount > 0:
            ans += zeroCount * (zeroCount + 1) // 2

        return ans
