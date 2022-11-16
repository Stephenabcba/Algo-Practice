# leetcode problem # 374. Guess Number Higher or Lower

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.



Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
"""

"""
My solution: Binary search the possible number range

As the problem is able to provide feedback on whether the value is larger or smaller, binary search can
be applied here.

With every guess, binary search will either reach the answer, or cut the number of possible values in half.
- If n == 100, and pick is 80:
    - Guess 1: 50, API returns pick is larger. there's no reason to consider 1-50 anymore, as 50 >= any value between 1-50
        and it is known that the pick is larger than 50 (pick > 50 >= (any value between 1 and 50))
    - Guess 2: 75, API returns pick is larger, there's no reason to consider 51-75
    - ... repeat until 80 is guessed, then return 80


Runtime: O(logN) where N is the input integer n
Space: O(1), memory usage should not scale with input
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        upper = n
        lower = 1

        mid = (upper + lower) // 2

        res = guess(mid)

        while (res != 0):
            if res < 0:
                upper = mid - 1
            else:
                lower = mid + 1
            mid = (upper + lower) // 2
            res = guess(mid)

        return mid
