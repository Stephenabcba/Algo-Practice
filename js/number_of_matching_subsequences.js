// leetcode problem # 792. Number of Matching Subsequences


/*
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
*/


/*
My solution: keep track of the next location of all English letters for every letter of s

By preprocessing the string s and saving the location of the next occurrance of any letter (a-z) for each index, finding whether a word is a substring of s is a O(L) task
- L is the length of the word

Runtime: O(N + M * L) where N is the length of string s, M is the number of words, and L is the length of each word

Space: O(N) where N is the length of string s

Runtime of 910ms (faster than 14.88% of JS submissions) and 169MB (less than 5.37% of JS submissions) suggests that there's room for improvement
*/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function (s, words) {
    let nextLetter = []

    const aIndex = "a".charCodeAt(0)

    let letters = []

    // initialize the array keeping track of the next letters of a character in s
    // by default, the last character in s do not have any next letters (-1)
    for (let i = 0; i < 26; i++) {
        letters.push(-1)
    }

    for (let i = 0; i < s.length; i++) {
        nextLetter.push(0)
    }

    // for each letter s (iterating backwards), make a copy of letters into nextLetter, and update the letters array
    // when this is done, the next location of any letter (if it exists) at any given index can be accessed in O(1) time
    for (let i = s.length - 1; i >= 0; i--) {
        nextLetter[i] = letters.slice()

        letters[s.charCodeAt(i) - aIndex] = i
    }

    let ans = 0

    for (let word of words) {
        let index = 0
        let match = true
        for (let i = 0; i < word.length; i++) {
            if (i == 0 && s[0] == word[0]) {
                continue
            } else if (nextLetter[index][word.charCodeAt(i) - aIndex] > 0) {
                index = nextLetter[index][word.charCodeAt(i) - aIndex]
            } else {
                match = false
                break
            }
        }
        if (match) {
            ans++
        }
    }

    return ans
};

/*
Best runtime submission for JavaScript on LeetCode:
Supporting function: isSubsequence
- Make use of indexOf array method to match the letters of each word to string s
- If indexOf returns -1 at any point, return false
- If indexOf was able to reach all letters, return true

Count the number of words that returned true from the above function.

Runtime: O(M * N) where M is the number of words, N is the length of the string s
    - although indexOf is ran O(L) times for length of word L, each character in s is iterated at most once
        - this is due to specifying the start index of indexOf every call.

Space: O(1); the solution memory usage does not scale with input size.
*/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function (s, words) {
    let len2 = words.length;
    let sum = 0;

    for (let x = 0; x < len2; x++) {
        if (isSubsequence(words[x], s) == true) {
            sum += 1;
        }
    }
    return sum;
};

var isSubsequence = function (s, t) {
    let len = s.length;
    let i = 0;
    let j = -1;

    while (i < len) {
        j = t.indexOf(s[i], j + 1);

        if (j == -1) {
            return false;
        }
        i += 1;
    }
    return true;
};