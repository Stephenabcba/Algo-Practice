# leetcode problem # 1512. Number of Good Pairs

"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

"""
My solution: Dictionary and Math

Observation: 
1. A number can only form a good pair with another number with identical value
    - other values in the list do not interfere with the number of good pairs with this value
    -> numbers with identical values can be grouped together
2. The position of values do not really matter
    - regardless of whether the value is on index 0 or index 99, the number of good pairs formed do not change

Finding the number of good pairs:
1. Group the identical values in a dictionary
    - key is the value of the number
    - value is the numebr of times the value occurred
2. Calculate the number of good pairs each value can form
    - If there are 5 of the same value, the number of good pairs is 4 + 3 + 2 + 1 = 10
    - In general, with x of the same value, the number of good pairs is (x * (x - 1)) / 2
3. Return the total number of good pairs found after processing each unique number in the dictionary

Runtime: O(N) where N is the length of nums list
Space: O(N)
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numDict = defaultdict(int)

        for num in nums:
            numDict[num] += 1


        ans = 0
        for num in numDict:
            ans += (numDict[num] * (numDict[num] - 1)) // 2

        return ans