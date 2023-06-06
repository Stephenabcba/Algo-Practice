# leetcode problem # 1502. Can Make Arithmetic Progression From Sequence

"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:
2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""

"""
My solution: sort and check

sort arr and check that the difference between every consecutive values is the same.

Runtime: O(N logN) where N is the length of list arr
Space: O(N)
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sortedArr = sorted(arr)

        diff = sortedArr[1] - sortedArr[0]

        for idx in range(2,len(sortedArr)):
            if sortedArr[idx] - sortedArr[idx - 1] != diff:
                return False

        return True