# leetcode problem # 912. Sort an Array

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:
1 <= nums.length <= 5 * 10^4
-5 * 104 <= nums[i] <= 5 * 10^4
"""

"""
Solution: Merge sort

Logic taken from Merge Sort page on GeeksforGeeks.org: https://www.geeksforgeeks.org/merge-sort/

Idea:
1. Split the array in half until each subarray has size of 1
2. Merge neighboring subarrays until the whole array is sorted
    - by default, subarrays of size 1 must be sorted
    - when merging, maintain sorted order

Runtime: O(N * logN) where N is the number of elements in the list
Space: O(N)

"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) > 1:
                left = arr[:len(arr) // 2]
                right = arr[len(arr) // 2:]
                mergeSort(left)
                mergeSort(right)

                leftIdx = rightIdx = k = 0

                while leftIdx < len(left) and rightIdx < len(right):
                    if left[leftIdx] < right[rightIdx]:
                        arr[k] = left[leftIdx]
                        leftIdx += 1
                    else:
                        arr[k] = right[rightIdx]
                        rightIdx += 1
                    k += 1

                while leftIdx < len(left):
                    arr[k] = left[leftIdx]
                    leftIdx += 1
                    k += 1

                while rightIdx < len(right):
                    arr[k] = right[rightIdx]
                    rightIdx += 1
                    k += 1

        mergeSort(nums)
        return nums
