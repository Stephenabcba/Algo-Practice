// leetcode problem # 48. Rotate Image

/*
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Example 1:
https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
*/

/*
My solution: Swap 4 elements at a time

As additional matrices cannot be used, swaps need to be done in a cycle where only one temp variable is needed.

Observation: 
The four corners moved clockwise by 90 degrees, but did not swap values with non-corner values
- the rest of the matrix follows the same pattern

The outer loop runs N / 2 times while the inner loop runs N - 1 - i times
- this rotates the matrix by the correct amount
- if more iterations are done, the matrix would be over-rotated

The correct indexing was found by testing against given cases

original corners  sides
1 2 3    7 2 1    7 4 1
4 5 6 -> 4 5 6 -> 8 5 2
7 8 9    9 8 3    9 6 3

Runtime: O(N^2) where N is the side length of the matrix (N x N matrix)
Space: O(1), memory usage does not scale with input size.
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
    let prev = 0
    let n = matrix.length - 1
    for (let i = 0; i < matrix.length / 2; i++) {
        for (let j = i; j < n - i; j++) {
            prev = matrix[i][j]
            matrix[i][j] = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = prev
        }
    }
};