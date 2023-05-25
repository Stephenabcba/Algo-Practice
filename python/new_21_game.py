# leetcode problem # 837. New 21 Game

"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Example 1:
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.

Example 2:
Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.

Example 3:
Input: n = 21, k = 17, maxPts = 10
Output: 0.73278

Constraints:
0 <= k <= n <= 10^4
1 <= maxPts <= 10^4
"""

"""
My solution: Sliding window

Sliding Window Approach:
1. For any point value X, there are up to (maxPts) ways to reach the value from a previous state.
    - from (X - maxPts), Alice could draw a card worth maxPts to reach X
    - from (X - maxPts + 1), Alice could draw a card worth maxPts - 1 to reach X
    - for every point value in between, Alice could draw a valid card to reach X
2. The probability to draw the desired card is 1 / maxPts
-> The total probability to reach a point value X at some point in the game is:
    (Sum of all possible values' probilities) / maxPts
* when iterating through the values, the sum of the probabilities can be updated in constant time by
using a sliding window
    - remove the value exiting the window
    - add the new value entering the window
3. After the points exceed K, Alice would not draw anymore, so the window would not include any starting
values >= K

The processing is done in 2 parts:
Part 1: Point values within the range of first draw
- The probability to reach a point value X is the probability of reaching X
    in the first draw + the probability of reaching X after multiple draws
    -> the probability is (1 + window Probability) / maxPts
Part 2: The rest of the point values
- The initial draw could not reach these point values, so the probability is just
    (window Probability) / maxPts
- Once the window reaches a probability of 0, it is impossible to draw any point value
larger than the current point value

The total probability to end with points under N is the sum of the probabilities between
K and N

Edge Case: k = 0
- when k is 0, Alice will never draw a card.
- since n >= k, the points earned will always be 0 and be under n
-> probability is 1

Runtime: O(N) where N is the integer N
Space: O(N)
"""


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        probabilities = [0 for _ in range(n + 1)]
        windowPts = 0

        for i in range(1, maxPts + 1):
            if i <= n:
                probabilities[i] = (1 + windowPts) / maxPts
                if i < k:
                    windowPts += probabilities[i]

        for i in range(maxPts + 1, n + 1):
            probabilities[i] = windowPts / maxPts
            windowPts -= probabilities[i - maxPts]
            if i < k:
                windowPts += probabilities[i]
            if windowPts <= 0:
                break

        return sum(probabilities[k:])
