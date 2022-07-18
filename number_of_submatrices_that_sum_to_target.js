// leetcode problem # 1074. Number of Submatrices That Sum to Target

/*
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.


Example 1:
https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
*/

/*
My solution: check all combinations of (x1,y1,x2,y2)

By calculating the sum from (0,0) to any index (i,j) and storing the result in a matrix, finding the sum of (x1,y1,x2,y2) becomes O(1)

Runtime: O(M^2 * N^2) where M and N are the lengths and widths of the matrix, respectively
Space: O(M*N) where M and N are the lengths and widths of the matrix, respectively

runtime of 954ms (faster than 24.24% of JS submissions) suggests that there's room for improvement
- 
*/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {number}
 */
var numSubmatrixSumTarget = function (matrix, target) {
    let sums = []
    for (let i = 0; i < matrix.length; i++) {
        sums.push([])
        let rowSum = 0
        for (let j = 0; j < matrix[0].length; j++) {
            if (i > 0) {
                sums[i].push(sums[i - 1][j] + rowSum + matrix[i][j])
            } else {
                sums[i].push(rowSum + matrix[i][j])
            }
            rowSum += matrix[i][j]
        }
    }

    let ans = 0

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            for (let k = 0; k <= i; k++) {
                for (let l = 0; l <= j; l++) {
                    if (k == 0) {
                        if (l == 0) {
                            if (sums[i][j] == target) {
                                ans += 1
                            }
                        } else if (sums[i][j] - sums[i][l - 1] == target) {
                            ans += 1
                        }
                    } else if (l == 0) {
                        if (sums[i][j] - sums[k - 1][j] == target) {
                            ans += 1
                        }
                    } else if (sums[i][j] - sums[k - 1][j] - sums[i][l - 1] + sums[k - 1][l - 1] == target) {
                        ans += 1
                    }
                }
            }
        }
    }


    return ans
};

/*
Solution in leetcode discussion by nadaralp (originally written in python)
by processing a dimension as a subarray sum equal to target problem, the runtime can be reduced to O(M^2 * N)
The last dimension is handled using a dictionary
*/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {number}
 */
var numSubmatrixSumTarget = function (matrix, target) {
    let m = matrix.length
    let n = matrix[0].length

    let matrixSums = []
    for (let i = 0; i < m; i++) {
        matrixSums.push([])
        for (let j = 0; j < n; j++) {
            matrixSums[i].push(0)
        }
    }

    for (let row = 0; row < m; row++) {
        for (let col = 0; col < n; col++) {
            if (row == 0 && col == 0) {
                matrixSums[row][col] = matrix[row][col]
            } else if (row == 0) {
                matrixSums[row][col] = matrix[row][col] + matrixSums[row][col - 1]
            } else if (col == 0) {
                matrixSums[row][col] = matrix[row][col] + matrixSums[row - 1][col]
            } else {
                matrixSums[row][col] = matrix[row][col] + matrixSums[row][col - 1] + matrixSums[row - 1][col] - matrixSums[row - 1][col - 1]
            }
        }
    }

    let ans = 0

    for (let y1 = 0; y1 < m; y1++) {
        for (let y2 = y1; y2 < m; y2++) {
            let subarraySums = {}
            subarraySums[0] = 1

            for (let x = 0; x < n; x++) {
                let matrixSum = matrixSums[y2][x]

                if (y1 > 0) {
                    matrixSum -= matrixSums[y1 - 1][x]
                }

                if (subarraySums.hasOwnProperty(matrixSum - target)) {
                    ans += subarraySums[matrixSum - target]
                }

                if (!subarraySums.hasOwnProperty(matrixSum)) {
                    subarraySums[matrixSum] = 0
                }

                subarraySums[matrixSum] += 1
            }
        }
    }

    return ans
};