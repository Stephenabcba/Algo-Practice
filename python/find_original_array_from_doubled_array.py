# leetcode problem # 2007. Find Original Array From Doubled Array

"""
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.


Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Constraints:

1 <= changed.length <= 10^5
0 <= changed[i] <= 10^5
"""

"""
My solution: Sort then process

By sorting the changed array from smallest to largest first, every value is either a value in the original array or the doubled value of the smallest unpaired original value
- if the array is a doubled array, the original array should be half the length of the changed array
- otherwise, the original array would have too many values due to how the logic is implemented.
- Using example 1:
    sorted array is [1,2,3,4,6,8]
        1 must be in the original array, since there's no values in the original array to double - > original = [1]
        2 is a doubled value, as it is twice the value of 1 -> original = [1]
        3 must be in the original array, since there's no values in the original array to double - > original = [1, 3]
        4 must be in the original array, as 4 != 6 = 3 * 2 -> original = [1,3,4]
        6 is a doubled value
        8 is a doubled value
        -> The resulting array has a length of 3, which is half of the changed array's length of 6
        => The input array is a doubled array, return the array

Runtime: O(N * log N) where N is the number of elements in the changed array (input)
- sorting is the most time-intensive process
Space: O(N) where N is the number of elements in the changed array (input)
- The only scaling memory usage is the original array (output)
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()

        original = []
        ogIndex = 0

        for number in changed:
            # if there's no values to double, or the current value is not the double of the smallest unpaired original value
            # add the current value to the original array
            if ogIndex >= len(original) or original[ogIndex] * 2 != number:
                original.append(number)
            # the current value is a doubled value, increment the pointer of the smallest unpaired value
            elif original[ogIndex] * 2 == number:
                ogIndex += 1

        if len(original) * 2 == len(changed):
            return original
        return []
