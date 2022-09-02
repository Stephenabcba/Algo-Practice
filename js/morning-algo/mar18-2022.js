/* 
  Given a square matrix (2d array) of integers
  Calculate the absolute difference between the sums of its diagonals
    - top left to bottom right diagonal
    - top right to bottom left diagonal
*/

const squareMatrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9],
];
const expected1 = 2;
/* 
  left to right diagonal: 1 + 5 + 9 = 15
  right to left diagonal: 3 + 5 + 9 = 17
  absolute difference = 2
*/

const squareMatrix2 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
];
const expected2 = 0;
/* 
  left to right diagonal: 1 + 2 + 3 + 4 + 5 = 15
  right to left diagonal: 5 + 4 + 3 + 2 + 1 = 15
  absolute difference = 0
*/

const squareMatrix3 = [
    [1, 2],
    [3, 4]
]

const squareMatrix4 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]


/*
create a function that takes in a square matrix (nxn) and returns a number
find the sum of each diagonal
    - iterate through the outer array
        - the index of each number is 1 larger or 1 smaller than the previous
find the difference of the two sums
return the absolute value of the difference
*/
function diagonalDifference(sqrMatrix) {
    let diagonalSum1 = 0
    let diagonalSum2 = 0
    const matrixLength = sqrMatrix.length
    for (let i = 0; i < matrixLength; i++) {
        diagonalSum1 += sqrMatrix[i][i]
        diagonalSum2 += sqrMatrix[i][sqrMatrix.length - 1 - i]
    }
    // return Math.abs(diagonalSum1 - diagonalSum2)
    let diagonalDiff = diagonalSum1 - diagonalSum2;
    return (diagonalDiff >= 0) ? diagonalDiff : - diagonalDiff
}

console.log(diagonalDifference(squareMatrix1));
console.log(diagonalDifference(squareMatrix2));
console.log(diagonalDifference(squareMatrix3));
console.log(diagonalDifference(squareMatrix4));