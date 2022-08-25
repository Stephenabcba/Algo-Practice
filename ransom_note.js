// leetcode problem # 383. Ransom Note

/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
*/

/*
My solution: compare count of letters
Observation: the order of the letters in ransomNote and magazine do not matter
-> What matters is that magazine has enough of each letter for ransomNote

Solution logic:
1. Find the count of each unique letter in ransom note
2. Find the count of each unique letter in magazine
3. For each unique letter(a,b,c...) in ransom note, make sure the count of the same letter in magazine is higher
-> if the count of any letter is lower in magazine, the ransom note cannot be constructed from the magazine (return false)
4. if all letters have passed, the ransome note can be constructed from the magazine (return true)

Runtime: O(N + M + K) Where N is the length of the ransom note string, M is the length of the magazine string, and K is the number of allowed characters
-> in this case, K is the lowercase English alphabet (26)
Space: O(K) where K is the number of allowed characters
-> in this case, K is the lowercase English alphabet (26)
*/

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
    let ransomLetters = {}
    let magazineLetters = {}

    for (let letter of ransomNote) {
        if (ransomLetters.hasOwnProperty(letter)) {
            ransomLetters[letter] += 1
        } else {
            ransomLetters[letter] = 1
        }
    }

    for (let letter of magazine) {
        if (magazineLetters.hasOwnProperty(letter)) {
            magazineLetters[letter] += 1
        } else {
            magazineLetters[letter] = 1
        }
    }

    for (let letter of Object.keys(ransomLetters)) {
        if (!magazineLetters.hasOwnProperty(letter) || magazineLetters[letter] < ransomLetters[letter]) {
            return false
        }
    }

    return true
};