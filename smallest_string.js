// leetcode problem #1663. Smallest String With A Given Numeric Value
/*
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Constraints:

1 <= n <= 105
n <= k <= 26 * n
*/

//Input: 
const n = 3
const k = 27
//Output: 
const output = "aay"
/*
Explanation: 
The numeric value of the string is 1 + 1 + 25 = 27,
and it is the smallest string with such a value and length equal to 3.
*/

//Input: 
const n2 = 5
const k2 = 73
//Output: 
const output2 = "aaszz"

const n3 = 3
const k3 = 77

/*
My Solution:
idea:
- to minimize the lexicographical score of the string, we should push the scores of letters as far back as possible
    -all "a" should be at the front of the string and "z" at the back of the string, as required
- there should be at most 1 letter in the string that is not "a" or "z"
ex: aaz and aby have the same score, but aaz has the lower lexicographical score
implementation:
- we do not build the actual string until the end
1. assume all n letters are "a"s
    - the number of "a"s can be stored as an integer
    - the score of the current string is n * 1 = n
2. find the number of "z"s that should be at the end of the string
    - every "a" the is converted to "z" increases the score by 25
    - the number of "z"s converted can be found mathematically by dividing the remaining score by 25\
        - only whole number multiples are counted
    - decrease the number of "a"s by the number of "z"s converted
    - increase score accordingly
    - by the end of this step, the difference between the target score and current score is less than 25
3. find the single letter that is neither "a" nor "z", if needed
    - this letter should bring the current score up to the target score
    - if the conversion is needed:
        - convert an "a" to the letter at 1 + remaining score
            - decrease the number of "a" by 1
        - the letter will be after "a"s and before "z"s
    - ex: current string: "aaazz", (target score - current score = 5), the string becomes "aafzz"
        - the last "a" is converted to "f", increasing the current score by 5
4. build the string and return

*/

/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getSmallestString = function (n, k) {
    let aCount = n;
    let score = n;

    let zCount = Math.floor((k - score) / 25)
    aCount -= zCount
    score += zCount * 25

    let midVal = (k - score)
    if (midVal > 0) {
        aCount--
        return "a".repeat(aCount) + String.fromCharCode("a".charCodeAt(0) + midVal) + "z".repeat(zCount)
    } else {
        return "a".repeat(aCount) + "z".repeat(zCount)
    }

};

console.log(getSmallestString(n3, k3))