/* 
    Given a string that may have extra spaces at the start and the end,
    return a new string that has the extra spaces at the start and the end trimmed (removed)
    do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "        ";
const expected2 = "";

const str3 = "   hello world earth     ";
const expected3 = "hello world earth";

const str4 = ""
const expected4 = ""


/*
PSEUDO CODE
create a function that takes in a string and returns a string
iterate through the string twice, once from the start and once from the end
    - once a non-space character is reached, stop looping and record the position as start and stop
    - if start is at the end, return empty string
iterate thourgh the string starting at start and stopping at stop
    - build the return string
return the string
*/

function trim2(str) {
    var returnString = ""
    var curWord = ""
    var wordStart = false
    for (var i = 0; i < str.length; i++) {
        if (str[i] != " ") {
            wordStart = true
            curWord += str[i]
        } else if (wordStart) {
            if (returnString.length != 0) {
                returnString += " "
            }
            returnString += curWord
            wordStart = false
            curWord = ""
        }
    }
    return returnString
}


/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
    var start = 0
    var end = str.length-1
    for (start = 0; start< str.length; start++) {
        if (str[start] != " ") {
            break
        } else if (start == str.length -1) {
            return ""
        }
    }
    for (end = str.length-1; end >= 0; end--) {
        if (str[end] != " ") {
            break
        }
    }
    var returnString = ""
    for (var i = start; i <= end; i++) {
        returnString += str[i]
    }
    return returnString
}

console.log(trim2(str1));
console.log(trim2(str2));
console.log(trim2(str3));
console.log(trim2(str4));


// ************************************************************************

/* 
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    Is there a quick way to determine if they aren't an anagram before spending more time?
    Given two strings
    return whether or not they are anagrams
*/

const two_strA1 = "yes3";
const two_strB1 = "3eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;

const two_strA5 = "not";
const two_strB5 = "noo";
const two_expected5 = false;

const two_strA6 = "motherinlaw"
const two_strB6 = "womanhitler"
const two_expected6 = true;

/*
create a function that takes in 2 strings and returns a boolean
check the length of the two strings
    - if they are not equal in length, return false
build a letters object/dictionary for each string
for each key in the dictionary, compare its value with the other dictionary's key-value pair
    -if the values don't match for any given key, return false
-if everything matches, return true
*/


/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
    if (s1.length != s2.length) {
        return false
    }
    str1Dict = {}
    str2Dict = {}
    s1 = s1.toLowerCase()
    s2 = s2.toLowerCase()
    for (var i = 0; i < s1.length; i++) {
        if (str1Dict.hasOwnProperty(s1[i])) {
            str1Dict[s1[i]]++
        } else {
            str1Dict[s1[i]] = 1
        }
        if (str2Dict.hasOwnProperty(s2[i])) {
            str2Dict[s2[i]]++
        } else {
            str2Dict[s2[i]] = 1
        }
    }
    for ([key, value] of Object.entries(str1Dict)) {
    // for (key of Object.keys(str1Dict)) {
        if (value != str2Dict[key]) {
        // if (str1Dict[key] != str2Dict[key]) {
            return false
        }
    }
    return true
}

// console.log(isAnagram(two_strA1,two_strB1));
// console.log(isAnagram(two_strA2,two_strB2));
// console.log(isAnagram(two_strA3,two_strB3));
// console.log(isAnagram(two_strA4,two_strB4));
// console.log(isAnagram(two_strA5,two_strB5));
// console.log(isAnagram(two_strA6,two_strB6));