// leetcode problem # 695. Max Area of Island

/*
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Example 1:
https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
*/

/*
My solution: DFS
Solution created after seeing related topics of Depth-First Search on leetcode

Idea:
Attempt to find the entire area of an island when new land is discovered.
- if the current cell is water, it cannot be part of land
- to prevent double counting and visiting the island more than once, keep track of which cells are already visited
    - can be done with a m x n matrix
Keep track of the area of the largest island found so far
- if a new island is larger, update the largest area variable.

Runtime: O(M * N), where M and N are the dimensions of the grid
- the visited grid ensures that even though the recursive function is iterated M*N times, an island will never be processed twice
Space: O(M * N), where M and N are the dimensions of the grid

*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
    // create a boolean matrix to keep track of which cells are already visited.
    let visited = []
    for (let i = 0; i < grid.length; i++) {
        visited.push([])
        for (let j = 0; j < grid[0].length; j++) {
            visited[i].push(false)
        }
    }

    let max = 0

    // main DFS traversal logic
    let traverse = (i, j) => {
        // don't pursue the path if the index is out of bounds, or the cell is already visited.
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || visited[i][j]) {
            return 0
        }
        // if the cell is in bounds and not visited, set it to visited
        visited[i][j] = true

        // if the current cell is not land, then it can't be a part of an island
        if (grid[i][j] === 0) {
            return 0
        }

        // the current cell is part of an unvisited island, try to find the area of the island.
        return 1 + traverse(i - 1, j) + traverse(i + 1, j) + traverse(i, j - 1) + traverse(i, j + 1)
    }

    // try to start DFS on every cell, to ensure that the traversal did not wall itself off when starting at a given point
    // any visited cell will immediately return.
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (!visited[i][j]) {
                let area = traverse(i, j)
                max = Math.max(max, area)
            }
        }
    }

    return max
};