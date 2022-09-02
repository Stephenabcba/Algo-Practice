// leetcode problem # 304. Range Sum Query 2D - Immutable

/*
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion.
*/

/*
My solution: brute force calculate the sum every call to sumRegion()
The runtime is O(K * M * N), where M*N is the size of the matrix, and K is the number of calls to sumRegion()

The algorithm is very slow when there are many calls to sumRegion(), and could use some improvements
*/

/**
 * @param {number[][]} matrix
 */
var NumMatrix = function (matrix) {
    this.matrix = matrix
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function (row1, col1, row2, col2) {
    let sum = 0
    for (let i = row1; i <= row2; i++) {
        for (let j = col1; j <= col2; j++) {
            sum += this.matrix[i][j]
        }
    }
    return sum
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */

/*
Example 1:
https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
*/

/*
Solution by leetcoe solutions:
Preprocessing the sum from (0,0) to any coordinate in the matrix.
This way, each sumRegion() call is simply a constant time calculation of manipulating the areas
- The calculation is taking a large rectangle, removing the 2 rectangles to the top and left of the desired rectangle, and then adds the double-counted rectangle back in.
Preprocessing takes O(M*N) time, where M*N is the size of the matrix.

https://leetcode.com/static/images/courses/sum_od.png

https://leetcode.com/static/images/courses/sum_ob.png

https://leetcode.com/static/images/courses/sum_oc.png

https://leetcode.com/static/images/courses/sum_oa.png

Sum(ABCD) = Sum(OD) - Sum(OB) - Sum(OC) + Sum(OA)
*/

/**
 * @param {number[][]} matrix
 */
var NumMatrix = function (matrix) {
    if (matrix.length == 0 || matrix[0].length == 0) return

    this.dp = []
    for (let i = 0; i <= matrix.length; i++) {
        this.dp.push([])
        for (let j = 0; j <= matrix[0].length; j++) {
            this.dp[i].push(0)
        }
    }

    for (let r = 0; r < matrix.length; r++) {
        for (let c = 0; c < matrix[0].length; c++) {
            this.dp[r + 1][c + 1] = this.dp[r + 1][c] + this.dp[r][c + 1] + matrix[r][c] - this.dp[r][c]
        }
    }
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function (row1, col1, row2, col2) {
    // since the class saves all the sums from (0,0), the sum of a rectangle is:
    //           bottom right          -           top right     -          bottom left    +         top left
    return this.dp[row2 + 1][col2 + 1] - this.dp[row1][col2 + 1] - this.dp[row2 + 1][col1] + this.dp[row1][col1]
};
