// leetcode problem # 342


/*
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4^x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
*/

/*
My solution: divide by 4
1. Divide the number by 4 until it is less than 4
2. if the resulting number is not 1, the number is not a power of 4

Runtime: O(log_4 N) where N is the input number
Space: O(1), memory usage does not scale with input.
*/

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function (n) {
    while (n >= 4) {
        n /= 4
    }
    return n == 1
};

/*
Solution by ankit4601 in leetcode discussion:
Make use of binary operators
3 conditions:
1. N must be greater than 0 (power of 4 is never <= 0)
2. N must be a power of 2 (all powers of 4 are powers of 2) => there is only a single 1 in binary representation of N
3. The only 1 in the binary representation of N is in an even location
If all three conditions are true, N is a power of 4

Runtime: O(1)
Space: O(1)
*/

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour2 = function (n) {
    return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555)
};