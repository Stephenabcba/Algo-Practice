// leetcode problem #1091. Shortest Path in Binary Matrix

/*
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
*/

/*
My Solution: Adapting BFS for shortest path
Started from copying the BFS algorithm from wikipedia
Makes use of BFS's ability to find shortest paths for unweighted, undirected graphs

Main modifications:
- In BFS's iterations, don't process the nodes that have a value of 1 in the grid, as those are not valid paths
- The visited matrix is holding the node's distance from the start (following clear paths) instead of just booleans
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function (grid) {
    let n = grid.length

    // initialize the visited array
    const visited = []
    for (let i = 0; i < n; i++) {
        visited.push([])
        for (let j = 0; j < n; j++) {
            visited[i].push(0)
        }
    }

    // initialize the queue
    const queue = []

    // initialize the directions array (there are 8 directions in total)
    const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    // set the starting node of (0,0)
    visited[0][0] = 1
    let curQueuePos = 0
    queue.push([0, 0])

    // BFS main logic
    while (curQueuePos < queue.length) {
        // dequeue a node from the queue
        let vertex = queue[curQueuePos]
        curQueuePos++

        // only process the node if it is a "clear path"
        if (grid[vertex[0]][vertex[1]] == 0) {
            // the node is at the bottom right of the grid, return the number of nodes visited
            if (vertex[0] == n - 1 && vertex[1] == n - 1) {
                return visited[n - 1][n - 1]
            }

            // check all 8 directions for unvisited nodes and add them to the queue
            for (let direction of directions) {
                let y = vertex[0] + direction[0]
                let x = vertex[1] + direction[1]

                if (y >= 0 && y < n && x >= 0 && x < n) { // skip out of bounds indexes
                    if (visited[y][x] == 0) { // checking for unvisited nodes
                        visited[y][x] = visited[vertex[0]][vertex[1]] + 1 // the shortest path from the current node to the start is the previous node's path + 1 more edge
                        queue.push([y, x])
                    }
                }
            }
        }
    }

    // the bottom right node is unreachable, return -1
    return -1
};


/*
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
*/