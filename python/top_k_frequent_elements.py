# leetcode problem # 347. Top K Frequent Elements

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

"""
My Solution: find frequencies then sort

Idea: 
1. Find the frequencies of each unique value in nums
2. Sort the frequencies (with the corresponding unique values attached)
3. Return the top k unique values with the highest frequencies

Runtime: O(N * logN) where N is the length of nums list
Space: O(N)
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = {}

        for num in nums:
            if num not in numFrequency:
                numFrequency[num] = 1
            else:
                numFrequency[num] += 1

        frequencyList = [frequency for frequency in numFrequency.items()]

        frequencyList.sort(reverse=True, key=lambda x: x[1])

        ans = [val[0] for val in frequencyList[:k]]

        return ans
