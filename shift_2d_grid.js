// leetcode problem # 1260. Shift 2D Grid

/*
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
*/


/*
My solution: 
copy the values to a new grid
a grid can be "flattened" to an array with length M*N
for any index i, its value after rotation should be ((i + M*N - k) % M*N)
the grid and the array have a 1:1 mapping, where array[i] = grid[Math.floor(i / numCols)][i%numCols]
*/
/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function (grid, k) {
    const fullLength = grid.length * grid[0].length
    const numRows = grid.length
    const numCols = grid[0].length
    const newGrid = []
    k = k % (fullLength)
    for (let i = 0; i < numRows; i++) {
        newGrid.push([])
    }
    for (let i = 0; i < fullLength; i++) {
        newGrid[Math.floor(i / numCols)].push(grid[Math.floor(((i + fullLength - k) % fullLength) / numCols)][((i + fullLength - k) % fullLength) % numCols])
    }
    return newGrid
};




/*
In-place solution in leetcode discussion by zayne-siew (originally in Python)
Idea: "swap" the values to their correct places
sometimes, k could form a cycle where the chain of swaps are complete before the operation is done
simply move to the next element and swap again
this way, only O(1) extra space is required
*/

var shiftGrid2 = function (grid, k) {
    const fullLength = grid.length * grid[0].length
    const numRows = grid.length
    const numCols = grid[0].length
    k = k % (fullLength)
    if (k == 0) {
        return grid
    }
    let count = 0
    let i = 0
    while (count < fullLength) {
        let curRow = Math.floor(i / numCols)
        let curCol = i % numCols
        let nextVal = grid[curRow][curCol]
        let nextIndex = (i + k) % fullLength
        while (true) {
            curRow = Math.floor(nextIndex / numCols)
            curCol = nextIndex % numCols
            let temp = nextVal
            nextVal = grid[curRow][curCol]
            grid[curRow][curCol] = temp
            count++
            if (nextIndex == i) {
                break
            }
            nextIndex = (nextIndex + k) % fullLength
        }
        i++
    }
    return grid
};

/*
Example 1: 
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1 
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2: 
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4 
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
*/

const grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 1
// const grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k = 4
// const grid = [[1]], k = 5
console.log(shiftGrid2(grid, k))