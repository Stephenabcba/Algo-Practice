// leetcode problem # 17. Letter Combinations of a Phone Number

/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
*/

/*
My solution: build the combination one by one
iterate through the digits
    - special case: first digit -> add all letters that correspond to the digit
    - otherwise, append the letters to all previous combinations
ex: "234"
first digit: add all corresponding letters
-> ["a", "b", "c"]
second digit: combine the letters with previous combinations
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
third digit: combine with previous combinations
["adg", "adh", "adi", "aeg", "aeh", "aei"...]

*/

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
    const numberMapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    let answer = []
    for (let digit of digits) {
        if (answer.length > 0) { // all digits after the first
            let newAnswer = []
            for (let part of answer) { // combine the parts in the array with the additional letter corresponding to the current digit
                for (let letter of numberMapping[digit]) {
                    newAnswer.push(part + letter)
                }
            }
            answer = newAnswer
        } else { // the first digit
            for (let letter of numberMapping[digit]) { // add all letters that the digit maps to to the array
                answer.push(letter)
            }
        }
    }
    return answer
};

/*
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
*/