# leetcode problem # 1232. Check If It Is a Straight Line

"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

"""
My solution: Check the slope

If the points form a line, all lines connecting the first point to every other point should have the same slope
    - if the lines don't have the same slope, the dots don't form a line
    - the slope of a line is the rise of run, or difference in y / difference in x

Edge Case: the dots form a vertical line
    - the slope is infinite, and cannot be calculated with division
-> check that the change in X is 0 for every point in comparison to the first point

Runtime: O(N) where N is the number of dots
Space: O(1) memory usage does not depend on input
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        deltaY = (coordinates[1][1] - coordinates[0][1])
        deltaX = (coordinates[1][0] - coordinates[0][0])

        if deltaX == 0:
            for point in range(2, len(coordinates)):
                if (coordinates[point][0] - coordinates[0][0]) != 0:
                    return False
        else:
            slope =  deltaY / deltaX
            for point in range(2, len(coordinates)):
                deltaY = (coordinates[point][1] - coordinates[0][1])
                deltaX = (coordinates[point][0] - coordinates[0][0])
                if deltaX == 0:
                    return False
                if deltaY / deltaX != slope:
                    return False
            
        return True