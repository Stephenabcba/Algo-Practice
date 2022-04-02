// leetcode problem # 680. Valid Palindrome II
/*
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
*/

/*
my solution: modified check palindrome
basic palidrome check algorithm: check each letter at index i against the letter at index s.length-1-i
- only need to iterate until the front meets the back
- if any letter mismatches, the string is not a palindrome
challenge: knowing whether a front or a back letter should be deleted when mis-matched
modification: check both if needed
** the front index now needs to be separated from the back index (cannot just use s.length-1-i)
if a letter mismatches, do the following:
    - the first mismatch: assume that the front letter should be removed, then continue the check
        - save the index of the removed letter for later
        - increment the front index without modifying the back index
    - the second mismatch: assume that the back letter should've been removed in the first mismatch, then continue the check
        - reset the front and back index to when the first mismatch happened, and decrement the back index
        - set a flag marking that the back letter is now removed instead
    - the third mismatch: the string now requires more than 1 letter removed to become a palindrome.
        - return false
if the palidrome check completes before the third mismatch happens, the string fits the requirement.
*/


/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function (s) {
    let front = 0
    let back = s.length - 1
    let deleteIndex = -1
    let deleteBack = false
    while (front <= back) {
        if (s[front] === s[back]) {
            front += 1
            back -= 1
        } else {
            if (deleteIndex < 0) {
                deleteIndex = front
                front += 1
            } else if (!deleteBack) {
                front = deleteIndex
                back = s.length - deleteIndex - 2
                deleteBack = true
            } else {
                return false
            }
        }
    }
    return true
};

/*
Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
*/

/*
Refactored version from leetcode solution:
refactor the inner palindrome check to be a second function for clarity.
check if the remaining inner string is a palindrome after removing either the front or back of the mismatch
    if either string is a palindrome, the string s fits the function requirement.
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome2 = function (s) {
    let front = 0
    let back = s.length - 1

    const checkPalindrome = (s, i, j) => {
        while (i < j) {
            if (s[i] != s[j]) {
                return false
            }
            i++
            j--
        }
        return true
    }

    while (front < back) {
        if (s[front] !== s[back]) {
            return checkPalindrome(s, front + 1, back) || checkPalindrome(s, front, back - 1)
        }
        front += 1
        back -= 1
    }
    return true
};