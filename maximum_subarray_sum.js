// The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers

// Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

// Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

// maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
// should be 6: [4, -1, 2, 1]

var maxSequence = function(arr){
    if (arr.length == 0) return 0
    let negativeCount = 0
    for (let num of arr) {
        if (num < 0) negativeCount++
    }
    if (!negativeCount) {
        let sum = 0
        for (let num of arr) {
            sum += num
        }
        return sum
    } else if (negativeCount == arr.length) {
        return 0
    }
    let maxSum = 0
    let curSum = 0
    for (let i = 0; i < arr.length; i++) {
        curSum += arr[i]
        if (curSum < 0) {
            curSum = 0
        } else if (curSum > maxSum) {
            maxSum = curSum
        }
    }
    return maxSum
}

console.log(maxSequence([]));
console.log(maxSequence([-1,-2,-3,-4,-5]));
console.log(maxSequence([1,2,3,4,5]));
console.log(maxSequence([1,-2,3,-4,5,-6,7]));
console.log(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 10]));
console.log(maxSequence([-2, 1, -3, 4, -1, 2, 1, -50, 10]));