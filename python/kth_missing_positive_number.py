# leetcode problem # 1539. Kth Missing Positive Number

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
 

Follow up:

Could you solve this problem in less than O(n) complexity?
"""

"""
My solution: Count the missing numbers

There are multiple cases for where the missing numbers can be
1. The missing number is smaller than the smallest number in arr
    - the missing number is k
2. The missing number is somewhere in between two numbers in arr
    - iteratively process the numbers in arr
        - when the numbers increase more than +1 between two numbers,
        there are missing numbers
3. The missing number is larger than the largest number in arr
    - the missing number is (largest + k - missingCount)
    - missingCount is the number of missing numbers found in the list
        - in the entire list, missingCount = largest - len(arr)

Runtime: O(N) where N is the length of the arr list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingCount = 0
        idx = 0
        curVal = 1

        while missingCount < k:
            if idx < len(arr):
                if curVal < arr[idx]:
                    if arr[idx] - curVal >= k - missingCount:
                        curVal += k - missingCount - 1
                        missingCount = k
                    else:
                        missingCount += arr[idx] - curVal
                        curVal += arr[idx] - curVal + 1
                else:
                    curVal += 1
                idx += 1
            else:
                curVal += k - missingCount - 1
                missingCount = k

        return curVal
