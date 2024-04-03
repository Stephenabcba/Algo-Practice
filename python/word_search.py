# leetcode problem # 79. Word Search

"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
https://assets.leetcode.com/uploads/2020/11/04/word2.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
https://assets.leetcode.com/uploads/2020/10/15/word3.jpg
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

"""
My solution: Recursion

Using recursion, the program can traverse the board to check whether the word exists.

Replace each used letter with an empty space, and change the letter back when
recursion is complete

Runtime: O(M*N*W) where M and N are the rows and columns of board, respectively, and W is length of word
Space: O(W)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(row, col, idx):
            if idx == len(word) - 1:
                return True
            if row - 1 >= 0 and board[row - 1][col] == word[idx + 1]:
                board[row - 1][col], temp = "", board[row - 1][col]
                if traverse(row - 1, col, idx + 1):
                    return True
                board[row - 1][col] = temp
            if col - 1 >= 0 and board[row][col - 1] == word[idx + 1]:
                board[row][col - 1], temp = "", board[row][col - 1]
                if traverse(row, col - 1, idx + 1):
                    return True
                board[row][col - 1] = temp
            if row + 1 < len(board) and board[row + 1][col] == word[idx + 1]:
                board[row + 1][col], temp = "", board[row + 1][col]
                if traverse(row + 1, col, idx + 1):
                    return True
                board[row + 1][col] = temp
            if col + 1 < len(board[0]) and board[row][col + 1] == word[idx + 1]:
                board[row][col + 1], temp = "", board[row][col + 1]
                if traverse(row, col + 1, idx + 1):
                    return True
                board[row][col + 1] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    board[row][col], temp = "", board[row][col]
                    if traverse(row, col, 0):
                        return True
                    board[row][col] = temp

        return False
