// leetcode problem #1337. The K Weakest Rows in a Matrix
/*
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
*/

/*
My solution:
Idea:
- Find the number of soldiers in each row
- Store the number in a dictionary, with the number as the key and an array of indexes with the number as the value
- add the rows to the answer starting from the weakest (lowest number of soldiers and lowest index)
*/

/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function (mat, k) {
    const soldierCount = {}
    for (let i = 0; i < mat.length; i++) {
        const row = mat[i]
        let count = 0
        for (let j = 0; j < row.length; j++) {
            const col = row[j]
            if (col === 0 || j === row.length - 1) {
                if (col === 1) {
                    count++
                }
                if (!soldierCount.hasOwnProperty(count)) {
                    soldierCount[count] = []
                }
                soldierCount[count].push(i)
                break
            }
            count++
        }
    }
    let ans = []
    let added = 0
    let curSold = 0
    let arrayIdx = 0
    console.log(soldierCount);
    while (added < k) {
        if (!soldierCount.hasOwnProperty(curSold)) {
            curSold++
            continue
        }
        const curRow = soldierCount[curSold]
        if (arrayIdx < curRow.length) {
            ans.push(curRow[arrayIdx])
            arrayIdx++
            added++
        } else {
            curSold++
            arrayIdx = 0
            continue
        }
    }
    return ans
};

const mat =
    [[1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]]

const k = 3

const mat2 =
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]

console.log(kWeakestRows(mat, k));
console.log(kWeakestRows(mat2, 1));

/*
Solution from Leetcode discussion:
- Sum up each row
    - the sum is the number of soldiers for the row
    - store the sum in an array, where each item in the array is a tuple/array
        - first part is the number of soldiers, second part is the index of the row in the matrix
- sort the array based on the number of soldiers
- the first k indexes in the array are the weakest rows
*/