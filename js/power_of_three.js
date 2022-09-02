// leetcode problem # 326. Power of Three

/*
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
 

Constraints:

-2^31 <= n <= 2^31 - 1
 

Follow up: Could you solve it without loops/recursion?
*/

/*
My solution: keep dividing by 3

Keep dividing the number by three until the value is less than 3
If the resulting value is 1, n is a power of 3
Otherwise, n is not a power of 3.

Runtime: O(log_3 N) where N is the value of input n
Space: O(1), solution memory does not scale with input

Improvement from leetcode solutions:
Implement a check such that all values < 1 are rejected
Then change the iteration condition to n % 3 == 0

This way, if a value is not divisible by 3, it is rejected instead of continuing to iterate.
*/

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
    while (n >= 3) {
        n /= 3
    }
    return n == 1
};

/*
Solution from leetcode solutions: Change from base 10 to base 3
1. Change from base 10 to base 3 with toString()
2. match the resulting string with regex ^10*$
    - this matches any string that starts with 1 and has only trailing 0s
3. if there is a match, n is a power of 3; otherwise, n is not a power of 3.
*/

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree2 = function (n) {
    return n.toString(3).match(/^10*$/) !== null
};