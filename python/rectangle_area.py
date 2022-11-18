# leetcode problem # 223. Rectangle Area

"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).


Example 1:
https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png
Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45

Example 2:
Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16

Constraints:

-10^4 <= ax1 <= ax2 <= 10^4
-10^4 <= ay1 <= ay2 <= 10^4
-10^4 <= bx1 <= bx2 <= 10^4
-10^4 <= by1 <= by2 <= 10^4
"""

"""
My solution: Find the total area, subtract overlap as needed

The area of any triangle can be calculated with the formula Area = base * height,
where base is one of the sidelengths, and height is length of the side adjacent to the base.

Arbitrarily setting the horizonal sides as the base and the vertical sides as the height, the area
can be rewritten as Area = (x2 - x1) * (y2 - y1) where (x1, y1) is the bottom left vertex of the rectangle
and (x2, y2) is the top right vertex of the rectangle

If the two rectangles do not overlap, the area they cover is simply Area1 + Area2.

If the two rectangles do overlap, the overlap area must be subtracted from the sum.
- it can be proven that if there is overlap, the overlap must be a rectangle
- it can also be proven that the left side of the overlap must be the larger of the x1s
- and the right side of the overlap must be the smaller of the x2s
- the same logic can be applied to the y axis
-> The area of the overlap rectangle (if it exists) can be found.

The algorithm becomes finding the sum of area of both rectangles, then subtracting the overlap
area as needed.

Runtime: O(1), runtime does not depend on input
Space: O(1), space does not depend on input
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        totalArea = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)

        overlapX2 = min(ax2, bx2)
        overlapX1 = max(ax1, bx1)

        overlapY2 = min(ay2, by2)
        overlapY1 = max(ay1, by1)

        if overlapX2 > overlapX1 and overlapY2 > overlapY1:
            totalArea -= (overlapX2 - overlapX1) * (overlapY2 - overlapY1)

        return totalArea
