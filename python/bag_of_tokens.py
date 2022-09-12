# leetcode problem # 948. Bag of Tokens

"""
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.

Example 1:
Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

Example 2:
Input: tokens = [100,200], power = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.

Example 3:
Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], power < 10^4
"""

"""
My solution: sort then process

Observation: 
- If a token is to be placed up, the smallest token remaining is used first
- If a token is to be placed down, the largest token remaining is used first

Not mentioned in the problem statement: The score cannot go below 0
-> in the case of [71, 55, 82] with 54 as the initial power, 82 cannot be placed down first
    - if done, the tentative score becomes -1, even though the final score becomes 1
    - the correct answer is 0

By sorting the list from smallest to largest, it is trivial to find the next smallest / largest token
- Use two variables holding indeces of the smallest / largest token to serve as pointers for easy access
    - increment/decrement the indeces as the tokens are used.

Cases when processing the tokens:
1. Power >= smallest token:
- Play the smallest token face up, for +1 in score and some loss in power
2. Power + Largest token >= smallest token:
- Play the largest token face down and the smallest token face up
- + 0 in score and net gain of power (potential for more face up tokens)
- This is not a valid play if:
    - current score is 0 (tokens cannot be placed faced down, resulting in negative score)
    - the smallest and largest is the same token (each token can only be played at most once)
3. All other cases:
- it is impossible to increase the score more; end logic.

Runtime: O(N log N) where N is the number of tokens
- sorting is the most time-consuming step
Space: O(1), algorithm does not use input-scaling memory
- this assumes that the default sorting method does not use extra space.
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        frontPointer = 0
        backPointer = len(tokens) - 1
        score = 0

        while (frontPointer <= backPointer):
            if power >= tokens[frontPointer]:
                power -= tokens[frontPointer]
                score += 1
                frontPointer += 1
            elif frontPointer != backPointer and score > 0 and power + tokens[backPointer] >= tokens[frontPointer]:
                power += tokens[backPointer] - tokens[frontPointer]
                frontPointer += 1
                backPointer -= 1
            else:
                backPointer = frontPointer - 1

        return score
