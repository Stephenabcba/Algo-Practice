// leetcode problem # 387. First Unique Character in a String

/*
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.
*/

/*
My solution:

Step 1: Find the first occurance index of each character
- omit the character if it has been found more than once
    - the algorithm sets the index to Infinity

Step 2: Find the smallest first occurance index and return the value
- If there's no smallest first occurance index, return -1
    - the algorithm will return -1 if the minimum was Infinity

Runtime: O(N) where N is the length of input string s
Space: O(M) where M is the number of unique characters in string s, which is up to 26 lowercase English letters.
*/


/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    let firstOccurance = {}

    // Step 1: Find the first occurance index of each character
    for (let i = 0; i < s.length; i++) {
        if (firstOccurance.hasOwnProperty(s[i])) {
            firstOccurance[s[i]] = Infinity
        } else {
            firstOccurance[s[i]] = i
        }
    }

    // Step 2: Find the smallest first occurance index and return the value
    let min = Infinity
    for (let lastIndex of Object.values(firstOccurance)) {
        if (lastIndex < min) {
            min = lastIndex
        }
    }

    return min === Infinity ? -1 : min
};