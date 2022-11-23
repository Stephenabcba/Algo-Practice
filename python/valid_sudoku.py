# leetcode problem # 36. Valid Sudoku

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

"""
My solution: Check the board according to definition

The board is checked 3 times in total
Check # 1: check numbers in every row is unique
Check # 2: check numbers in every column is unique
Check # 3: check numbers in every sub-box is unique

Runtime: O(1), although the runtime technically scales with board size, as the board size is fixed, the algorithm can be done in fixed time
Space: O(1), same logic as runtime.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        curSet = {"1"}
        # check all rows
        for row in range(9):
            curSet.clear()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in curSet:
                    return False
                curSet.add(board[row][col])

        # check all cols
        for col in range(9):
            curSet.clear()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in curSet:
                    return False
                curSet.add(board[row][col])

        # check the 3x3 sub-boxes
        subBoxRelCoordinates = ((0, 0), (0, 1), (0, 2),
                                (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
        subBoxStart = ((0, 0), (3, 0), (6, 0), (0, 3),
                       (3, 3), (6, 3), (0, 6), (3, 6), (6, 6))

        for startCoord in subBoxStart:
            curSet.clear()
            for coordinates in subBoxRelCoordinates:
                if board[startCoord[0] + coordinates[0]][startCoord[1] + coordinates[1]] == ".":
                    continue
                if board[startCoord[0] + coordinates[0]][startCoord[1] + coordinates[1]] in curSet:
                    return False
                curSet.add(board[startCoord[0] + coordinates[0]]
                           [startCoord[1] + coordinates[1]])

        return True
