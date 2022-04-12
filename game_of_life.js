// leetcode problem #289. Game of Life
/*
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
*/


/*
My solution: intermediate state
- get the number of live cells around any given cell of the old state
- modify the state of the current cell
    - in order to make the modification in place, this solution passes through the entire board twice
        - the first pass introduces an intermedite state to correctly evaluate the state of all cells
    - a cell that was alive in the old state but will die in the new state has a value of 0.75
        - 0.75 is rounded to 1 when processing the new state for the surrounding cells
    - a cell that was dead in the old state but will be alive in the new state has value of 0.25
        - 0.25 is rounded to 0 when processing the new state for the surroudning cells
    - in all other cases, the cells keep their values
- in the second pass, convert the intermediate state to the actual new state
    - cells with value of 0.75 becomes 0
    - cells with value of 0.25 becomes 1

Major challenge in the problem:
- correctly handling the edge cases for getting the number of alive cells
- modifying the board in-place
    - required the use of intermediate state

Runtime: O(N*M), where N is number of rows and M is number of columns
Space: O(1), the only extra variable is the score variable, which is just an integer
*/
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            let score = 0
            if (i - 1 >= 0) { // row above exists
                if (j - 1 >= 0) { // top left
                    score += Math.round(board[i - 1][j - 1])
                }
                if (j + 1 < board[i].length) { // top right
                    score += Math.round(board[i - 1][j + 1])
                }
                score += Math.round(board[i - 1][j]) // directly above
            }
            if (j - 1 >= 0) { // left side exists
                score += Math.round(board[i][j - 1])
            }
            if (j + 1 < board[i].length) { // right side exists
                score += Math.round(board[i][j + 1])
            }
            if (i + 1 < board.length) { // row below exists
                if (j - 1 >= 0) { // bottom left
                    score += Math.round(board[i + 1][j - 1])
                }
                if (j + 1 < board[i].length) { // bottom right
                    score += Math.round(board[i + 1][j + 1])
                }
                score += Math.round(board[i + 1][j]) // directly below
            }

            if (board[i][j] == 1) { // cell was alive
                if (score < 2 || score > 3) {
                    board[i][j] = 0.75 // cell will die
                }
            } else { // cell was dead
                if (score == 3) {
                    board[i][j] = 0.25 // cell will become alive
                }
            }
        }
    }
    // find the actual new state
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
            if (board[i][j] == 0.75) {
                board[i][j] = 0
            } else if (board[i][j] == 0.25) {
                board[i][j] = 1
            }
        }
    }
};

/*
Example 1: 
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] 
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]] 

Example 2: 
Input: board = [[1,1],[1,0]] 
Output: [[1,1],[1,1]]
*/

const board = [[1, 1], [1, 0]]
gameOfLife(board)
console.log(board)