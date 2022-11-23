# leetcode problem # 279. Perfect Squares

"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 10^4
"""

"""
Solution from Leetcode by md2030: DP solution

Intuition: build a dp array from 1 to N
- for every new value i processed, check all integers j from 1 to i to find the smallest sum of dp[j] + dp[i - j]
    * j + i - j == i, where j and i-j are both smaller than i
- if i is a perfect square, dp[i] = 1

Improvement: The values can only be smaller if j is a perfect square
- does not need to check any values of j that are not perfect squares

Improvement 2: To save the progress of dp array, make it a class variable

Runtime: O(n sqrt(n)) where n is the input integer 
Space: O(N) where n is the input integer 


"""


class Solution:

    # Make dp a class variable :)
    dp = [0]

    def numSquares(self, n: int) -> int:

        dp = self.dp

        # Precompute the perfect squares.
        perfectSq = [pow(i, 2) for i in range(1, int(sqrt(n))+1)]

        # We are building dp up to length n+1.
        while len(dp) < n+1:

            # Will add this new element to dp
            dpI = inf

            # dp equation
            for ps in perfectSq:
                if len(dp) < ps:
                    break
                dpI = min(dpI, 1+dp[-ps])

            dp.append(dpI)

        return dp[n]
