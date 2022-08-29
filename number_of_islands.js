// leetcode problem # 200. Number of Islands

/*
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
*/

/*
My solution: Recursive Traversal with visited matrix

Using recursive traversal, the algorithm can attempt to travel on all four sides to explore the island until it is out of bounds or reaches water.
Using a visited matrix, the algorithm will skip all cells that are already processed
Base Cases: 
1. coordinate is out of bounds or cell is already visited
2. the current coordinate is in water
    - in this case, the algorithm will mark the coordinate as visited first, and then break recursion.

Recursive Case:
The coordinate is unvisited land
-> mark coordinate as visited then attempt to travel to all four sides

With recursive traversal, the program will fully explore every island before moving on.
Using a nested loop traversing over the entire matrix, every time an unvisited land is encountered, a new island is discovered
-> increment the number of islands
-> call the recursive traversal program on the new island

Runtime: O(M * N) where M is the width of the array and N is the length of the array
Space: O(M * N) where M is the width of the array and N is the length of the array
*/

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
    const height = grid.length
    const width = grid[0].length
    let visited = new Array(height)

    for (let i = 0; i < height; i++) {
        visited[i] = new Array(width).fill(false)
    }

    let islands = 0

    let traverse = (i, j) => {
        // index out of bounds or cell already visited; do not need to process
        if (i < 0 || i >= height || j < 0 || j >= width || visited[i][j]) {
            return 0
        }

        visited[i][j] = true

        // if the cell is in the water, the island cannot extend this way
        if (grid[i][j] == "0") {
            return 0
        }

        // if the cell is land, attempt to traverse to all four sides
        traverse(i + 1, j)
        traverse(i - 1, j)
        traverse(i, j + 1)
        traverse(i, j - 1)
        return 0
    }


    for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
            if (!visited[i][j]) {
                if (grid[i][j] == "0") {
                    visited[i][j] = true
                } else {
                    traverse(i, j)
                    islands += 1
                }
            }
        }
    }

    return islands
};

let test1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
let test2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

console.log("Test 1: " + numIslands(test1))
console.log("Test 2: " + numIslands(test2))