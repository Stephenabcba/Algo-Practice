// leetcode problem # 509. Fibonacci Number

/*
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).


Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4

Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30
*/

/*
My solution: keep track of the previous two numbers
Idea: as any given fibonacci number only depends on the past two values, working from the first fibonacci number to the target number iteratively only requires saving 2 previous values at any given time.
Edge case: the first two fibonacci numbers are defined as 0 and 1, and thus do not need to be iterated.

Runtime: O(N) where N is the target fibonacci number
Space: O(1); the solution memory usage does not depend on the target fibonacci number.
*/

/**
 * @param {number} n
 * @return {number}
 */
var fib = function (n) {
    if (n <= 1) {
        return n
    }

    let current = 1
    let previous = 0
    let idx = 1
    while (idx < n) {
        // javascript has a built-in functionality of swapping values in ES 6
        // however, instead of just swapping, the current value is the sum of the past 2 values, and the past value is the previous current value
        [current, previous] = [current + previous, current]
        idx += 1
    }

    return current
};