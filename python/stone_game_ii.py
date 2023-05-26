# leetcode problem # 1140. Stone Game II

"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10^4
"""

"""
My solution: DP Working backwards

Logic:
When M is large enough to take all remaining stones, do it.
Otherwise, choose the number of piles resulting in the largest gains while keeping track of
the opponent's stones
    - the stones gained is equal to the total stones collected this round + the largest "opponent" stones
    reachable
        - the turns alternate between Alice and Bob, so the current turn is the previous turn's opponent
The current turn depends on the outcome of future turns, but the future turn does not depend on the current turn
as long as the state of the future turn is reached
-> working backwards yields a deterministic result

Runtime: O(N ^ 3) where N is the number of piles
Space: O(N ^ 2)
"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        numPiles = len(piles)
        if numPiles <= 2:
            return sum(piles)
        memo = [[[0, 0] for _ in piles] for __ in piles]

        for curStone in range(numPiles - 1, -1, -1):
            for m in range(1, min(2 * (curStone + 1) + 1, numPiles)):
                if curStone + m >= numPiles:
                    if curStone == numPiles - 1:
                        memo[curStone][m][0] = piles[-1]
                    else:
                        memo[curStone][m][0] = memo[curStone +
                                                    1][m][0] + piles[curStone]
                else:
                    gainedStones = piles[curStone]
                    maxStones = 0
                    oppStones = 0
                    for chosenStones in range(1, min(m + 1, numPiles)):
                        if gainedStones + memo[curStone + chosenStones][min(numPiles - 1, max(2 * chosenStones, m))][1] > maxStones:
                            maxStones = gainedStones + \
                                memo[curStone + chosenStones][min(
                                    numPiles - 1, max(2 * chosenStones, m))][1]
                            oppStones = memo[curStone + chosenStones][min(
                                numPiles - 1, max(2 * chosenStones, m))][0]
                        gainedStones += piles[curStone + chosenStones]
                    memo[curStone][m][0] = maxStones
                    memo[curStone][m][1] = oppStones

        return memo[0][2][0]


"""
Leetcode best runtime solution (161ms)

Prefix sum - prefixSum[i] is the sum of all values from i to the end of the list.

dp logic:
1. if i + m reaches the end of the array, take all remaining stones
2. otherwise, choose the number of piles that will result in the opponent taking the least amount of stones from the rest of
    the piles
    - the number of piles is limited from 0 to 2m

As the sum of stones is fixed, when the opponent's gained stones decrease, the playering gained stones increase
-> minimizing the opponent's gains results in the optimal gains for the player

In a chain of recursive calls, every recursive call is alternating turns between Alice and Bob


@lru_cache(None) will automatically create a memo for the dp function
- this is equivalent to using @cache

Runtime: O(N^2) where N is the number of piles
Space: O(N^2)?
"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)

        # make the prefix sum
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)
