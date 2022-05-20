// leetcode problem #329. Longest Increasing Path in a Matrix

/*
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 


 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^(31 - 1)
*/

/*
My solution: modified dfs
Modification 1: an edge only exists out of the 4 directions if the value in the matrix at that direction is higher than that of the current location
Modification 2: Instead of just keeping track of whether a node has been visited, keep track of the longest chain of nodes that the node is connected to, or -1 if it hasn't been visited
    - when a neighboring node has already been visited, the current node will connect to the chain if doing so creates a longer chain
        - when a neighboring node has not been visited, perform a dfs on it first
        - due to the characteristics of dfs, the length of the chain of neighboring nodes at the time of comparison 

With these modifications done, some observations can be made:
1. the dfs forms a chain of nodes in increasing values
2. only nodes that are start of a recursion cycle can be the starting node in the chain
    - these nodes are not necessarily the start of chains, but they are the only candidates that could be the start of the longest chains

To ensure that all nodes have been visited, iterate through all of the matrix and perform dfs on unvisited nodes

From observation 2, only nodes that initiated dfs can be candidates for the longest chain
- find the largest chain out of the nodes that initiated dfs

*/

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function (matrix) {
    const visited = []
    for (let i = 0; i < matrix.length; i++) {
        visited.push([])
        for (let j = 0; j < matrix[0].length; j++) {
            visited[i].push(-1)
        }
    }
    const directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    const dfs = (y, x) => {

        if (visited[y][x] < 0) {
            visited[y][x] = 1
        }
        for (let direction of directions) {
            let mody = y + direction[0]
            let modx = x + direction[1]
            // make sure the coordinate is within bounds
            if (mody >= 0 && mody < matrix.length && modx >= 0 && modx < matrix[0].length) {
                // only consider edges that lead to larger values in the matrix
                if (matrix[mody][modx] > matrix[y][x]) {
                    if (visited[mody][modx] < 0) {
                        dfs(mody, modx)
                    }
                    if (visited[mody][modx] >= visited[y][x]) { // if the edge leads to a longer chain of nodes, save that length instead
                        visited[y][x] = visited[mody][modx] + 1
                    }
                }
            }
        }
        return visited[y][x]
    }
    let max = 0
    // to ensure that every node has been visited, iterate through all the nodes in the matrix
    // and perform dfs on the node if it hasn't been visited after previous recursive calls.
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (visited[i][j] < 0) {
                // these nodes that start the dfs recursion are the only candidates for the start of the longest chain
                let maxCandidate = dfs(i, j)
                if (maxCandidate > max) {
                    max = maxCandidate
                }
            }
        }
    }
    return max
};

/*
Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
*/