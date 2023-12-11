# leetcode problem # 1287. Element Appearing More Than 25% In Sorted Array

"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

"""
My solution: Binary Search 3 times

Observation: For an integer to take up more than 25% of the list, it must cross at least one of the 25th quartile, median, and 75th quartile
-> Only 3 potential candidates to test

Binary search the three values, and find out which one has more than 25% occurrance in the list.

Runtime: O(logN) where N is the length of list arr
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        middle = len(arr) // 2
        quart25 = middle // 2
        quart75 = (middle + len(arr)) // 2

        def binSearch(array, val):
            rangeStart = 0
            rangeEnd = len(array) - 1

            end = len(array) - 1

            while rangeStart < end:
                mid = (rangeStart + end) // 2
                if array[mid] >= val:
                    end = mid
                else:
                    rangeStart = mid + 1

            start = rangeStart

            while start < rangeEnd:
                mid = ceil((start + rangeEnd) / 2)
                if array[mid] > val:
                    rangeEnd = mid - 1
                else:
                    start = mid
            return rangeEnd - rangeStart + 1 > len(array) // 4

        if binSearch(arr, arr[quart25]):
            return arr[quart25]
        if binSearch(arr, arr[middle]):
            return arr[middle]
        if binSearch(arr, arr[quart75]):
            return arr[quart75]
