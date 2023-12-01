# leetcode problem # 935. Knight Dialer

"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:
https://assets.leetcode.com/uploads/2020/08/18/chess.jpg

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

https://assets.leetcode.com/uploads/2020/08/18/phone.jpg

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.


Example 1:
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

Constraints:
1 <= n <= 5000
"""

"""
My solution: Go through each iteration

Observations:
1. The knight cannot move from the square at 5
    - only dials with length of 1 can include 5
2. Most other squares have 2 paths, with the exception of 4 and 6
    - 4 and 6 have 3 paths that the knight can move to

Logic: Keep track of the number of ways to reach each square at each iteration, and increase the reachable
squares accordingly

Runtime: O(N) where n is the number of digits to dial
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        bigPrime = 1000000007
        old = [1 for _ in range(10)]
        old[5] = 0

        accessibilities = {
            1: [6, 8],
            2: [7, 9],
            3: [6, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        while n > 1:
            n -= 1
            new = [0 for _ in range(10)]
            for idx, ways in enumerate(old):
                for path in accessibilities[idx]:
                    new[path] = (new[path] + ways) % bigPrime
            old = new

        ans = 0
        for num in old:
            ans = (ans + num) % bigPrime

        return ans
