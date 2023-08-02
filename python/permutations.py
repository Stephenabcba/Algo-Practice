# leetcode problem # 46. Permutations

"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

"""
My solution: Recursion

If the length of nums is fixed, the solution is writing a nested loop with N layers, where N
is the length of nums

As the length of nums is fixed, the nested loops have to be implemented another way
-> Recursion can simulate nested loops with variable length
    - recurse until the base case (a full permutation) is reached

To build a permutation, choose 1 value from the remaining numbers to put in the current place.
Repeat until the permutation has all the values in nums

Implementation details: to find what values are already included in the permutation more quickly,
a set is also to keep track of the current values

Runtime: O(N * N!), where N is the length of nums list
- there are N! permutations, and takes O(N) time to copy the current permutation to results
Space: O(N)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        skipVal = set()

        def buildPermutation(curPermutation):
            for num in nums:
                if num not in skipVal:
                    skipVal.add(num)
                    curPermutation.append(num)
                    if len(curPermutation) == len(nums):
                        ans.append(curPermutation[:])
                    else:
                        buildPermutation(curPermutation)
                    skipVal.remove(num)
                    curPermutation.pop()

        buildPermutation([])

        return ans