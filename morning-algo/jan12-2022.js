/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 


    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.

    - create a function that takes in a string and returns a string
    - create a return string
    - create a count variable that starts at 1
    - EDGE CASE: if string has no length
    - loop through the given string
        - compare the current string index to the index - 1 
        - if true: increase count
            - if character not already in return string then add to return string
        - if false: 
            - add the total count for the variable to return string
            - reset the count variable back to 1
    - return the return variable string...

  */

    const str1 = "aaaabbcddd";
    const expected1 = "a4b2c1d3";
    
    const str2 = "";
    const expected2 = "";
    
    const str3 = "a";
    const expected3 = "a";
    
    const str4 = "bbcc";
    const expected4 = "bbcc";
    
    /**
     * Encodes the given string such that duplicate characters appear once followed
     * by a number representing how many times the char occurs only if the
     * character occurs more than two time.
     * - Time: O(?).
     * - Space: O(?).
     * @param {string} str The string to encode.
     * @returns {string} The given string encoded.
     */
    function encodeStr(str) {
        if (str.length <= 1) {
            return str
        }
        var count = 1
        var returnString = str.charAt(0)
        for (var i = 1; i < str.length; i++) {
            if (str.charAt(i) == str.charAt(i-1)) {
                count += 1
            } else {
                returnString += count
                count = 1
                returnString += str.charAt(i)
            }
            if (i == str.length - 1) {
                returnString += count
            }
        }
        if (returnString.length < str.length)  {
            return returnString
        } else {
            return str
        }
    }

// console.log(encodeStr(str1))
// console.log(encodeStr(str2))
// console.log(encodeStr(str3))
// console.log(encodeStr(str4))
//   **************************************************************************************

/* 
    String Decode  
*/

const str1a = "a3b2c1d3";
const expected1a = "aaabbcddd";

const str2a = "a3b2c12d10";
const expected2a = "aaabbccccccccccccdddddddddd";


// 1. create a function
// 2. crete a empty string to hold result
// 3. iterate through string with index 0
    // add char at current index and assign to var letter
    // increment index
    // check the index + 1 to see if it is also a number
        //if true: 
            //take both the char and make it as var number (converted to number from string)
            //increment index once (extra)
        // add the letter var times the number var add it to the result
        // increment index
//5.

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {
    if (str.length <= 1) {
        return str
    }
    var returnString = ""
    var curLetter = str.charAt(0)
    var curLetterCount = ""
    for (var i = 1; i < str.length; i++) {
        if (isNaN(str.charAt(i))) {
            if (i != 1) {
                for (var j = 0; j < parseInt(curLetterCount); j++) {
                    returnString += curLetter
                }
            }
            curLetter = str.charAt(i)
            curLetterCount = ""
        } else {
            curLetterCount += str.charAt(i)
        }
        if (i == str.length - 1) {
            for (var j = 0; j < parseInt(curLetterCount); j++) {
                returnString += curLetter
            }
        }
    }
    return returnString
}

console.log(decodeStr(str1a))
console.log(decodeStr(str2a))