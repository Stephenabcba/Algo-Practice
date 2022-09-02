//  Leetcode problem # 258. Add Digits
// Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

// Example 1:

// Input: 
const num = 38
// Output: 
const result = 2
// Explanation: The process is
// 38 --> 3 + 8 --> 11
// 11 --> 1 + 1 --> 2 
// Since 2 has only one digit, return it.


/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    let curNum = num
    let result = num
    while (curNum >= 10) {
        result = 0
        while (curNum > 0) {
            result += curNum % 10
            curNum = Math.floor(curNum/10)
        }
        curNum = result
    }
    return result
};

// console.log(addDigits(8));

// mathematical solution from leetcode
var addDigits2 = function(num) {
    if (num === 0) return 0
    if (num === 9) return 9
    return num % 9
}

console.log(addDigits2(8))