# leetcode problem # 2038. Remove Colored Pieces if Both Neighbors are the Same Color

"""
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.


Example 1:
Input: colors = "AAABABB"
Output: true
Explanation:
AAABABB -> AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.


Example 2:
Input: colors = "AA"
Output: false
Explanation:
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.


Example 3:
Input: colors = "ABBBBBBBAAA"
Output: false
Explanation:
ABBBBBBBAAA -> ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBBBBBAA -> ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.


Constraints:
1 <= colors.length <= 10^5
colors consists of only the letters 'A' and 'B'
"""

"""
My solution: Count the removeable pieces

Observations:
1. Moves made by Alice cannot interfere with Bob's available moves, and vice versa
- Alice can only remove "A" when both neighbors are "A"
    -> there must be at least 3 "A" in a group for Alice to remove a piece
    -> there will be at least 2 "A" remaining after Alice removes pieces from the group
    -> with "A" leftover, two groups of "B" will not merge, thus Bob do not get extra moves in any case
2. The order of moves that Alice performs do not affect her future moves
- if there's a group "AAAA", it doesn't matter if Alice removes the second or the third piece first.
- extension from Observation 1: Bob's moves do not affect Alice's moves
    -> Alice cannot lock herself out of a move that would later be unlocked by Bob's moves

Resulting solution:
1. Break the colors list into clusters of "A"s and "B"s
    - the clusters end and a new cluster starts when an opposite letter is encountered
2. Remove the maximum number of pieces from each cluster
    - if a cluster has fewer than 3 pieces, no pieces can be extracted from the cluster
    - if a cluster has 3 or more pieces, (len(cluster) - 2) pieces can be removed from the cluster
3. Compare the number of removeable pieces that Alice and Bob can remove at the end.
    - Alice wins if she has at least 1 more removeable piece than Bob
    - Otherwise, Bob wins.

Runtime: O(N) where N is length of colors list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        aRemoveCount = 0
        bRemoveCount = 0

        aCount = 0
        bCount = 0

        for color in colors:
            if color == "A":
                aCount += 1
                if bCount > 2:
                    bRemoveCount += bCount - 2
                bCount = 0
            else:
                bCount += 1
                if aCount > 2:
                    aRemoveCount += aCount - 2
                aCount = 0

        if aCount > 2:
            aRemoveCount += aCount - 2

        if bCount > 2:
            bRemoveCount += bCount - 2

        return aRemoveCount > bRemoveCount