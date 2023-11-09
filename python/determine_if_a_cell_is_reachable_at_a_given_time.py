# leetcode problem # 2849. Determine if a Cell Is Reachable at a Given Time

"""
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.

Example 1:
https://assets.leetcode.com/uploads/2023/08/05/example2.svg
Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
Output: true
Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above. 

Example 2:
https://assets.leetcode.com/uploads/2023/08/05/example1.svg
Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
Output: false
Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.

Constraints:
1 <= sx, sy, fx, fy <= 10^9
0 <= t <= 10^9
"""

"""
My solution: find the shortest path

The shortest path is the longer of the x or y distance from start to finish
- As it is possible to travel in a diagonal, the shorter of the x or y distance can be traversed
    while advancing in the longer direction, and will reach the correct x or y level before the
    longer direction is completed
- Extra time can be spent traversing in squares around the final square
=> As long as the shortest time taken is smaller than t, the operation is possible
* Edge Case: Shortest path is 0 and t = 1
    - if shortest path is 0, it is impossible to traverse to another square and return
    in 1 second
    - if t > 1, the operation is possible

Runtime: O(1), time does not depend on input
Space: O(1)
"""


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        shortestTime = max(abs(sx - fx), abs(sy - fy))

        if shortestTime == 0 and t == 1:
            return False

        return shortestTime <= t
