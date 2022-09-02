// leetcode problem # 583. Delete Operation for Two Strings

/*
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
*/

/*
My attempt: build the shared letters string then count the discarded letters

Greedily try to pair the letters in the first string to the nth occurance of the letter in the second string
- the first "a" gets paired with the first "a", the second "a" gets paired with the second "a", and so on.

From the pairs, find the longest subsequence such that the paired index is always increasing.

The number of "steps" would then be the word1.length + word2.length - 2 * shared subsquence.length

The attempt failed due to the pairing process. 

example case of failed test case:
"uuuuuuuabc"
"uuuudsfeadfuuuuabc"
the algorithm chose the first "a" in the second string to pair with the "a" in the second string,
even though choosing the second "a" in the second string would've led to a longer subsequence.
*/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistanceAttempt = function (word1, word2) {
    const word2Positions = {}
    for (let i = word2.length - 1; i >= 0; i--) {
        if (word2Positions.hasOwnProperty(word2[i])) {
            word2Positions[word2[i]].push(i)
        } else {
            word2Positions[word2[i]] = [i]
        }
    }

    const letterPairs = []

    for (let i = 0; i < word1.length; i++) {
        if (word2Positions.hasOwnProperty(word1[i]) && word2Positions[word1[i]].length > 0) {
            letterPairs.push(word2Positions[word1[i]].pop())
        } else {
            letterPairs.push(-1)
        }
    }

    console.log(letterPairs)

    const letterStack = []
    let longestWord = 0

    for (let pair of letterPairs) {
        if (pair >= 0) {
            while (letterStack.length > 0 && letterStack[letterStack.length - 1] > pair) {
                letterStack.pop()
            }
            letterStack.push(pair)
            if (letterStack.length > longestWord) {
                longestWord = letterStack.length
            }
        }
    }

    return word1.length + word2.length - 2 * longestWord
};

/*
Solution in Leetcode (originally written in Java)
The solution also utilizes the idea of longest common subsequence (LCS), but it also utilizes dynamic programming
The dp matrix holds the length of the LCS, where dp[i][j] holds the length of the LCS for word 1 up to the i-1 th index and word 2 up to the j-1 th index
    - thus, if i or j is 0, the dp array would be 0
2 cases when building the dp
1. the characters at word1[i-1] and word2[j-1] match: add 1 to dp[i-1][j-1] (LCS length increased)
2. the characters do not match: take the higher LCS of dp[i-1][j] or dp[i][j-1] (hold the LCS length from the smaller index)

The answer is word1.length + word2.length - 2 * dp[word1.length][word2.length]

Runtime: O(M*N), where M and N are the lengths of word1 and word2, respectively.
    - the algorithm processes each cell in the dp matrix exactly once
Space: O(M*N), where M and N are the lengths of word1 and word2, respectively.
    - main memory usage is the dp matrix
*

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function (word1, word2) {
    const dp = []
    for (let i = 0; i <= word1.length; i++) {
        dp.push([])
        for (let j = 0; j <= word2.length; j++) {
            dp[i].push(0)
        }
    }

    for (let i = 0; i <= word1.length; i++) {
        for (let j = 0; j <= word2.length; j++) {
            if (i == 0 || j == 0) {
                continue
            }
            if (word1[i - 1] == word2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1]
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1])
            }
        }
    }

    return word1.length + word2.length - 2 * dp[word1.length][word2.length]
};