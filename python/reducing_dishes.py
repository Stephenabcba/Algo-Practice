# leetcode problem # 1402. Reducing Dishes

"""
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
Each dish is prepared in one unit of time.

Example 2:
Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)

Example 3:
Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People do not like the dishes. No dish is prepared.

Constraints:
n == satisfaction.length
1 <= n <= 500
-1000 <= satisfaction[i] <= 1000
"""

"""
My solution: sort the dishes

Observation 1: including a dish with positive score will always increase the final score
Observation 2: a dish with a largest score should be placed last to maximize the final score
Observation 3: Including a dish with a negative score may increase or decrease the final score

Logic:
1. Sort the dishes from largest to smallest
2. Iterate through each dish
    - technically, the dishes are being arranged from back to front in this order
    - calculate the incremental increase by including the current dish
        - the incremental increase is the sum of all the dishes up to the current dish
            - this effectively raises the multiplier of all previous dishes by 1
                - ex: 2 * 0 + 3 * 1 + 4 * 2 becomes 2 * 1 + 3 * 2 + 4 * 3 when (2 + 3 + 4 = 9) is added
    - if the incremental increase is greater than 0, include the current dish and increase the final score
    - otherwise, break iteration
3. return the final score

Runtime: O(N * logN) where N is the number of dishes
Space: O(1), memory usage does not depend on input.
"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        score = 0
        increaseAmount = 0

        for dish in satisfaction:
            increaseAmount += dish
            if increaseAmount > 0:
                score += increaseAmount
            else:
                break

        return score
