# leetcode problem # 486. Predict the Winner

"""
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Example 1:
Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.

Example 2:
Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 10^7
"""

"""
My solution: Dynamic Programming

Idea:
Try all combinations, and keep track of the combinations seen and their scores
- Alternate turns between player1 and player2
If a combination is seen before, no further calculation is needed

Check whether player 1 has a higher score than player 2

Runtime: O(N^2) where N is the length of nums list
Space: O(N^2) 
"""

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[[-1, -1] for _ in range(len(nums) + 1)] for __ in range(len(nums))]
        
        for idx in range(len(nums)):
            dp[idx][0][0] = dp[idx][0][1] = dp[idx][1][1] = 0
            dp[idx][1][0] = nums[idx]

        def play(start, length):
            if dp[start][length][0] >= 0:
                return
            play(start + 1, length - 1)
            play(start, length - 1)
            option1 = dp[start + 1][length - 1]
            option2 = dp[start][length - 1]
            if option1[1] + nums[start] > option2[1] + nums[start + length - 1]:
                dp[start][length][0] = option1[1] + nums[start]
                dp[start][length][1] = option1[0]
            else:
                dp[start][length][0] = option2[1] + nums[start + length - 1]
                dp[start][length][1] = option2[0]

        play(0, len(nums))

        return dp[0][-1][0] >= dp[0][-1][1]