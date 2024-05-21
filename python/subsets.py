# leetcode problem # 78. Subsets

"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

"""
My solution: Build new subsets using previous subsets

When adding a new number, all previous subsets create a new subset with the new
number included

Runtime: O(2^N) Where N is the length of nums
Space: O(2^N)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            prevSize = len(results)
            for idx in range(prevSize):
                new = results[idx][:]
                new.append(num)
                results.append(new)

        return results
