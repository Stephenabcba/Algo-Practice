# leetcode problem # 1636. Sort Array by Increasing Frequency

"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

"""
My solution: Store to a dictionary then sort

Logic:
1. Get the count of each number
    - the counts are stored in a dictionary
2. Sort the numbers based on count then based on value
    - the frequency and value are stored in a separate list
    - by default, python sorts list of lists in ascending order with the first item of
    each list, then in ascending order of the second item if the value of the first item
    is the same
        -> the frequency is stored first, and the value of the number is reversed to present them
        in decreasing order for the output
3. Recreate nums in sorted order
    - based on the frequency and order, nums can be repopulated with the correct values
4. return nums

Runtime: O(N * logN) where N is the length of nums
Space: O(N)
"""


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCount = defaultdict(int)

        for num in nums:
            numCount[num] += 1

        reversedCount = []

        for num, freq in numCount.items():
            reversedCount.append([freq, -num])

        reversedCount.sort()

        idx = 0

        for freq, num in reversedCount:
            for _ in range(freq):
                nums[idx] = -num
                idx += 1

        return nums
