// leetcode problem #97. Interleaving String

/*
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.


Example 1:
https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
*/


/*
My solution: dynamic programming (2D)

In a brute force solution, it is difficult to decide whether a character in s3 should be taken from s1 or s2.
By utilizing dynamic programming, the logic will effectively check both ways, elliminating the uncertainty.

main logic:
- iterate through each cell in the dp matrix:
    - if either the cell above or the cell to the left of the current cell is valid, the current cell could be valid
        - check whether the cell is valid or not.
            - if the cell above is valid, check if the next letter in s1 matches the next letter in s3
            - if the cell to the left is valid, check if the next letter in s2 matches the next letter in s3
            * only one of the checks above needs to be valid for the cell to be valid.
    - otherwise, the current cell is invalid
    - a cell is valid if i letters from s1 and j letters from s2 can interleave into the first i+j letters of s3.

Runtime: O(M*N) where M and N are the lengths of s1 and s2, respectively.
Space: O(M*N) where M and N are the lengths of s1 and s2, respectively.

Runtime of 140ms (faster than 17.69% of JavaScript submissions) suggests that there could be performance improvements.
The follow up suggests that the dp matrix (2D) can be reduced to a dp array (1D)
*/
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function (s1, s2, s3) {
    // edge cases:
    // if concatenating s1 and s2 does not produce a string with the same length as s3, s1 and s2 cannot be interleaved into s3.
    if (s1.length + s2.length != s3.length) {
        return false
    }

    // if the above condition was false, then if s1 == s2 == s3 == "", then s1 and s2 can be interleaved into s3.
    if (s3.length === 0) {
        return true
    }

    // build the empty dp matrix
    let dp = []
    for (let i = 0; i < s1.length + 1; i++) {
        dp.push([])
        for (let j = 0; j < s2.length + 1; j++) {
            dp[i].push(false)
        }
    }


    // populate the first row and first column of the dp matrix
    dp[0][0] = true

    for (let i = 0; i < s1.length; i++) {
        if (s1[i] == s3[i]) {
            dp[i + 1][0] = true
        } else {
            break
        }
    }

    for (let j = 0; j < s2.length; j++) {
        if (s2[j] == s3[j]) {
            dp[0][j + 1] = true
        } else {
            break
        }
    }


    // main logic:
    // if either the cell above or the cell to the left is valid, the current cell could be valid
    // - check whether the cell is valid or not.
    // otherwise, the current cell is invalid
    // a cell is valid if i letters from s1 and j letters from s2 can interleave into the first i+j letters of s3.
    for (let i = 1; i < s1.length + 1; i++) {
        for (let j = 1; j < s2.length + 1; j++) {
            if (dp[i][j - 1]) {
                if (s2[j - 1] == s3[i + j - 1]) {
                    dp[i][j] = true
                    continue
                }
            }
            if (dp[i - 1][j]) {
                if (s1[i - 1] == s3[i + j - 1]) {
                    dp[i][j] = true
                }
            }
        }
    }


    return dp[s1.length][s2.length]
};

/*
Solution from leetcode solutions: 1D dynamic programming (originally written in java)
This solution traverses left to right first, and then top to bottom.
- it does not require pre-populating the first row and the first column
By using this traversal pattern, the 2D dp matrix can be reduced to a 1D dp array.
- the only relevant information at any given row is the results of the previous row, any more rows above do not offer relevant information.

Runtime: O(M*N) where M and N are the lengths of s1 and s2, respectively.
Space: O(N) where N is the lengths of s2.

Leetcode submission improvement:
Reduced runtime from 140ms to 116ms (faster than 17.69% to faster than 39%)
Reduced memory from 45.5MB to 43.5MB (less than 42.8% to less than 93.42%)

*/

/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave2 = function (s1, s2, s3) {
    if (s1.length + s2.length != s3.length) {
        return false
    }

    let dp = []
    for (let i = 0; i <= s2.length; i++) {
        dp.push(false)
    }

    for (let i = 0; i <= s1.length; i++) {
        for (let j = 0; j <= s2.length; j++) {
            if (i == 0 && j == 0) {
                dp[j] = true
            } else if (i == 0) {
                dp[j] = dp[j - 1] && s2[j - 1] == s3[i + j - 1]
            } else if (j == 0) {
                dp[j] = dp[j] && s1[i - 1] == s3[i + j - 1]
            } else {
                dp[j] = (dp[j] && s1[i - 1] == s3[i + j - 1]) || (dp[j - 1] && s2[j - 1] == s3[i + j - 1])
            }
        }
    }

    return dp[s2.length]
};