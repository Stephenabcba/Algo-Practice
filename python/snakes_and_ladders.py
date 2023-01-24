# leetcode problem # 909. Snakes and Ladders

"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:
https://assets.leetcode.com/uploads/2018/09/23/snakes.png
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1

Constraints:
n == board.length == board[i].length
2 <= n <= 20
grid[i][j] is either -1 or in the range [1, n^2].
The squares labeled 1 and n^2 do not have any ladders or snakes.
"""

"""
My solution: BFS

The problem is essentially for the shortest path (minimum moves) to reach
the end of the board, which makes pathfinding algorithms useful.
BFS (breadth first search) is a pathfinding algorithm that could find the
shortest path.

Intuition:
- The most straightforward path (assuming no bridges or snakes) from start
to end is rolling a 6 every time until the end is reached.
    - Assuming no bridges or snakes are in the way, rolling 3 twice is inefficient
    compared to rolling a 6 once
- Taking a bridge could potentially make progress in the path, but it could also
skip other bridges that crosses over longer distances
- Taking a snake loses progress, but could allow access to bridges that were skipped,
making net progress
- Therefore, to minimize the number of moves from start to end, only 3 types of paths
are considered every dice roll
    1. The longest path that doesn't result in a bridge or snake
        - if bridges and snakes are not on current square + 6, roll a 6
        - otherwise, check current square + 5, current square + 4...
        - it is possible that all possible rolls result in a bridge or snake,
            and this path is skipped
    2. Any path that results in a bridge
    3. Any path that results in a snake

Optimization: Implementing a visited array
- Keep track of the number of moves required to reach any square from start to finish
- If it takes more moves to reach the current state than the previous movesets, there
is no reason to try navigating through the same square
    - ex: if it takes 3 moves to reach 25 in the current moveset when previous moves
    were able to reach 25 in 2 moves, the minimum path would've been found in the previous
    iteration; the current moveset can be skipped
*** Note that if the square is the start of the bridge or a snake, the square isn't
"reachable" from landing on the square through dice rolling, as doing so will just
move the current square to the end of the brige/snake
    - to actually reach the square, the square must be the end of a bridge/square
    - it is not an issue that a square isn't reachable, but not handling the special
    case will result in the algorithm not working.

Runtime: O(N^2) where N is the sidelength of the board
Space: O(N^2)
"""


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        boardSize = len(board)
        destinationSquare = boardSize ** 2

        def navigate(squareNum):
            squareNum -= 1
            row = boardSize - (squareNum // boardSize) - 1
            col = squareNum % boardSize
            if (boardSize - row) % 2 == 0:
                col = boardSize - col - 1
            return [row, col]

        queue = [[1, 0]]
        queueIdx = 0

        visited = [float('inf') for _ in range(destinationSquare + 1)]

        while queueIdx < len(queue):
            curSquare = queue[queueIdx][0]
            curMoves = queue[queueIdx][1]
            queueIdx += 1
            if curMoves > visited[curSquare]:
                continue
            takenNormalRoute = False
            for roll in range(6, 0, -1):
                if curSquare + roll > destinationSquare:
                    continue
                row, col = navigate(curSquare + roll)

                if board[row][col] != -1:
                    queue.append([board[row][col], curMoves + 1])
                    visited[board[row][col]] = min(
                        visited[board[row][col]], curMoves + 1)
                else:
                    visited[curSquare +
                            roll] = min(visited[curSquare + roll], curMoves + 1)
                    if not takenNormalRoute:
                        takenNormalRoute = True
                        queue.append([curSquare + roll, curMoves + 1])
        return visited[destinationSquare] if visited[destinationSquare] != float('inf') else -1
