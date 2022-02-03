/*
  Sum To One Digit
  Implement a function sumToOne(num)​ that,
  given a number, sums that number’s digits
  repeatedly until the sum is only one digit. Return
  that final one digit result.
  Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

const num4 = 987234;
const expected4 = 6
// 9+8+7+2+3+4 = 3+3 = 6

const num5 = 9999999999999999999999999999999;

/*
create a function that takes in a number (num) and returns a number
sum the number at each digit of num
    get the number at each digit by taking the modulus of num, and then dividing num by 10
    repeat until num is less than 10
base case: num is less than 10: return num
recursive call: call the function for the sum
*/



/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function sumToOneDigit(num) {
    if (num < 10) {
        return num
    }
    return sumToOneDigit(num%10 + sumToOneDigit(Math.floor(num/10)))
    // let sum = 0
    // while (num > 0) {
    //     sum += num % 10
    //     num = Math.floor(num / 10)
    // }
    // return sumToOneDigit(sum)
}

// console.log(sumToOneDigit(num1));
// console.log(sumToOneDigit(num2));
// console.log(sumToOneDigit(num3));
// console.log(sumToOneDigit(num4));
// console.log(sumToOneDigit(num5));
// **********************************************************

/* 
  String Anagrams
  Given a string,
  return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
  Ok to use built in methods
*/

const str1 = "lim";
const two_expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
const str2 = "limqwe";
const str3 = "limqweqr";
const str4 = "limqweqraw";
// Order of the output array does not matter



/*
create a function that takes in a string str and returns an array of strings
split the string into array of characters
iterate through the characters array
    for each letter, recursively call the function with remaining letters
base case: if the string is only one letter: return letter as an array of 1 letter?
*/


/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
function generateAnagrams(str) {
    // console.log(str);
    let anagramArray=[]
    if (str.length <= 1) {
        // console.log("************************BASECASE***********************");
        return [str]
    }
    let letterArray = str.split("")
    // for (let letter of letterArray) {
    for (let i = 0; i < letterArray.length; i++) {
        let subArray = letterArray.slice(0,i).concat(letterArray.slice(i+1, letterArray.length))
        let subString = subArray.join("")
        // console.log(subString);
        for (let subAnagram of generateAnagrams(subString)) {
            anagramArray.push(letterArray[i] + subAnagram) 
        }
    }
    return anagramArray
}


function generateAnagrams2(str, memo={}) {
    // console.log(str);
    let anagramArray=[]
    if (str.length <= 1) {
        // console.log("************************BASECASE***********************");
        return [str]
    }
    let letterArray = str.split("")
    // for (let letter of letterArray) {
    for (let i = 0; i < letterArray.length; i++) {
        let subArray = letterArray.slice(0,i).concat(letterArray.slice(i+1, letterArray.length))
        let subString = subArray.join("")
        // console.log(subString);
        if (!memo.hasOwnProperty(subString)) {
            memo[subString] = generateAnagrams2(subString, memo)
        }
        for (let subAnagram of memo[subString]) {
            anagramArray.push(letterArray[i] + subAnagram) 
        }
    }
    return anagramArray
}
console.log(generateAnagrams(str1))
console.log(generateAnagrams(str2))
console.log(generateAnagrams(str3))
console.log(generateAnagrams(str4))

// console.log(generateAnagrams2(str1))
// console.log(generateAnagrams2(str2))
// console.log(generateAnagrams2(str3))
// console.log(generateAnagrams2(str4))