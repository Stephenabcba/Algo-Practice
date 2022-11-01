# leetcode problem # 1706. Where Will the Ball Fall

"""
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.


Example 1:
https://assets.leetcode.com/uploads/2019/09/26/ball.jpg
Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:
Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Example 3:
Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
"""

"""
My solution: Follow the rules and traverse using recursion

Intuition: Follow each ball as it falls through the maze.

Recursion Logic:
Base Case:
1. Ball exits through the bottom of the maze
    - return the position where the ball exited
2. Ball got stuck
    - return -1, no need to recurse
    - Conditions for getting stuck: (either condtion will get the ball stuck)
        i. the path directs the ball into the wall
            - ex. the path directs right, and the ball is already next to the right-side wall
        ii. the path directions into a path of opposite direction
            - ex. the path directs right, and the path on the right directs left

Recursive Case:
If the base cases were not reached, traverse one level below, following the direction of the current path
- ex: if the path directs right AND the ball did not get stuck or exit the maze, move one space to the right
    and one space below.


This solution can also be done iteratively.

Runtime: O(N * M) where N and M are the width and height of the grid, respectively.
Space: O(N), where N is the width of the grid.
- This excludes the memory useage of recursion.
"""


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        boardHeight = len(grid)
        boardWidth = len(grid[0])

        def traverseBoard(x, y):
            if y >= boardHeight:
                return x
            if grid[y][x] == 1:
                if x == boardWidth - 1 or grid[y][x + 1] == -1:
                    return -1
                return traverseBoard(x + 1, y + 1)
            else:
                if x == 0 or grid[y][x-1] == 1:
                    return -1
                return traverseBoard(x - 1, y + 1)

        ans = []
        for ball in range(boardWidth):
            ans.append(traverseBoard(ball, 0))

        return ans
