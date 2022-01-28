/* 
    Given an int to represent how much change is needed
    calculate the fewest number of coins needed to create that change,
    using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) {
    let coinsObj = {}
    // can also write coinsValue as list of dictionaries
    // coinsValue = [{name:'quarter',amt:25}]
    let coinsValue = [['quarter',25],['dime',10],['nickel',5],['penny',1]]
    for (let i = 0; i < coinsValue.length; i++) {
        if (cents >= coinsValue[i][1]) {
            coinsObj[coinsValue[i][0]] = Math.floor(cents/coinsValue[i][1])
        }
        cents = cents % coinsValue[i][1]
    }
    return coinsObj
}

console.log(fewestCoinChange(cents1));
console.log(fewestCoinChange(cents2));
console.log(fewestCoinChange(cents3));
console.log(fewestCoinChange(cents4));
console.log("************************");

/* 
    Missing Value
    You are given an array of length N that contains, in no particular order,
    integers from 0 to N . One integer value is missing.
    Quickly determine and return the missing value.
*/

const two_nums1 = [3, 0, 1];
const two_expected1 = 2;

const two_nums2 = [3, 0, 1, 2];
const two_expected2 = null;
// Explanation: nothing is missing

/* 
    Bonus: now the lowest value can now be any integer (including negatives),
    instead of always being 0. 
*/

const two_nums3 = [2, -4, 0, -3, -2, 1];
const two_expected3 = -1;

const two_nums4 = [5, 2, 7, 8, 4, 9, 3];
const two_expected4 = 6;

/**
 * Determines what the missing int is in the given unordered array of ints
 *    which spans from 0 to N where only one int is missing. With this missing
 *    int, a consecutive sequence of ints could be formed from the array.
 * Bonus: Given ints can span from N to M (start and end anywhere).
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} unorderedNums
 * @returns {number|null} The missing integer needed to be able to form an unbroken
 *    consecutive set of integers from the given array or null if none is missing.
 */
function missingValue(unorderedNums) {
    let arrLenSum = 0
    let arrSum = 0
    let arrMin = unorderedNums[0]
    for (let i = 0; i < unorderedNums.length; i++) {
        if (unorderedNums[i] < arrMin)
            arrMin = unorderedNums[i]
    }

    for (let j = 0; j < unorderedNums.length; j++){
        arrLenSum += j + arrMin
        arrSum += unorderedNums[j]
    }
    if (arrSum == arrLenSum)
        return null
    return arrLenSum + unorderedNums.length + arrMin - arrSum
}

console.log(missingValue(two_nums1));
console.log(missingValue(two_nums2));
console.log(missingValue(two_nums3));
console.log(missingValue(two_nums4));