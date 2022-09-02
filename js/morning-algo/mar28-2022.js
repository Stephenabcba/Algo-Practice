/*
    Input: arr, callback
    Output: arr (with elements removed)
    Remove every element in the array, starting from idx 0,
    until the callback function returns true when passed the
    iterated element.
    Return an empty array if the callback never returns true
*/
//                     v
const arr1 = [1, 4, 3, 6, 9, 3];
const callback1 = (elem) => {
    return elem > 5;
};
const expected1 = [6, 9, 3];

const arr2 = [1, 4, 3, 6, 9, 3];
const callback2 = (elem) => {
    return elem > 2;
};
const expected2 = [4, 3, 6, 9, 3];

const arr3 = [1, 4, 3, 6, 9, 3];
const callback3 = (elem) => false;
const expected3 = [];

function dropIt(arr, callback) {
    while (!callback(arr[0]) && arr.length > 0) {
        for (let i = 0; i < arr.length - 1; i++) {
            let temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
        }
        arr.pop()
    }
    return arr
}

function dropIt2(arr, callback) {
    let startIndex = 0
    const arrLen = arr.length
    while (!callback(arr[startIndex]) && startIndex < arrLen) {
        startIndex++
    }
    const returnArr = []
    for (let i = startIndex; i < arrLen; i++) {
        returnArr.push(arr[i])
    }
    return returnArr
}

function dropIt3(arr, callback) {
    let foundIt = false
    return arr.filter(el => {
        if (callback(el)) {
            foundIt = true
        }
        return foundIt
    })
}



console.log(dropIt(arr1, callback1));
console.log(dropIt(arr2, callback2));
console.log(dropIt(arr3, callback3));


// console.log(dropIt2(arr1, callback1));
// console.log(dropIt2(arr2, callback2));
// console.log(dropIt2(arr3, callback3));