# leetcode problem # 1846. Maximum Element After Decreasing and Rearranging

"""
You are given an array of positive integers arr. Perform some operations (possibly none) on arr so that it satisfies these conditions:

The value of the first element in arr must be 1.
The absolute difference between any 2 adjacent elements must be less than or equal to 1. In other words, abs(arr[i] - arr[i - 1]) <= 1 for each i where 1 <= i < arr.length (0-indexed). abs(x) is the absolute value of x.
There are 2 types of operations that you can perform any number of times:

Decrease the value of any element of arr to a smaller positive integer.
Rearrange the elements of arr to be in any order.
Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

Example 1:
Input: arr = [2,2,1,2,1]
Output: 2
Explanation: 
We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
The largest element in arr is 2.

Example 2:
Input: arr = [100,1,1000]
Output: 3
Explanation: 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange arr so it becomes [1,100,1000].
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now arr = [1,2,3], which satisfies the conditions.
The largest element in arr is 3.

Example 3:
Input: arr = [1,2,3,4,5]
Output: 5
Explanation: The array already satisfies the conditions, and the largest element is 5.

Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
"""

"""
My solution: sort then decrease

Observations:
1. Rearranging is preferred over decreasing values
- When decreasing values, the maximum value could be lowered by the process
- ex: [3,2,1] becomes [1,1,1], when rearranging arr can yield [1,2,3]
    -> when decreasing, the maximum was lowered to 1, when rearranging would yield 3
2. The maximum value of any given list is the length of the list
- as the absolute difference between neighboring elements is 1, the best case scenario is
    a strictly increasing sequence in the form of [1,2,3...,N-1,N]

Logic:
1. Sort the list first
2. Iterate through each value in the list
    - if the current value is smaller than the expected next value, skip it
    - otherwise, lower the current value to the next expected value
3. Return the maximum value

Runtime: O(N * logN) where N is the arr list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxValue = 0
        idx = 0

        while idx < len(arr):
            idx += 1
            if arr[idx - 1] < maxValue + 1:
                continue

            maxValue += 1

        return maxValue
