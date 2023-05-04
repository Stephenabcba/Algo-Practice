# leetcode problem # 649. Dota2 Senate

"""
In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".


Example 1:
Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:
Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Constraints:
n == senate.length
1 <= n <= 10^4
senate[i] is either 'R' or 'D'.
"""

"""
My solution: Using Queues

Observation: A senator's best voting strategy is to vote out the next senator of the opposing
party that has the power to vote
    - if a senator is at the end, vote out the senator that will vote first in the next round
    - by doing so, the opposing party has decreased chance of being to vote, and the senator's party
    is more likely to vote

by using queues with the senators' index as the values, the algorithm can emulate the voting process
- the senator voting would remove the opposing party's next voting senator, and the senator who voted would be 
    moved to the next round
    - at the end of a round, a party's senator may be removing the next round's opposing senator's right to vote

Runtime: O(N) where N is the length of senate string
Space: O(N)
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        curRad = []
        curDire = []

        for idx, senator in enumerate(senate):
            if senator == "R":
                curRad.append(idx)
            else:
                curDire.append(idx)

        nextRad = []
        nextDire = []

        while len(curRad) > 0 and len(curDire) > 0:
            radIdx = 0
            direIdx = 0
            while radIdx < len(curRad) and direIdx < len(curDire):
                if curRad[radIdx] < curDire[direIdx]:
                    nextRad.append(curRad[radIdx])
                else:
                    nextDire.append(curDire[direIdx])
                radIdx += 1
                direIdx += 1

            if radIdx < len(curRad):
                nextDire = nextDire[len(curRad) - radIdx:]
                nextRad = nextRad + curRad[radIdx:]
            elif direIdx < len(curDire):
                nextRad = nextRad[len(curDire) - direIdx:]
                nextDire = nextDire + curDire[direIdx:]

            curRad = nextRad
            curDire = nextDire
            nextRad = []
            nextDire = []

        if len(curRad) > 0:
            return "Radiant"
        return "Dire"
