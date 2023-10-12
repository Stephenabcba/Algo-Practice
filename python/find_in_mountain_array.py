# leetcode problem # 1095. Find in Mountain Array

"""
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:
3 <= mountain_arr.length() <= 10^4
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""

"""
My solution: Three Binary Searches

Observations:
1. The target can only occur at most twice in the mountain array
- if it occurs 0 times, return -1
- if it occurs 1 time, return the index of target
- if it occurs 2 times, return the index of target at the increasing part before the peak
2. Without knowledge of where the peak is, binary search cannot be performed
- it is impossible to know whether the target is to the left or the right of a guess

Binary Search #1: Find the peak in mountain array
- if the guess is smaller than its right neighbor, the peak must be to the right of the guess
- otherwise, the peak is the guess or to the left of the guess

Binary Search #2: Look for target in the strictly increasing subarray before the peak
- if the guess is the target, return the index of the guess
- if the guess is smaller than the target, the target could only be to the right of the guess
- if the guess is larger than the target, the target could only be to the left of the guess

Binary Search #3: Look for target in the strictly decreasing subarray after the peak
- if the guess is the target, return the index of the guess
- if the guess is larger than the target, the target could only be to the right of the guess
- if the guess is smaller than the target, the target could only be to the left of the guess

The restriction of at most 100 calls is always satisfied given the problem constraints
- Binary search #1 takes 2 * logN calls, which is 28(rounded up) when N is at its maximum of 1e4
- Binary search #2 and binary search # 3 takes at a combined logN calls, which is 14 when N is at its maximum of 1e4
-> In total, the program can make up to 42 calls to MountainArray.get()

Runtime: O(logN) where N is the length of MountainArray
Space: O(1), memory usage does not depend on input
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low = 0
        high = mountain_arr.length() - 1
        while low < high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid

        peak = low
        low = 0
        high = peak + 1
        while low < high:
            mid = (low + high) // 2
            midVal = mountain_arr.get(mid)
            if midVal == target:
                return mid
            elif midVal < target:
                low = mid + 1
            else:
                high = mid

        low = peak + 1
        high = mountain_arr.length()
        while low < high:
            mid = (low + high) // 2
            midVal = mountain_arr.get(mid)
            if midVal == target:
                return mid
            elif midVal > target:
                low = mid + 1
            else:
                high = mid
        return -1