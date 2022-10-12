# leetcode problem # 976. Largest Perimeter Triangle

"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.


Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0

Constraints:

3 <= nums.length <= 10^4
1 <= nums[i] <= 10^6
"""

"""
My solution: Sort then find the largest possible combo

Property of triangle: For any triangle with non-zero area:
- The sidelength of any side < sum of sidelengths of other two sides

After sorting the nums array from largest to smallest, the smallest i where nums[i], nums[i+1], num[i+2] fit the property above will create the triangle with the largest perimeter possible from the given nums array.
- Intuition: if the triangle requirement was removed, and the problem was just choosing 3 numbers that create the largest sum, the largest 3 numbers would be chosen
    - if the largest 3 sides also create a valid triangle, the answer is found for this problem
    - as the array is sorted, the first chosen side must be too long for the triangle if the triangle is invalid
        - ex: if nums = [1000,2,1], 1000 is too large to form a triangle with 2 and 1 (1000 >= 1 + 2 == 3)
        - thus, the first chosen side is eliminated from candidate for a side of the triangle
    - after eliminating the longest side, repeat the logic for the 3 longest sides from the remaining sides (the array remains sorted)
    - if there are fewer than 3 sides available before a solution is found, it is impossible to create a valid triangle from the given sidelengths; return 0

Runtime: O(N*logN) where N is the length of the nums array
- Sorting is the most time-intensive task in this algorithm
Space: O(1), memory usage does not scale with input size.
- This assumes that the sorting logic does not use extra space
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for idx in range(len(nums) - 2):
            if nums[idx] < nums[idx + 1] + nums[idx + 2]:
                return nums[idx] + nums[idx + 1] + nums[idx + 2]
        return 0
