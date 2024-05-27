# leetcode problem # 1608. Special Array With X Elements Greater Than or Equal X

"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.


Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

"""
My solution: Sort then binary search

After sorting, it is easy to determine the number of values larger than any value at any index
Thus, it is possible to use binary search to find the exact value of x

** the only configuration of nums such that it is not special is when nums only contains 0

Runtime: O(N * logN) where N is the length of nums list
Space: O(N)
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        N = len(nums)
        low = 0
        high = N

        while low < high:
            mid = (low + high) // 2

            x = N - mid
            if mid > 0:
                if nums[mid] >= x:
                    if nums[mid - 1] < x:
                        return x
                    else:
                        high = mid
                else:
                    low = mid + 1

            else:
                if nums[mid] >= x:
                    return x
                else:
                    return -1

        return -1


"""
Solution from Editorial: Counting Sort + Prefix Sum

Optimization: The definition of x only requires the number of values greater than or equal to x
- x is limited to N, where N is the length of nums
-> a full sort is not needed
    - Instead, the algorithm can find the number of values greater than or equal to any value from 0 to N in
    linear time

To find x, simply calculate the prefix sum until the index matches with the prefix sum

Runtime: O(N)
Space: O(N)
"""


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        N = len(nums)

        freq = [0] * (N + 1)
        for num in nums:
            freq[min(N, num)] += 1

        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            if i == num_greater_than_or_equal:
                return i

        return -1
