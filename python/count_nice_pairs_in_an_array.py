# leetcode problem # 1814. Count Nice Pairs in an Array

"""
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:
Input: nums = [13,10,35,24,76]
Output: 4

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

"""
My solution: Organize based on the difference between num and rev(num)

Observation: Nice pairs only occur in numbers that have the same difference between num and rev(num)
- ex: 42 - 24 = 18; 97 - 79 = 18 -> 42 and 97 form a nice pair

After taking count of all the numbers that form the same difference, the total number can be found with the
combination formula: Total! / (Chosen! * notChosen!)
    - since the problem is asking for pairs, Chosen! is always 2, and notChosen! is always (Total - 2)!
    -> The simplified equation is: Total * (Total - 1) / 2

Count all of the nice pairs and return at the end
    - since the value could be large, take modulo of the largePrime when adding

Runtime: O(N) where N is the length of nums list
Space: O(N)
"""


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        largePrime = 1000000007

        revDiff = defaultdict(int)

        for num in nums:
            revNum = 0
            numCopy = num
            while num > 0:
                revNum *= 10
                revNum += num % 10
                num = num // 10
            revDiff[numCopy - revNum] += 1

        nicePairs = 0

        for pairsCount in revDiff.values():
            nicePairs = (nicePairs + (pairsCount *
                         (pairsCount - 1)) // 2) % largePrime
        return nicePairs
