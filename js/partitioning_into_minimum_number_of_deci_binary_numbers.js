// leecode problem # 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

/*
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.


Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:
Input: n = "82734"
Output: 8

Example 3:
Input: n = "27346209830709182346"
Output: 9

Constraints:

1 <= n.length <= 10^5
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.
*/

/*
My solution: find the highest digit value in the string
observation: the number of deci-binary numbers required is always the highest digit in the string.
    - ex: if there the highest digit is 8 in the string, it requires at least 8 deci-binary numbers
        - each deci-binary number needs to have 1 at the location of 8

Runtime: O(N) where N is length of the string
Space: O(1), the memory usage does not depend on length of input
*/

/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function (n) {
    let ans = 0
    for (let digit of n) {
        digit = parseInt(digit)
        if (digit > ans) {
            ans = digit
        }
    }

    return ans
};