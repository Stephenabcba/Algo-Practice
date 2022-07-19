// leetcode problem # 118. Pascal's Triangle

/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
*/

/*
My solution: build the triangle row by row
As each row in the triangle depends on the previous row, building the triangle from the first row down will eventually complete the triangle

Implementation logic:
When the triangle is presented in array form, it looks like the follows:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

The first and last element of each row is always 1
For each element not equal to 1, the value of the element is equal to the sum of the value above and the value to the top left
    - when implementing, it's the previous row's value at index i and index i-1

Runtime: O(M) where M is the number of elements in the triangle
- In terms of the input number of rows N, the number of elements is N * (N + 1) / 2
    - This becomes O(N^2)
Space: O(M) where M is the number of elements in the triangle

*/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
    let triangle = []

    if (numRows > 0) {
        triangle.push([1])
        for (let i = 1; i < numRows; i++) {
            let newRow = []
            for (let j = 0; j < i + 1; j++) {
                if (j == 0 || j == i) {
                    newRow.push(1)
                } else {
                    newRow.push(triangle[triangle.length - 1][j - 1] + triangle[triangle.length - 1][j])
                }
            }
            triangle.push(newRow)
        }
    }

    return triangle
};