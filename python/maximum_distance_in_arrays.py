# leetcode problem # 624. Maximum Distance in Arrays

"""
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Example 2:
Input: arrays = [[1],[1]]
Output: 0

Constraints:
m == arrays.length
2 <= m <= 10^5
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 10^4
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
"""

"""
My Solution: Check the first and last element of every array

Idea: To maximize distance, the larger value should be taken from the last element of an array, and the smaller value
should be taken from the first element of an array
- Ideally, the larger value is the largest of all the arrays, and the smaller value is the smallest of all the arrays
    - however, if the larger value and the smaller value are both taken from the same array, one of the two have to be replaced
    -> find the second largest and second smallest values, and find the maximum distance without taking both from the same array

Runtime: O(N) where N is the number of arrays
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lowest = arrays[0][0]
        lowestIdx = 0

        highest = arrays[0][-1]
        highestIdx = 0

        for idx in range(1, len(arrays)):
            if arrays[idx][0] < lowest:
                lowest = arrays[idx][0]
                lowestIdx = idx
            if arrays[idx][-1] > highest:
                highest = arrays[idx][-1]
                highestIdx = idx

        if lowestIdx != highestIdx:
            return highest - lowest

        secondLowest = arrays[0][0]
        secondLowestIdx = 0
        if lowestIdx == 0:
            secondLowest = arrays[1][0]
            secondLowestIdx = 1

        secondHighest = arrays[0][-1]
        secondHighestIdx = 0
        if highestIdx == 0:
            secondHighest = arrays[1][-1]
            secondHighestIdx = 1

        for idx in range(1, len(arrays)):
            if arrays[idx][0] < secondLowest and idx != lowestIdx:
                secondLowest = arrays[idx][0]
                secondLowestIdx = idx
            if arrays[idx][-1] > secondHighest and idx != highestIdx:
                secondHighest = arrays[idx][-1]
                secondHighestIdx = idx

        return max(highest - secondLowest, secondHighest - lowest)
