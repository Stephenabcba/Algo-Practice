// leetcode problem #216. Combination Sum III

/*
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Constraints:
2 <= k <= 9
1 <= n <= 60
*/

/*
My Solution:
recursively search for the solution space
a set of numbers is a solution if it has k values and sums up to n -> add to solution
    - if a set of numbers has k values but does not sum up to n, the set is invalid
    - if a set of numbers has sum higher than n, the set is invalid

if the set is currently empty, check all values from 1 to 9 for the first value in the set
if the set is not empty, check values 1 + last value in set to 9 as the current value in the set

keep track of all values currently in the set in an array
in this implementation, the current numbers array is copied in every iteration of the recursive call
*/

/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function (k, n) {
    const ansArr = []
    const recursiveSum = (k, n, ansArr, curNums, sum) => {
        if (sum > n) { // sum too large
            return false
        }
        if (k == 0) { // the set has k values
            if (sum == n) { // sum matches n
                ansArr.push(curNums)
                return true
            }
            return false // sum does not match n
        }
        if (k < 0) { // should never happen
            return -1
        }
        let start = 1
        if (curNums.length > 0) {
            start = curNums[curNums.length - 1] + 1
        }
        for (let i = start; i <= 9; i++) {
            recursiveSum(k - 1, n, ansArr, [...curNums, i], sum + i)
        }
    }
    recursiveSum(k, n, ansArr, [], 0)
    return ansArr
};

/*
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 
*/

/*
improvement from leetcode discussion by hi-malik:
3 main points of improvement:
1. the current set array is pushed/popped instead of copied (1 array instead of many copies)
    - the array is still copied when added to the returned array
2. keep track of the start value as an argument of the recursive function
3. the sum of the array is integrated into n (n-sum), reducing the need to pass an additional argument for sum
*/

/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function (k, n) {
    const solve = (start, k, n, temp, res) => {
        if (n == 0 && temp.length == k) {
            res.push([...temp])
        }
        for (let i = start; i <= 9; i++) {
            temp.push(i)
            solve(i + 1, k, n - i, temp, res)
            temp.pop()
        }
    }
    const res = []
    solve(1, k, n, [], res)
    return res
};