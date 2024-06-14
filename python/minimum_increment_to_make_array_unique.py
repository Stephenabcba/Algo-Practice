# leetcode problem # 945. Minimum Increment to Make Array Unique

"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""

"""
My solution: Sort then solve

Idea:
1. The problem is simplified after sorting
    - smaller values are processed before larger values
2. Keep track of the smallest available value X to be occupied
    - if the current value Y is larger than or equal to X, then no change is needed, X becomes Y + 1
    - if the current value Y is smaller than X, Y needs (Y - X) moves to change to X, and X becomes X + 1

Runtime: O(N*logN) Where N is the length of nums
Space: O(N)
"""


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        available = nums[0] + 1
        moves = 0

        for num in nums[1:]:
            if num >= available:
                available = num + 1
            else:
                moves += available - num
                available += 1

        return moves
