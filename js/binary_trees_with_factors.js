// leetcode problem # 823. Binary Trees With Factors

/*
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.


Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 10^9
All the values of arr are unique.
*/

/*
My solution: Dynamic Programming
Observation: for every value, the number of ways a valid tree can be made with the value as the root is the sum of the follows:
1. the value itself is a valid tree (1 way)
2. the product of the ways of its children to form valid trees
    - the children are any two numbers in arr that multiply to the root
    - if there are multiple sets are children, the products are added
        -ex: if the parent is 12 and the children are (4,3) and (3,4), and there are 1 way to form a valid tree with 3 and 2 ways for 4:
            - the total valid ways for 12 is 2 * 1 + 1 * 2, which is 4;

Therefore, for any value, find all possible children combinations, and multiply the ways.


Runtime: O(N^2 * log(N)) where N is the length of the arr array
Space: O(N) where N is the length of the arr array

*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var numFactoredBinaryTrees = function (arr) {
    // sort the array to allow for binary search
    arr.sort((a, b) => a - b)

    let dp = []
    for (let num of arr) {
        dp[num] = -1
    }

    let recurse = (num) => {
        // if the value was already processed, use the saved value
        if (dp[num] >= 0) {
            return dp[num]
        } else {
            // otherwise, process the value
            let result = 1
            // find all factors that has the product of the current number
            for (let child of arr) {
                if (child * arr[0] > num) {
                    break
                }
                let start = 0
                let end = arr.length - 1
                let middle
                // binary search for whether there is another value that pairs with child and creates a valid pair.
                while (start < end) {
                    middle = Math.floor((start + end) / 2)
                    if (child * arr[middle] > num) {
                        end = middle - 1
                    } else if (child * arr[middle] < num) {
                        start = middle + 1
                    } else {
                        start = middle
                        break
                    }
                }
                // the number of ways that the current number can form a valid tree is equal to the sum of the product of ways that the children can form valid trees
                if (child * arr[start] == num) {
                    result += recurse(child) * recurse(arr[start])
                }
            }
            dp[num] = result
            return result
        }
    }

    let ans = 0
    for (let num of arr) {
        ans = (ans + recurse(num)) % (1000000007) // reduce the answer value as requested by the problem
    }

    return ans
};

/*
Solution by Leetcode:
As the array is sorted from smallest to largest, and the children of the tree is always smaller than the parent, recursion is not needed.
The solution can be done iteratively.
Using a dictionary, the binary search can also be skipped.

Runtime: O(N^2) where N is the length of the arr array
Space: O(N) where N is the length of the arr array
*/


/**
 * @param {number[]} arr
 * @return {number}
 */
var numFactoredBinaryTrees = function (arr) {
    let MOD = 1000000007
    let N = arr.length
    arr.sort((a, b) => a - b)
    dp = new Array(N).fill(1)

    let index = {}
    for (let i = 0; i < N; i++) {
        index[arr[i]] = i
    }

    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < i; j++) {
            // if this is true, arr[j] is a left child of arr[i]
            // just need to check if the right child exists in the array
            if (arr[i] % arr[j] == 0) {
                let right = arr[i] / arr[j];
                if (index.hasOwnProperty(right)) {
                    dp[i] = (dp[i] + dp[j] * dp[index[right]]) % MOD
                }
            }
        }
    }

    let ans = 0
    for (let x of dp) ans += x
    return ans % MOD
};