// leetcode problem # 242. Valid Anagram

/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
*/

/*
My solution: Use a dictionary
1. Find the count of each letter in string s
2. Compare to the count of each letter in string t
- if string t contains a letter not in s, t is not an anagram of s
- if string t has more of a letter than s, t is not an anagram of s
3. if s and t has the same count of each character, t is an anagram of s

Runtime: O(N) where N is the number of characters in the strings s and t
Memory: O(M) where M is the number of characters in the character set; in this case 26
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    // two strings cannot be anagrams of each other if they are not equal in length
    if (s.length != t.length) {
        return false
    }

    let letterDict = {}

    for (let letter of s) {
        if (letterDict.hasOwnProperty(letter)) {
            letterDict[letter] += 1
        } else {
            letterDict[letter] = 1
        }
    }

    for (let letter of t) {
        if (letterDict.hasOwnProperty(letter)) {
            letterDict[letter] -= 1
            // t has too many of a letter
            if (letterDict[letter] < 0) {
                return false
            }
        } else {
            // t has a letter that does not exist in s
            return false
        }
    }

    return true
};