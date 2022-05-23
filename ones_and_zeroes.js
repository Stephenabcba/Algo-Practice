// leetcode problem #474. Ones and Zeroes

/*
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
*/

/*
My attempt: sorting the array
problem: unable to determine which string to remove from the subset
*/

/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxFormAttempt = function (strs, m, n) {
    const zeros = []
    for (let str of strs) {
        let zeroCount = 0
        let oneCount = 0
        for (let digit of str) {
            if (digit == "0") {
                zeroCount++
            } else if (digit == "1") {
                oneCount++
            }
        }
        zeros.push([zeroCount, oneCount, false])
    }
    const ones = [...zeros]
    zeros.sort((a, b) => a[0] - b[0])
    ones.sort((a, b) => a[1] - b[1])

    let zeroIndex = 0
    let ans = 0
    let zeroSum = 0
    let oneSum = 0
    while (zeroIndex < zeros.length) {
        if (zeroSum + zeros[zeroIndex][0] <= m && oneSum + zeros[zeroIndex][1] <= n) {
            zeroSum += zeros[zeroIndex][0]
            oneSum += zeros[zeroIndex][1]
            zeros[zeroIndex][2] = true
            ans++
        } else {
            break
        }
        zeroIndex++
    }
    zeroIndex--


    let oneIndex = 0
    let prevIndex = -1
    while (oneIndex < ones.length) {
        if (ones[oneIndex][2] == false) {
            if (zeroSum + ones[oneIndex][0] <= m && oneSum + ones[oneIndex][1] <= n) {
                zeroSum += ones[oneIndex][0]
                oneSum += ones[oneIndex][1]
                ones[oneIndex][2] = true
                ans++
            } else {
                if (prevIndex < 0) {
                    prevIndex = oneIndex
                } else {
                    if (zeroIndex >= 0) {
                        while (zeroIndex >= 0 && zeros[zeroIndex][2] == false) {
                            zeroIndex--
                        }
                        if (zeroIndex >= 0 && ((zeroSum - zeros[zeroIndex][0] + ones[prevIndex][0] + ones[oneIndex][0]) <= m && (oneSum - zeros[zeroIndex][1] + ones[prevIndex][1] + ones[oneIndex][1]) <= n)) {
                            zeros[zeroIndex][2] = false
                            ones[prevIndex][2] = true
                            ones[oneIndex][2] = true
                            zeroSum += -zeros[zeroIndex][0] + ones[prevIndex][0] + ones[oneIndex][0]
                            oneSum += -zeros[zeroIndex][1] + ones[prevIndex][1] + ones[oneIndex][1]
                            zeroIndex--
                            prevIndex = -1
                            ans++
                        } else {
                            break
                        }
                    }
                }
            }
        }
        oneIndex++
    }

    return ans
};

/*
Solution in leetcode discussion by Nimesh-Srivastava (originally written in C++)
The solution uses a dynamic programming matrix
    - the rows are the number of 0's
    - the columns are the number of 1's
    - the dp matrix keeps track of the maximum count of strings that have 0's and 1's within the given index
        - dp[i][j] holds the maximum number of strings that has the count(zeros in all the strings in subset) <= i AND count(ones in all the strings in subset) <= j

iterate through all the strings and the update the dp matrix
    - count the number of 0's and 1's in the string, save as variables zeros and ones
    - iterate through the dp matrix where i >= the count of 0's AND j >= the count of 1's
        - it is impossible for the string to be in a subset with sum of 0's and 1's less than the single string
        - update the cell with position (i,j) if dp[i - zeros][j - ones] + 1 is larger than the current value 
            - the cell dp[i - zeros][j - ones] holds the count of strings that had a total of i - zeros 0's and j - ones 1's, and the current string is the + 1
        - iterate from the bottom right to the top left to update the values properly
            - each cell depends on values of cells to the top left of it

After all the strings have been processed, the value of cell dp[m][n] holds the final answer
*/

/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function (strs, m, n) {
    // initialize the dp matrix
    const dp = []
    for (let i = 0; i <= m; i++) {
        dp.push([])
        for (let j = 0; j <= n; j++) {
            dp[i].push(0)
        }
    }

    // process every string
    for (let s of strs) {
        // find the cound of 0's and 1's within the string
        let zeros = 0
        for (let digit of s) {
            if (digit == "0") {
                zeros++
            }
        }
        let ones = s.length - zeros

        // update the dp matrix
        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], 1 + dp[i - zeros][j - ones])
            }
        }
    }
    return dp[m][n]
};

/*
Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

*/