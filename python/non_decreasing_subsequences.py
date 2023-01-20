# leetcode problem # 491. Non-decreasing Subsequences

"""
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.


Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]

Constraints:
1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""

"""
My solution: Iteratively build the solutions

Logic:
- Sequentially process each number
- if the number is larger than or equal to the largest
    value in the previously built lists, create a copy
    of the list and append the number
- to access the lists that fit the criteria, save the lists
    in a dictionary, with the key as the largest value in the
    list (as the lists are non-decreasing, the largest value
    is always the last value added)

Note: The problem does not want duplicate subsequences
- ex: [7,7] should only occur once in the answer list, 
    even if multiple can be made from the nums list
- To remove duplicates, the data is stored in sets and the
    lists are stored as tuples (lists cannot be stored in sets)
    - The set of tuples are converted to list of lists at the end

Runtime: O(2^N * N^2) where N is the length of nums list
Space: O(2^N * N^2)
"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ansSet = set()
        maxDict = {}
        for num in nums:
            maxDict[num] = maxDict.get(num, set())
            newVals = []
            for maxVal in maxDict:
                if maxVal <= num:
                    for subSeq in maxDict[maxVal]:
                        newSeq = subSeq + (num,)
                        ansSet.add(newSeq)
                        newVals.append(newSeq)
            # to avoid infinite loop processing the new lists during
            # iteration
            maxDict[num].add((num,))
            for newVal in newVals:
                maxDict[num].add(newVal)
        ans = []
        for tupleSeq in ansSet:
            ans.append(list(tupleSeq))
        return ans
