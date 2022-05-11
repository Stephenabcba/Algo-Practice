// leetcode problem #1641. Count Sorted Vowel Strings

/*

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.


Constraints:

1 <= n <= 50 
*/

/*
My solution: recursive backtracking
base case: don't need to add any more vowels, the current case is 1 valid answer
recursive case: add more vowels that are valid (lexicographically equal or larger than the previous vowel)
    - in implementation, decrement n by 1 when recursively calling, therefore making n = 0 when the base case should be reached.

sum up all valid answers to get the total count.

for simplicity of computations, a e i o u is mapped to 0 1 2 3 4, respectively.
    - when recursing, only consider the vowels larger than or equal to the previous vowel.
        - ex: if the previous vowel is i (2), the only consider i o u (2 3 4)
*/

/**
 * @param {number} n
 * @return {number}
 */
var countVowelStrings = function (n) {
    const recursiveCount = (n, prev) => {
        if (n == 0) { // base case
            return 1
        }
        let count = 0
        for (let i = prev; i < 5; i++) {
            count += recursiveCount(n - 1, i) // recursive case
        }
        return count
    }
    return recursiveCount(n, 0)
};

/*
Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045
*/