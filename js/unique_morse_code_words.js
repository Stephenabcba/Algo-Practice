// leetcode problem # 804. Unique Morse Code Words

/*
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.



Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:
Input: words = ["a"]
Output: 1

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 12
words[i] consists of lowercase English letters.
*/

/*
My solution: build each string and find unique ones

Pseudocode:
1. create a dictionary mapping each letter to their corresponding morse code
2. convert each word into their corresponding morse code
2.1 if the mapping does not exist, add it to the list of unique mappings
    - the mappings are saved in a dictionary
3. return the number of unique mappings

Runtime: O(W * L) where W is the length of the words array, and L is the length of each word
- each letter of each word is processed exactly once
Space: O(W * L^2) where W is the length of the words array, and L is the length of each word
- as string is immutable, a new string is created every time a letter's morse code is added to the string.
*/

/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function (words) {
    const letters = "abcdefghijklmnopqrstuvwxyz"
    const morseCodes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    // map each letter to its corresponding morse code.
    let morseMapping = {}
    for (let i = 0; i < 26; i++) {
        morseMapping[letters[i]] = morseCodes[i]
    }

    // keep track of unique morse code mappings.
    let uniqueMorse = {}

    // convert each word to morse code
    // if the mapping did not exist, add it to the list of unique mappings.
    for (let word of words) {
        let transformed = ""
        for (let letter of word) {
            transformed += morseMapping[letter]
        }
        if (!uniqueMorse.hasOwnProperty[transformed]) {
            uniqueMorse[transformed] = true
        }
    }

    return Object.keys(uniqueMorse).length
};