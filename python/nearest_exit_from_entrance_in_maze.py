# leetcode problem # 1926. Nearest Exit from Entrance in Maze

"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.


Example 1:
https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.


Constraints:
maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrance_row < m
0 <= entrance_col < n
entrance will always be an empty cell.
"""

"""
My solution: breadth-first search

As the problem is asking for a path from the entrance to the exit, a path-finding algorithm can be used.

Breadth-first search (BFS) and Depth-first search (DFS) are commonly used, and BFS is chosen here.

BFS explores the map by processing the nodes closest to the originating node first, instead of
exhausting a single path before moving to the next path.

Here, the BFS logic is implemented with a queue using the deque class.

Logic:
1. initialize the DP matrix to keep track of the nodes that have been processed already
2. initialize the queue, and add the entrance node into it
3. process through each node in the queue
    i. if the node is out of bounds, move on
    ii. if the node has been processed, move on
    iii. if the node is a wall, move on
    iv. otherwise:
        - mark the node as visited
        - add the nodes in 4 directions that it can travel to to the queue
        - if the node is on the edge of the maze, it could be an exit
            - unless the node is the entrance node, then it can't be an exit node by problem definition
            - check if the path to the node is shorter than the current shortest path
4. After all nodes in the queue have been processed, return the length of the shortest path found.
- if there were no paths found, return -1
    - check whether the path has been lowered from the impossible path length.


Runtime: O(N*M) where N and M are the length and width of the maze
Space: O(N + M) where N and M are the length and width of the maze
"""




from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        mazeWidth = len(maze[0])
        mazeLength = len(maze)

        dp = [[False for j in range(mazeWidth)] for i in range(mazeLength)]

        q = deque()
        q.append((entrance, 0))

        shortestPath = 1000000

        while (len(q) > 0):
            node, steps = q.popleft()
            nodeX, nodeY = node

            # index out of bounds, don't process the coordinate
            if nodeX < 0 or nodeX >= mazeLength or nodeY < 0 or nodeY >= mazeWidth:
                continue

            # only process nodes that have not been accessed before
            if not dp[nodeX][nodeY]:
                dp[nodeX][nodeY] = True
                # only empty cells (no walls) can be traversed
                if maze[nodeX][nodeY] == ".":
                    q.append(([nodeX + 1, nodeY], steps + 1))
                    q.append(([nodeX - 1, nodeY], steps + 1))
                    q.append(([nodeX, nodeY + 1], steps + 1))
                    q.append(([nodeX, nodeY - 1], steps + 1))

                    # index reached a potential exit, process the number of steps
                    if nodeX == 0 or nodeX == mazeLength - 1 or nodeY == 0 or nodeY == mazeWidth - 1:
                        # make sure the cell is not the entrance
                        if nodeX != entrance[0] or nodeY != entrance[1]:
                            if steps < shortestPath:
                                shortestPath = steps

        if shortestPath == 1000000:
            return -1
        return shortestPath
