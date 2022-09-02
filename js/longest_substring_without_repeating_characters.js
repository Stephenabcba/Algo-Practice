// leetcode problem # 3. Longest Substring Without Repeating Characters

/*
Given a string s, find the length of the longest substring without repeating characters.

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
*/

/*
My Solution: Making use of objects/dictionaries

Basic Idea: work bottoms up from left to right
- for all substrings that start from index 0 (lengths 1 to s.length), find the longest substring that meets the criteria.
- ex: s is "abbcccdefg"
    - check "a", "ab", "abb", "abbc" ... "abbcccdefg" to find the longest substring within each of them without repeating characters.
- only a substring that ends at the end of the current substring needs to be considered
    - only "cdefg" needs to be processed in "abbccdefg"
        - "ab" and "bc" were already processed when the substring was "ab" and "abbc", respectively.
- to find where the longest non-repeating substring starts, an object (or dictionary / hashtable) is used to keep track of the last occurance index of all seen characters
    - if the last character in the substring is repeated in the candidate substring, shorten the substring until there are no more duplicates.
        -> move the start index to the last seen index + 1

Runtime: O(N), where N is the length of string s. Iteration repeats for all characters in s.
Space: O(k), where k is the length of the set of unique characters in s. Main memory usage is the object keeping track of the last seen indeces of each unique character.


*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let startIndex = 0
    let longestLength = 0
    const lastSeen = {}

    for (let idx = 0; idx < s.length; idx++) {
        if (lastSeen.hasOwnProperty(s[idx])) {
            // move the start of the current substring to the right of the last occurance of current character if the repeated character is included in the substring.
            if (lastSeen[s[idx]] >= startIndex) {
                startIndex = lastSeen[s[idx]] + 1
            }
        }
        // add the character to the object / update the character's last seen position in the object
        lastSeen[s[idx]] = idx

        // update the longest length if current substring is longer
        if (idx - startIndex + 1 > longestLength) {
            longestLength = idx - startIndex + 1
        }
    }

    return longestLength
};

/*
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/