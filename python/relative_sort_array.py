# leetcode problem # 1122. Relative Sort Array

"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

Constraints:
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""

"""
My solution: Modified Counting Sort

The items in arr1 can be grouped with a dictionary
The first half of arr1 can be sorted following the order of arr2
    - remove the dictionary entry after processing a value
The second half of arr1 can be sorted using counting sort

Runtime: O(N + M + k) where N is the length of arr1, M is the length of arr2, and k is the range of arr1
Space: O(N)
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Items = defaultdict(int)
        lowest, highest = min(arr1), max(arr1)
        for num in arr1:
            arr1Items[num] += 1

        mainIdx = 0
        for num in arr2:
            for occurrence in range(arr1Items[num]):
                arr1[mainIdx] = num
                mainIdx += 1
            del (arr1Items[num])

        for num in range(lowest, highest + 1):
            for occurrence in range(arr1Items.get(num, 0)):
                arr1[mainIdx] = num
                mainIdx += 1

        return arr1
