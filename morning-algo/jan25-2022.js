/* 
    Given two arrays, interleave them into one new array.
    The arrays may be different lengths. The extra items should be added to the
    back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 */
function interleaveArrays(arr1, arr2) {
    var i = 0
    var returnArr = []
    while (i < arr1.length || i < arr2.length) {
        if (i < arr1.length) {
            returnArr.push(arr1[i])
        }
        if (i < arr2.length) {
            returnArr.push(arr2[i])
        }
        i++
    }
    return returnArr
}
console.log(interleaveArrays(arrA1,arrB1));
console.log(interleaveArrays(arrA2,arrB2));
console.log(interleaveArrays(arrA3,arrB3));
console.log(interleaveArrays(arrA4,arrB4));

/* 
    Array: Binary Search (non recursive)
    Given a sorted array and a value, return whether the array contains that value.
    Do not sequentially iterate the array. Instead, ‘divide and conquer’,
    taking advantage of the fact that the array is sorted .
    Bonus (alumni interview): 
        first complete it without the bonus, because they ask for additions
        after the initial algo is complete
        return how many times the given number occurs
*/




const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const two_expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const two_expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const two_expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const two_expected4 = 4;


// 1,10,100,1000,10000,100000


/*
PSEUDOCODE
create a function that takes in an array and an integer (search value)
  create a dictionary/object of already searched index
start and end index variables
LOOP:
    find the middle by taking the average of start and end index and take the floor of it (truncate decimal)
        // if the middle index is already in the searched object, return false
        if start equals end and value at that index is not search value, return false
    compare the value at the middle index and compare with the search value
        - case 1: equal: return true
        - case 2: search value is greater: repeat search to the right ->move start index to middle + 1
        - case 3: search value is lower: repeat search to the left -> move end index to middle - 1
*/

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {
    var start = 0
    var end = sortedNums.length - 1
    var middle = Math.floor((start + end) /2)
    var found = false
    while (end >= start) {
        // console.log(sortedNums[middle]);
        if (sortedNums[middle] == searchNum) {
            found = true
            break
        } else if (sortedNums[middle] > searchNum) {
            end = middle - 1
        } else { // searchNum is greater
            start = middle + 1
        }
        middle = Math.floor((start + end) /2)
    }
    if (!found) {
        return false
    }
    // find all appearances
    var appearance = 1
    var i = middle + 1
    while(sortedNums[i] == searchNum) {
        appearance++
        i++
    }
    var j = middle - 1
    while(sortedNums[j] == searchNum) {
        appearance++
        j--
    }
    return appearance
}
console.log(binarySearch(nums1,searchNum1));
console.log(binarySearch(nums2,searchNum2));
console.log(binarySearch(nums3,searchNum3));
console.log(binarySearch(nums4,searchNum4));