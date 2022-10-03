# leetcode problem # 1578. Minimum Time to Make Rope Colorful

"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

 

Example 1:
https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:
https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:
https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

Constraints:

n == colors.length == neededTime.length
1 <= n <= 10^5
1 <= neededTime[i] <= 10^4
colors contains only lowercase English letters.
"""

"""
My solution: find consecutive balloons and keep the most expensive to remove

From how the problem is defined, whenever there is a consecutive chain of balloons with the same color,
    only 1 balloon will remain from the chain; all other balloons in the chain are removed
* In the solution, the chain can have length of 1 (the balloon has different color than the previous and the next balloon)
    - in this case, no balloons are removed from the chain of 1 balloon.

In order to minimize the time cost of removing balloons, the balloons with the lowest time cost should be removed from a 
    consecutive chain first.
    - In other words, only the balloon with the highest time cost in the consecutive chain is kept in the chain.
    - In the solution, keep track of two things
        1. total time cost of removing every balloon in the consecutive chain
        2. the highest single time cost of removing a balloon
        - the total time to remove the required balloons is (1) - (2)

To find the start/end of a chain, compare the color of the balloon to the color of the previous balloon
- If both balloons are the same color, the current balloon is part of the chain of the previous balloon
    - update the max time to remove a balloon as needed
    - add the time cost of removing the balloon to the sum
- If the balloons have different colors, the current balloon is the start of a new chain of balloons
    - remove balloons as necessary from the previous chain
        - add the costs to the overall sum
    - reset the total time to remove all balloons in the chain to the current balloon

Runtime: O(N) where N is the number of balloons in colors string
Space: O(1), memory useage does not depend on input size
"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        maxTime = 0
        sumTime = 0
        prevColor = ''
        totalTime = 0

        for idx, balloon in enumerate(colors):
            if balloon == prevColor:
                maxTime = max(neededTime[idx], maxTime)
                sumTime += neededTime[idx]
            else:
                # if the color of the balloon is different from the previous balloon, the previous chain has ended
                # if the previous chain has a length of 1, maxTime == sumTime and no balloons are removed
                # a potential new consecutive chain has also started
                if idx > 0:
                    totalTime += sumTime - maxTime
                prevColor = balloon
                maxTime = neededTime[idx]
                sumTime = maxTime

        # at the end, remove balloons from the last consecutive chain as needed
        totalTime += sumTime - maxTime

        return totalTime
