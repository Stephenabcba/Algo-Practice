// leetcode problem #59. Spiral Matrix II

/*
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Constraints:
1 <= n <= 20
*/

/*
for n = 2, the matrix looks like:
1 2
4 3

for n = 4, the matrix looks like:
1  2  3  4
12 13 14 5
11 16 15 6
10 9  8  7
*/

/*
My solution: fill with a direction variable
observation: the number of values required to fill a row/column follows this given pattern:
n, n-1, n-1, n-2, n-2 ..., 2, 2, 1, 1
* except for the top row, the number of values required decreases every 2 changes in direction


implementation:
a direction variable is used to dictate how the fill index changes
direction 0 is left to right
direciton 1 is top to bottom
direction 2 is right to left
direction 3 is bottom to top

Runtime: O(N^2), the logic runs from 1 to N^2
Space: O(N^2) for the actual matrix, and O(1) extra space for the various variables

readability improvement:
the if-else-if block for direction could be replaced with an increment array:
const directionArr = [[1,0], [0,1], [-1,0], [0,-1]]
and every iteration, simply do:
x += direcitonArr[direction][0]
y += direcitonArr[direction][1]
*/

/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function (n) {
    // initialize the matrix and populate the top row
    const matrix = []
    for (let i = 0; i < n; i++) {
        matrix.push(new Array(n))
        matrix[0][i] = i + 1
    }

    let curNum = n + 1 // the value to fill into the matrix
    let direction = 1
    let x = n - 1 // horizontal deviation from index 0,0
    let y = 0 // vertical deviation from index 0,0
    let fillCount = n - 1
    while (curNum <= n * n) {
        for (let i = 0; i < 2; i++) { // the number of values to fill decreases every 2 iterations
            for (let j = 0; j < fillCount; j++) { // fills an entire row / column
                if (direction == 0) { // go right
                    x++
                } else if (direction == 1) { // go down
                    y++
                } else if (direction == 2) { // go left
                    x--
                } else if (direction == 3) { // go up
                    y--
                }
                matrix[y][x] = curNum
                curNum++
            }
            direction = (direction + 1) % 4 // direction change follows the pattern of: right, down, left, up, and repeats every 4 iterations
        }
        fillCount--
    }
    return matrix
};

const n = 5
console.log(generateMatrix(n))

/*
Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
*/