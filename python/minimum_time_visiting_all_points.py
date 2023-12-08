# leetcode problem # 1266. Minimum Time Visiting All Points

"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Example 1:
https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

Example 2:
Input: points = [[3,2],[-2,2]]
Output: 5

Constraints:
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""

"""
My solution: Find the longer time taken for each path

The longer time taken for each path is the longer of the x or y distance from the previous point
- when there is a difference in both x and y direction, traverse diagonally, and the distance to be travelled is
    decremented by 1 in both directions
    - 1 second is taken for this move
- if there is a difference in only 1 direction, move 1 space in that direction
    - 1 second is taken for this move
-> the distance in the shorter direction do not affect the time taken

Add up all the time taken and return.

Runtime: O(N) where N is the number of points
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        timeTaken = 0
        prevX, prevY = points[0]

        for point in points[1:]:
            xDiff = abs(point[0] - prevX)
            yDiff = abs(point[1] - prevY)

            timeTaken += max(xDiff, yDiff)

            prevX, prevY = point

        return timeTaken
