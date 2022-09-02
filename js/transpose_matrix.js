// leetcode problem #867. Transpose Matrix

/*
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
-10^9 <= matrix[i][j] <= 10^9
*/

/*
My solution:
access the matrix in the transposed orientation, and building the new matrix that way.
The outer loop iterates over the horizontal axis of the matrix, while the inner loop iterates over the vertical axis of the matrix
As a result, the first column of the original matrix becomes the first row of the new matrix, the second column becomes the second row, and so on.

Runtime: O(M*N), where M and N are the number of rows and columns of the matrix, respectively. The solution is linear to the size of the matrix.
Space: O(M*N), where M and N are the number of rows and columns of the matrix, respectively. The solution is linear to the size of the matrix.

*/

/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function (matrix) {
    let ans = []
    for (let i = 0; i < matrix[0].length; i++) {
        ans.push([])
        for (let j = 0; j < matrix.length; j++) {
            ans[i].push(matrix[j][i])
        }
    }
    return ans
};


/*
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
*/