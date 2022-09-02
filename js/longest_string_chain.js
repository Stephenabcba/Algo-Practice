// leetcode problem # 1048. Longest String Chain

/*
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
*/

/*
My solution: check the words with 1 lower in length
For ease of accessing the words based on length, the words are sorted according to their lengths

For any word1 with length n, check all words with length n-1 for word1's predecessor
    - for better performance, skip any words with length n-1 if it cannot increase chain length of word1

Implementation details:
- keep track of the start of words with length k, where k is between 1 and 16
- all word chains have an initial trivial length of 1

Runtime: O(N^2), where N is the number of words given
- Sorting algorithm likely takes O(N * logN) time
- Preprocessing takes O(N) time
- The main logic could take up to O(k * N ^2) time, where k is 16
    - worst case scenario: the words only have 2 lengths, N and N-1, and the count of words with length N equals that of length N-1
        - every word with length N must check every word with length N-1
        - the word comparison logic depends on the length of the word, which could be up to 16 letters
Space: O(N), where N is the number of words given
- the array keeping track of the start position is O(k), where k is 16
- the sorting algorithm could take up to O(N) space
- the array keeping track of the length of chains of each word is O(N)
*/

/**
 * @param {string[]} words
 * @return {number}
 */
var longestStrChain = function (words) {
    // sort the words according to their lengths
    words.sort((a, b) => a.length - b.length)

    const chains = []
    const wordLengthStart = []
    let wordLength = 1
    for (let i = 0; i <= 16; i++) {
        wordLengthStart.push(-1)
    }

    for (let i = 0; i < words.length; i++) {
        // all words have at least the trivial chain length of 1
        chains.push(1)

        // find the start position of the word lengths
        if (words[i].length > wordLength) {
            wordLength = words[i].length
        }
        if (wordLengthStart[words[i].length] < 0) {
            wordLengthStart[words[i].length] = i
        }
    }

    let longestChain = 1

    for (let i = 0; i < words.length; i++) {
        if (wordLengthStart[words[i].length - 1] < 0) {
            continue
        }

        // only words with length - 1 are considered
        for (let j = wordLengthStart[words[i].length - 1]; j < wordLengthStart[words[i].length]; j++) {
            // don't process any word that can not grow the word chain
            if (chains[i] > chains[j] + 1) {
                continue
            }

            // check if the shorter word can match the longer word by removing exactly 1 letter
            // if a letter is removed, check if the next letter in the longer word matches with the current letter in the shorter word
            // if they do not match, the shorter word is not a predecessor.
            let skips = 0
            for (let k = 0; k < words[j].length; k++) {
                if (words[j][k] != words[i][k + skips]) {
                    skips++
                    if (words[j][k] != words[i][k + skips]) {
                        skips++
                    }
                }
                if (skips > 1) {
                    break
                }
            }

            // if the word is a predecessor, increment the chain length of the longer word
            if (skips <= 1) {
                chains[i] = chains[j] + 1
                if (chains[i] > longestChain) {
                    longestChain = chains[i]
                }
            }
        }
    }

    return longestChain
};