/* 
    Recursively reverse a string
    helpful methods:
    str.slice(beginIndex[, endIndex])
    returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";

/*
Create a function that takes in a string str and returns a string that is the reverse of str
edge case: ?
base case: input string length <= 1 : return string
recursive call: take the last letter and concatenate with reverse of the remaining string (recursive)
return result
*/

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 * 
 * 1. edge case
 * 2. base case
 * 3. recursive call
 */
function reverseStr(str) {
    if (str.length <= 1) return str
    return str[str.length-1] + reverseStr(str.slice(0,str.length-1))
}

console.log(reverseStr(str1));
console.log(reverseStr(str2));

// ****************************************************************

/*
    Recursive Binary Search
    Input: SORTED array of ints, int value
    Output: bool representing if value is found
    Recursively search to find if the value exists, do not loop over every element.
    Approach:
    Take the middle item and compare it to the given value.
    Based on that comparison, narrow your search to a particular section of the array
*/

const two_nums1 = [1, 3, 5, 6];
const two_searchNum1 = 4;
const two_expected1 = false;

const two_nums2 = [4, 5, 6, 8, 12];
const two_searchNum2 = 5;
const two_expected2 = true;

const two_nums3 = [3, 4, 6, 8, 12];
const two_searchNum3 = 3;
const two_expected3 = true;




/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */

/*
Create a function that takes in an sorted array of numbers and a num (to search for) and returns a boolean
edge case: empty array: false
base case: array of one
            - it doesn't match search num: return false
            - it matches: return true
        - compare center value to searchNum
            -matches the index currently searching: return true
            -doesn't match: go to recursive
recursive call: search either the left or right half of the array depending on the comparison
*/
function binarySearch(sortedNums, searchNum) {
    if (sortedNums.length == 0) return false
    // if (sortedNums.length == 1) {
    //     if (sortedNums[0] == searchNum) {
    //         return true
    //     } else {
    //         return false
    //     }
    // }
    let centerIndex = Math.floor(sortedNums.length/2)
    let center = sortedNums[centerIndex]
    // console.log(center);
    // console.log(sortedNums);
    if (center == searchNum) {
        return true
    } else if (sortedNums.length == 1) {
        return false
    } else if (center > searchNum){
        return binarySearch(sortedNums.slice(0,centerIndex),searchNum)
    }
    return binarySearch(sortedNums.slice(centerIndex,sortedNums.length),searchNum)
}

console.log(binarySearch(two_nums1,two_searchNum1));
console.log(binarySearch(two_nums2,two_searchNum2));
console.log(binarySearch(two_nums3,two_searchNum3));