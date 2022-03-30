// leetcode problem #74. Search a 2D Matrix

/*
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
*/

/*
My Solution: binary search on the rows and then binary search within the row
- idea: 
binary search for the target based on the first value of each row
    - the row is found when target is larger than the first value of the row, and smaller than the first value of the row after
binary search within the row 

runtime: O(logN + logM)

Possible Improvements: "connect" the rows and perform a binary search for the one "connected" array
- start is 0 (matrix[0][0])
- end is M * N - 1 (matrix[M-1][N-1])
- accessing the actual mid value is matrix[Math.floor(mid/N)][mid%N]
*/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
    let matStart = 0
    let matEnd = matrix.length - 1
    while (matStart < matEnd) {
        let matMid = Math.floor((matStart + matEnd) / 2)
        if (matrix[matMid][0] === target) {
            return true
        } else if (matrix[matMid][0] < target) {
            matStart = matMid
            if (matMid === matrix.length - 1) {
                matEnd = matMid
                break
            } else if (matStart === matEnd - 1) {
                if (matrix[matEnd][0] > target) {
                    matEnd = matStart
                } else {
                    matStart = matEnd
                }
            }
        } else { // (matrix[matMid][0] > target)
            if (matMid === 0) {
                return false
            } else {
                matEnd = matMid - 1
            }
        }
    }

    if (matStart != matEnd) {
        console.log("problem");
    }
    const curRow = matrix[matStart]
    let rowStart = 0
    let rowEnd = matrix[matStart].length - 1
    while (rowStart <= rowEnd) {
        const rowMid = Math.floor((rowStart + rowEnd) / 2)
        if (curRow[rowMid] === target) {
            return true
        } else if (curRow[rowMid] < target) {
            rowStart = rowMid + 1
        } else { // (curRow[rowMid] > target)
            rowEnd = rowMid - 1
        }
    }
    return false
};

const matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
const target = 3
const target2 = 13

console.log(searchMatrix(matrix, target));
console.log(searchMatrix(matrix, target2));