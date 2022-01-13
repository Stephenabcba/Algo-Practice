/* 
    String: Is Palindrome
    Create a function that returns a boolean whether the string is a strict palindrome. 
        - palindrome = string that is same forwards and backwards

    Do not ignore spaces, punctuation and capitalization
 */

    const str1 = "a x a";
    const expected1 = true;
    
    const str2 = "racecar";
    const expected2 = true;
    
    const str3 = "Dud";
    const expected3 = false;
    
    const str4 = "oho!";
    const expected4 = false;
    
/**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
function isPalindrome(str) {
    for (var i = 0; i < str.length/2; i++) {
        if (str[i] != str[str.length-1-i]) {
            return false
        }
    }
    return true
}

// console.log(isPalindrome(str1))
// console.log(isPalindrome(str2))
// console.log(isPalindrome(str3))
// console.log(isPalindrome(str4))

//   ********************************************************************************

/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/

const two_str1 = "what up, daddy-o?";
const two_expected1 = "dad";

const two_str2 = "uh, not much";
const two_expected2 = "u";

const two_str3 = "Yikes! my favorite racecar erupted!";
const two_expected3 = "e racecar e";

const two_str4 = "a1001x20002y5677765z";
const two_expected4 = "5677765";

const two_str5 = "a1001x20002y567765z";
const two_expected5 = "567765";

const two_str6 = "cacac"

/**
 * Finds the longest palindromic substring in the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The longest palindromic substring from the given string.
 */

function longestPalindromicSubstring(str) {
    var retStrStart = 0
    var retStrLen = 1
    for (var wordStart = 0; wordStart < str.length; wordStart++) {
        for (var wordEnd = wordStart+1; wordEnd < str.length+1; wordEnd++) {
            if (isPalindrome(str.substring(wordStart,wordEnd))) {
                if ((wordEnd-wordStart) > retStrLen) {
                    retStrStart = wordStart
                    retStrLen = wordEnd-wordStart
                }
            }
        }
    }
    return str.substring(retStrStart,retStrStart+retStrLen)
}

console.log(longestPalindromicSubstring(two_str1))
console.log(longestPalindromicSubstring(two_str2))
console.log(longestPalindromicSubstring(two_str3))
console.log(longestPalindromicSubstring(two_str4))
console.log(longestPalindromicSubstring(two_str5))
console.log(longestPalindromicSubstring(two_str6))