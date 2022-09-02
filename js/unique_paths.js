// leetcode problem # 62. Unique Paths

/*
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.


Example 1:
https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
*/

/*
My solution: recursion with memoization

Utilizing recursion, the algorithm explores all possible paths from (0,0) to (m-1,n-1).
- there are only two options at any given square: go right or go down
    - don't explore paths that are out of bounds.

To eliminate unnecessary processing on paths already traveled, a memo is used to keep track of the processed squares
- if a processed square is visited again, the algorithm can take the result from the memo rather than performing the calculations again.

Runtime: O(M*N) where M and N are the number of rows and number of columns of the matrix, resepctively.
Space: O(M*N) where M and N are the number of rows and number of columns of the matrix, resepctively.

Possible improvements:
It is likely that the solution can be written iteratively, working backwards from memo[m-1][n-1] to memo[0][0]
The runtime and space complexity remains the same, but there is no overhead from using recursive functions.
*/

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
    let memo = []
    for (let i = 0; i < m; i++) {
        memo.push([])
        for (let j = 0; j < n; j++) {
            memo[i].push(-1)
        }
    }

    memo[m - 1][n - 1] = 1

    let recurse = (i, j) => {
        if (i >= m || j >= n) {
            return 0
        }
        if (memo[i][j] <= 0) {
            memo[i][j] = recurse(i, j + 1) + recurse(i + 1, j)
        }

        return memo[i][j]
    }

    return recurse(0, 0)
};

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths2 = function (m, n) {
    // iterative solution
    let memo = []
    for (let i = 0; i < m; i++) {
        memo.push([])
        for (let j = 0; j < n; j++) {
            memo[i].push(-1)
        }
    }

    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (i == m - 1 || j == n - 1) {
                memo[i][j] = 1
            } else {
                memo[i][j] = memo[i + 1][j] + memo[i][j + 1]
            }
        }
    }

    return memo[0][0]
};

/*
Fastest JavaScript solution from leetcode submissions: (44ms)
The memo matrix is built using Array.from() function.
*/
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {

    let matrix = Array.from({ length: m }, () => Array.from({ length: n }, () => 0));
    matrix[0][0] = 1;


    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            let currentCell = matrix[i][j]
            if (i < m - 1) {
                matrix[i + 1][j] += currentCell
            }
            if (j < n - 1) {
                matrix[i][j + 1] += currentCell
            }
        }
    }
    return matrix[m - 1][n - 1]
};