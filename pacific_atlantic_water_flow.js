// leetcode problem # 417. Pacific Atlantic Water Flow

/*
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:
https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
*/

/*
My solution: Work backwards from the ocean

Idea: Find where the ocean can "climb" up parts of the island
1. Starting from the ocean, the neighboring block is "climbable" if the neighboring block has height >= current block
2. Mark the block as "reachable by ocean X" if there is a path for ocean X to "climb" up to the block
- It is inconclusive which way the water will flow in the normal direction if 2 neighboring platforms have the same height
- However, if working from lower elevation up, it is conclusive whether 2 neighboring platforms with the same height is reachable from the ocean
    - if one block is reachable from the ocean, the neighboring block with the same height is definitely reachable from the ocean.

a "reachable" matrix is created for each ocean to keep track of the blocks that has a path into each ocean

The paths are found using the DFS logic, using recursion
Base Cases:
1. if the block is out of bounds, or it is lower than the previous block, stop traversing
2. if the block is reachable and it is not an ocean-side block, stop traversing
Recursive Case:
The block is reachable from the ocean, and it has not been traversed before
-> check if any of the 4 neighboring sides can also be reached from the ocean

The logic is done twice, once for Pacific Ocean and once for Atlantic Ocean

At the end, if any block can reach both Pacific and Atlantic Ocean, add it to the answer list.
- this can be done by iterating through every block and checking

Runtime: O(M * N) where M and N are the lengths and widths of the matrix, respectively (M x N matrix)
Space: O(M * N) where M and N are the lengths and widths of the matrix, respectively (M x N matrix)
*/

/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
    let rows = heights.length
    let cols = heights[0].length
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    let pacificFlow = []
    let atlanticFlow = []

    for (let i = 0; i < rows; i++) {
        pacificFlow.push(new Array(heights[0].length).fill(0))
        atlanticFlow.push(new Array(heights[0].length).fill(0))
    }

    for (let i = 0; i < rows; i++) {
        pacificFlow[i][0] = 1
        atlanticFlow[i][cols - 1] = 1
    }

    for (let j = 0; j < cols; j++) {
        pacificFlow[0][j] = 1
        atlanticFlow[rows - 1][j] = 1
    }

    // let the water "climb" up to available locations
    let waterfall = (i, j, ocean, prevI = i, prevJ = j) => {
        // if the block is out of bounds, or it is lower than the previous block, stop traversing
        if (i < 0 || i >= rows || j < 0 || j >= cols || heights[prevI][prevJ] > heights[i][j]) {
            return
        }

        // if the block has been traversed and it is not an ocean-side block, stop traversing
        if (!(i == prevI && j == prevJ) && ocean[i][j] != 0) {
            return
        }

        // the current block is higher than the previous block; it can reach the ocean
        ocean[i][j] = 1

        // check if any block on any sides can also reach the ocean
        for (let direction of directions) {
            let newI = i + direction[0]
            let newJ = j + direction[1]
            waterfall(newI, newJ, ocean, i, j)
        }
    }

    for (i = 0; i < rows; i++) {
        waterfall(i, 0, pacificFlow)
        waterfall(i, cols - 1, atlanticFlow)
    }
    for (let j = 0; j < cols; j++) {
        waterfall(0, j, pacificFlow)
        waterfall(rows - 1, j, atlanticFlow)
    }
    let ans = []
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (pacificFlow[i][j] == 1 && atlanticFlow[i][j] == 1) {
                ans.push([i, j])
            }
        }
    }

    return ans
};