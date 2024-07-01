# leetcode problem # 1550. Three Consecutive Odds

"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

"""
My solution: Iteratively check each number

Idea: Keep a counter of consecutive odd numbers up to this point
- if the current number is odd, increment the counter
- if the current number is even, reset the counter to 0
- if the counter reaches 3, return True
- if the counter never reached 3 at the end, return False

Runtime: O(N) where N is the length of arr
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0

        for num in arr:
            if num % 2:
                oddCount += 1
                if oddCount == 3:
                    return True
            else:
                oddCount = 0

        return False
