# leetcode problem # 2366. Minimum Replacements to Sort the Array

"""
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.

For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.


Example 1:
Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0. 

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

"""
My solution: work backwards

Observations:
1. Whether a value needs to be replaced depends on the values tha come after
- if all values that come after are larger, the current value does not need to be replaced
    - also need to factor in the values that have to be split up afterwards
2. To maximize the minimum value after splitting, the original value should be split evenly
- the value could be split evenly into 2, 3, or more values, with a maximum difference of 1 between the largest and
    smallest value after split

Logic: Start from the back and work towards the front
1. Set the maximum threshold to the last value in nums
2. Iterate through each value in nums from back to front
    - if the value is smaller than or equal to the maximum threshold:
        -> set the maximum threshold to the current value
    - if the value is larger than the maximum threshold:
        - split the value evenly into X values
        - X is determined by ceil(value / maximum threshold)
        - it takes X-1 replacements to split 1 value into X values
        - the maximum threshold becomes floor(value/X)
            - this value is the smallest of all values created during the split
    - keep count of the number of replacements done
3. Return the number of replacements at the end

Runtime: O(N) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        maxNum = nums[-1]
        nums.pop()
        ans = 0

        while len(nums) > 0:
            if nums[-1] <= maxNum:
                maxNum = nums[-1]
            else:
                multi = ceil(nums[-1] / maxNum)
                maxNum = nums[-1] // multi
                ans += multi - 1
            nums.pop()

        return ans