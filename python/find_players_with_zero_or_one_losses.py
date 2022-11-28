# leetcode problem # 2225. Find Players With Zero or One Losses

"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:
Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

Constraints:
1 <= matches.length <= 10^5
matches[i].length == 2
1 <= winner_i, loser_i <= 10^5
winner_i != loser_i
All matches[i] are unique.
"""

"""
My solution: Keep track of the number of losses

Intuition:
To find which players have lost 0 or 1 times, keep track of the number of times each player have lost.
Filter through the counts and find the players who have lost a total of 0 or 1 times.

Logic:
1. Iterate through each match and keep track of the number of losses
- increment the loss count of each loser
- add the winner with 0 losses if needed
2. Find the players with 0 losses and add them to a winners list
3. Find the players with 1 loss and add them to a 1 loss list
4. Sort both lists and return them

* To keep count of the number of losses of each player, a dictionary can be used.

Runtime: O(N * logN) where N is the number of matches
- in the worst case, each winner has never lost, and the logic needs to sort every winner
Space: O(N) where N is the number of matches
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossCounts = {}

        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in lossCounts:
                lossCounts[winner] = 0
            if loser not in lossCounts:
                lossCounts[loser] = 0
            lossCounts[loser] += 1

        winners = []
        oneLoss = []

        for player in lossCounts:
            if lossCounts[player] == 0:
                winners.append(player)
            elif lossCounts[player] == 1:
                oneLoss.append(player)

        winners.sort()
        oneLoss.sort()

        return [winners, oneLoss]


"""
Solutions from Official Leetcode Solutions

1. Hash Set
- Use 3 sets to keep track: zero_loss, one_loss, and more_losses
- Add the winner to zero_loss if the player has never lost before
- Move the loser from n to n+1 losses (don't need to move losers in more_losses already)
- At the end:
    - convert zero_loss to a list and sort
    - convert one_loss to a list and sort

2. Hash Set + Hash Map
- Create a set for the players seen
- Create a dictionary for every player with at least one loss
- If a player is in the set but not in the dictionary, the player has never lost
- If a player has one loss in the dictionary, the player has one lost
- Add the players to the list accordingly and sort

3. Hash Map
- Similar logic to my solution.

4. Counting with Array
- Create an array of size K (where K is the constrained space for player values, K == 100001 here, from 0 to 10^5)
    - array is initialized with values of -1, signifying that the player has not been seen before
- Keep track of the number of losses using the array
    - array[i] = number of losses for player_i
- Iterate through the array and find the players with 0 or 1 losses
- As the array is inherently sorted, there's no need to sort the array again.
"""
