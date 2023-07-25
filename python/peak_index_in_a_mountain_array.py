# leetcode problem # 852. Peak Index in a Mountain Array

"""
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 10^5
0 <= arr[i] <= 10^6
arr is guaranteed to be a mountain array.
"""

"""
My solution: binary search

observation: the mountain array must be strictly increasing or decreasing from one value to the next
- any value in the array cannot be equal to the previous or the next value in the array
- ex: [0,1,1,0] is NOT a mountain array, 1 is not greater than or less than 1
-> a value in the array can be compared against the previous or the next value to find whether
the mountain array is increasing or decreasing that point
* also, the peak of the mountain cannot be at the start or the end of the mountain array

Logic: binary search
- with binary search, half of the solution space can be eliminated with each iteration
    - this satisfies the O(logN) time requirements
- it is deterministic which half of the solution space should be removed in each iteration
    - if the array is increasing (the current value is lower than the next value), the
    peak is to the right of the current value
    - if the array is decreasing (the current value is higher than the next value), the
    peak is either the current value or to the left of the current value
    - by definition, the mountain cannot "plateau" or be equal to the previous or the next value.
    * as the peak cannot be at the end of the mountain array, the last value will not be checked
    as a candidate; index out of bounds would not occur.

Runtime: O(logN) where N is the length of the mountain array
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)

        while start < end:
            middle = (start + end) // 2
            if arr[middle] > arr[middle + 1]:
                end = middle
            else:
                start = middle + 1

        return start