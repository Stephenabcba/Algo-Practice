# leetcode problem # 452. Minimum Number of Arrows to Burst Balloons

"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1
"""

"""
My solution: Sort then group the balloons

Although the question puts the balloons on an XY-plane, the Y-axis location of the balloons do not matter at all as the
arrow will travel in the Y-direction infinitely.

Intuition:
After sorting the balloons based on their x_start location, group them together
- each arrow will be shot at the lowest x_end of the group
- if a balloon has an x_start larger than the x_end of a group, a new group is created
    - shoot an arrow to pop the last group of balloons
    * as the arrow is always shot to pop the previous group of balloons, an arrow is needed at the end
    to pop the final group 

Runtime: O(N * logN) where N is length of points list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        takenShots = 0

        shot = points[0][1]
        for point in points:
            # x_start exceeds the x_end of the last group, shoot the arrow and form a new group
            if point[0] > shot:
                takenShots += 1
                shot = point[1]

            # find the lowest x_end of the group
            shot = min(shot, point[1])

        takenShots += 1

        return takenShots
