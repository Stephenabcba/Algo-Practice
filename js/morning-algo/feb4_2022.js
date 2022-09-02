/* 
    recursively find the lowest common multiple between two numbers
    "A common multiple is a number that is a multiple of two or more integers. 
    The common multiples of 3 and 4 are 0, 12, 24, .... 
    The least common multiple (LCM) of two numbers is the smallest number (not zero) 
    that is a multiple of both."
    
    Try writing two columns of multiples as a starting point:
    starting with 15 and 25 and keep writing their multiples until you find the lowest common one
    then turn this in to a step by step instruction
    15 25
    30 50
    45 75
    60
    75
    75 is the first common
*/

const num1A = 1;
const num1B = 1;
const expected1 = 1;

const num2A = 5;
const num2B = 10;
const expected2 = 10;

const num3A = 10;
const num3B = 5;
const expected3 = 10;

const num4A = 6;
const num4B = 8;
const expected4 = 24;

const num5A = 15;
const num5B = 25;
const expected5 = 75;

/*
create a function that takes 2 numbers and returns another number that is the least common multiple of the input numbers
edge case: if one of the numbers is 0 or lower, return -1?
base case: if inputs are the same: return one of the inputs
recursive call: increase the lower sum by the "base number"
*/

/**
 * Add params if needed for recursion
 * Finds the lowest common multiple of the two given ints.
 * @param {number} a
 * @param {number} b
 * @returns {number} The lowest common multiple of the given ints.
 */
function lowestCommonMult(a, b, aSum=0, bSum=0) {
    if (a <= 0 || b <= 0) {
        return -1
    }
    if (aSum === 0) aSum = a
    if (bSum === 0) bSum = b

    if (aSum == bSum) {
        return aSum
    }

    if (aSum > bSum) {
        return lowestCommonMult(a,b,aSum,bSum+b)
    }
    return lowestCommonMult(a,b,aSum+a,bSum)
}

console.log(lowestCommonMult(num1A,num1B));
console.log(lowestCommonMult(num2A,num2B));
console.log(lowestCommonMult(num3A,num3B));
console.log(lowestCommonMult(num4A,num4B));
console.log(lowestCommonMult(num5A,num5B));

// ************************************************************************

/* 
    Binary String Expansion
    You are given a STRING containing chars "0", "1", and "?"
    For every "?" character, either "0" or "1" can be substituted.
    Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/

const two_str1 = "1?0?";
const two_expected1 = ["1000", "1001", "1100", "1101"];
const two_str2 = "10011010"
const two_str3 = ""
const two_str4 = "????"
// 1?
// 10 -> 0?
// prefix+0
//        1
// 11 -> 0?
//        0
//        1



// output list order does not matter

/*
create a function that takes in a string of only 0s, 1s, and ?s that returns a list of strings (with only 0s and 1s)
create an empty array for returning
edge case?:empty string?
base case: no question marks -> return prefix
recursive case: question mark -> return function call of itself, replacing the question mark with 0 or 1, adding a prefix
*/



/**
 * Add params if needed for recursion
 * Expands a string such that each "?" in the given string will be replaced
 * with a "0" and a "1".
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string containing to expand.
 * @returns {Array<string>} The expanded versions of the given string.
 */
function binaryStringExpansion(str, prefix ="") {
    // console.log("STR:",str);
    // console.log("PREFIX",prefix);
    // if (str.length == 0) return [prefix]
    for (let i = 0; i < str.length; i++) {
        let letter = str[i]
        if (letter != "?") {
            prefix += letter
        } else {
            // console.log("WE ARE THERE")
            return binaryStringExpansion(str.slice(i+1), prefix+"0").concat(binaryStringExpansion(str.slice(i+1), prefix+"1"))
        }
    }
    return [prefix]
}

console.log(binaryStringExpansion(two_str1));
console.log(binaryStringExpansion(two_str2));
console.log(binaryStringExpansion(two_str3));
console.log(binaryStringExpansion(two_str4));