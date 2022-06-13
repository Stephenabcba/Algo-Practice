// leetcode problem # 120. Triangle

/*
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4
*/

/*
My solution: find the minimum sum from to the top of the triangle to the bottom
- at any position (i,j) in the triangle, the minimum sum is triangle[i][j] + (minimum sum of triangle[i-1][j-1] OR minimum sum of triangle[i-1][j]) (if they exist)

by building the minimum sum for every value in the triangle from the top row to the bottom row, the minimum sum of the triangle is the minimum of the value in the last row.

Time: O(N^2) where N is the number of rows in the triangle
Space: O(N^2) where N is the numer of rows in the triangle

The performance (faster than 14.34% and less memory then 27.59%) suggests that there are better solutions.
Runtime: 119ms
Memory: 44.2MB
*/

/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
    if (triangle.length == 1) {
        return triangle[0][0]
    }

    let dp = []

    dp.push([triangle[0][0]])
    let smallestSum = Infinity
    for (let i = 1; i < triangle.length; i++) {
        dp.push([])
        // at any row i, there are i + 1 values.
        for (let j = 0; j <= i; j++) {
            // at any position (i,j) in the triangle, the minimum sum is triangle[i][j] + (minimum sum of triangle[i-1][j-1] OR minimum sum of triangle[i-1][j]) (if they exist)
            let smaller = 0
            if (j == 0) {
                smaller = dp[i - 1][j]
            } else {
                smaller = dp[i - 1][j - 1]

                if (j < i && dp[i - 1][j] < smaller) {
                    smaller = dp[i - 1][j]
                }
            }

            smaller += triangle[i][j]

            dp[i].push(smaller)

            // find the smallest sum in the final row
            if (i == triangle.length - 1) {
                if (smaller < smallestSum) {
                    smallestSum = smaller
                }
            }
        }
    }

    return smallestSum
};

/*
Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above). ** underlines not supported in js files

Example 2:
Input: triangle = [[-10]]
Output: -10
*/

/*
Sample 48ms submission in leetcode records (top runtime submission)
The solution works bottom up, iterating for the sum from the second last row to the first row

observations:
- it is not necessary to retain the sum of every row in the triangle; only the previous row is needed
    - (the row above if top down, the row below if bottom up)
- by working bottom up, min-searching logic in the bottom row is not required (the last part in my solution), as the top of the triangle only has 1 value.
- by working bottom up, overwriting the dp array does not lose information needed in later iterations
    - do not need to save information in temporary variables
        - temp vars would be needed if top-down approach was used in a O(N) space approach

Runtime: O(N^2) where N is the number of rows in the triangle. All values are still visited once except the bottom row
Space: O(N) where N is the number or rows in the triangle (the actual space used is the size of bottom row in the triangle)
*/

/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
    const n = triangle.length;
    const minPath = triangle[n - 1];
    for (let row = n - 2; row >= 0; row--) {
        for (let i = 0; i <= row; i++) {
            minPath[i] = Math.min(minPath[i], minPath[i + 1]) + triangle[row][i];
        }
    }

    return minPath[0];
};