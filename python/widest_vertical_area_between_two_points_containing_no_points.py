# leetcode problem # 1637. Widest Vertical Area Between Two Points Containing No Points

"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Example 1:
https://assets.leetcode.com/uploads/2020/09/19/points3.png
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3

Constraints:
n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9
"""

"""
My solution: Sort then solve

Through sorting, the horizontal distance between any two neighboring points is alawys the minimum distance between them
    - before sorting, it is not certain whether this is the case
        - ex: [[3,3], [1,1], [2,2]]: 3 and 1 are neighboring points, but the closest point to 3 is 2.
Since the problem is only concerned with the widest vertical area, only the x values need to be compared
After sorting, compare the x values of neighboring points and find the maximum gap.

Runtime: O(N * logN) where N is the number of points
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widest = 0
        for idx in range(1, len(points)):
            if points[idx][0] - points[idx - 1][0] > widest:
                widest = points[idx][0] - points[idx - 1][0]
        return widest
