// leetcode problem # 5. Longest Palindromic Substring

/*
Given a string s, return the longest palindromic substring in s.


Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
*/

/*
My solution: dp matrix of all possible letter lengths and starting indeces
A dynamic programming matrix is created to 


Runtime: O(N^2), where N is the length of string s. All start positions and lengths (both up to N) are run once
Space: O(N^2), where N is the length of string s. The dp matrix takes up N^2 space.

However, runtme of ~2000ms and memory usage of 143.9MB suggests that there are much faster approaches
*/

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    // build the DP matrix
    const palindromeMatrix = []
    for (let i = 0; i < s.length; i++) {
        palindromeMatrix.push([])
        for (let j = 0; j < s.length; j++) {
            palindromeMatrix[i].push(false)
        }
    }

    // the smallest palindrome is a single letter, which is the base case if there are no other palindromes.
    let longestStartIndex = 0
    let longestLength = 1

    // initialize all single-letter substrings to be palindromes
    for (let i = 0; i < s.length; i++) {
        palindromeMatrix[0][i] = true
    }

    // iterate through the dp matrix
    for (let i = 1; i < s.length; i++) {
        for (let j = 0; j < s.length - i; j++) {
            // if the front letter and the back letter are identical, the substring could be a palindrome with the following conditions:
            // if the substring has a length of 2, then it's a palindrome
            // if the substring of 2 less length and starts 1 index to the right is a palindrom, then this substring is a palindrome
            if ((s[j] == s[j + i]) && (i == 1 || palindromeMatrix[i - 2][j + 1])) {
                palindromeMatrix[i][j] = true
                if (i + 1 > longestLength) {
                    longestStartIndex = j
                    longestLength = i + 1
                }
            }
        }
    }

    return s.slice(longestStartIndex, longestStartIndex + longestLength)
};

/*
Solutions from Leetcode:
Dynamic Programming: the DP matrix can also be structured to hold the start and end positions of the palindrome
Manacher's Algorithm: https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
"Expand Around Center" (shown below)
- A palindrome can be seen as a string of words "expanding" around a centerpoint
    - if x is a palindrome, then expanding the palindrome on both sides with the same letter produces a palindrome
        -> "bab" is a palindrome because "a" is a palindrome and both sides are expanded with "b"
- There are 2 * N - 1 centerpoints
    - the palindrome can be centered on a letter, or between two letters
- Runtime: O(N^2), each center needs O(N) time to expand, and there are O(N) centers
- Space: O(1)
*/


/**
 * @param {string} s
 * @return {string}
 */
var longestPalindromeLeetCode = function (s) {
    const expandAroundCenter = (s, left, right) => {
        let L = left
        let R = right

        while (L >= 0 && R < s.length && s[L] == s[R]) {
            L--
            R++
        }
        return R - L - 1
    }

    if (s == null || s.length < 1) return null

    let start = 0
    let end = 0

    for (let i = 0; i < s.length; i++) {
        let len1 = expandAroundCenter(s, i, i)
        let len2 = expandAroundCenter(s, i, i + 1)
        let len = Math.max(len1, len2)
        if (len > end - start) {
            start = i - (len - 1) / 2
            end = i + len / 2
        }
    }

    return s.slice(start, end + 1)
};
