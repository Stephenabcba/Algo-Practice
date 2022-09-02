// leetcode problem # 63. Unique Paths II

/*
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
*/

/*
My solution: DFS / dynamic programming
The grid is processed as a graph with directed edges going right or down.
At any given grid location, the number of ways to reach the target is fixed
    - independent of whether the path came from the top or the left
    - gives oppurtunity to use dynamic programming, reducing unnecessary recursion.
Utilize dfs recursion logic to traverse through the entire grid.
When initializing the visited matrix:
    - the target square is initialized as 1, as any path that reaches this square is a valid path
    - any square with an obstacle (value of 1 in obstacleGrid) is initialized to 0, as it is impossible to reach the target on an obstacle
    - all other squares are initialized to -1, and will be updated by DFS
DFS is only recursing if the square has not been visited
The value of each unvisited square in the visited matrix will be populated by the sum of available paths to the right and bottom of the square
    - perform dfs first if those 2 squares has not been visited
*/

/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function (obstacleGrid) {
    const m = obstacleGrid.length
    const n = obstacleGrid[0].length

    const visited = []
    for (let i = 0; i < m; i++) {
        visited.push([])
        for (let j = 0; j < n; j++) {
            if (obstacleGrid[i][j] == 1) {
                visited[i].push(0)
            } else {
                visited[i].push(-1)
            }
        }
    }
    visited[m - 1][n - 1] = 1

    const dfs = (x, y) => {
        // out of bounds edge case handling, left and top edge not required.
        if (x < 0 || x >= n || y < 0 || y >= m) {
            return 0
        }
        if (visited[y][x] < 0) {
            visited[y][x] = dfs(x + 1, y) + dfs(x, y + 1)
        }
        return visited[y][x]
    }
    return dfs(0, 0)
};

/*
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg
Output: 1
*/