// leetcode problem # 923. 3Sum With Multiplicity

/*
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300

Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.


Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
*/

/*
My solution (incomplete)
- uses combination formula for the case where all three numbers are the same
- seems to extend into unnecessary complication going forward
*/

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var threeSumMulti = function (arr, target) {
    const numIndexes = {}
    for (let i = 0; i < arr.length; i++) {
        if (!numIndexes.hasOwnProperty(arr[i])) {
            numIndexes[arr[i]] = []
        }
        numIndexes[arr[i]].push(i)
    }
    let ans = 0
    for (let firstNum in numIndexes) {
        if (firstNum > target) {
            continue
        }

        for (let secondNum = 0; secondNum <= target - firstNum; secondNum++) {
            const thirdNum = target - firstNum - secondNum
            if ((!numIndexes.hasOwnProperty(secondNum)) || (!numIndexes.hasOwnProperty(thirdNum))) {
                continue
            }
            if ((firstNum == secondNum) && (firstNum == thirdNum)) {
                const threeNumsLength = numIndexes[firstNum].length
                if (threeNumsLength < 3) {
                    continue
                }
                ans += threeNumsLength * (threeNumsLength - 1) * (threeNumsLength - 2) / 6
            }
        }
    }
    return ans
};

/*
Solution from leetcode discussion by zayne-siew (originally in Python)
Key ideas:
- i < j < k requirement is for indexes only ensures that the indexes used in any triplet are unique within the triplet
    - the requirement can be rewritten as: i != j != k
    - ex: (i,i,i) and (i,i,j) are invalid
    - rewriting any triplet (i,j,k) as (k,j,i) or (j,i,k) does not change the solution
        - all of these count as one solution
    - thus, sorting the array is allowed without affecting the solution
- the problem can be broken down into a 2-sum problem of j and k for every value of i
    - sort the array first so that the 2-sum problem takes linear time
    - must account for all combinations of i, j, and k
        - use the combination formula for n choose 2 and n choose 3 as needed
            - n choose 2: n * (n-1) / 2
            - n choose 3: n * (n-1) * (n-2) / 6
Implementation:
- sort the array from smallest to greatest
- build a count object (dictionary) that holds the number of occurances for each number
- iterate through all unique values of the array (firstNum)
    - **firstNum, secondNum and thirdNum are indexes within the array**
    - after each full iteration, firstNum is incremented by the count of its value to move to the next unique number's index
    - calculate the 2-sum for all numbers between the indexes [firstnum, arr.length-1]
        - if written in proper format, the 2-sum should be looking for a sum of target - arr[firstNum]
            - however, summing arr[firstNum], arr[secondNum], and arr[thirdNum] and comparing to target yields the same result
        - move secondNum and thirdNum according to 2-sum algorithm
            - if the sum is too small, increase secondNum
            - if the sum is too large, decrease thirdNum
        - if the sum matches, account for all combinations of firstNum, secondNum, and thirdNum
            - case 1: the value at all 3 indexes are distinct
                - the combination is val1 * val2 * val3
            - case 2: the two of the 3 values are distinct (1 value occurred twice)
                - the combination is (repeatedVal * (repeatedVal - 1) / 2) * otherVal
                    - (N choose 2) * nonRepeatedVal
                - the repeated val can either be firstVal with secondVal or secondVal with thirdVal
            - case 3: only 1 distinct value (1 value occured 3 times)
                - the combination is (repeatedVal * (repeatedVal - 1) * (repeatedVal - 2)) / 6
                    - N choose 3
            - in all cases where sum == target, secondVal is incremented by count(arr[secondVal]) and thirdVal is decremented by count(arr[thirdVal])
Runtime: O(N^2): iteration of firstVal is O(N), nested with sorted 2-sum (also O(N)), where N is length of the array
    - technically, the runtime might be O(N * logN) for the sorting algorithm
        - with how the nested while loops increment/decrement, the loops could have a runtime of O(M^2), which could be lower than O(N*logN) for large N
            - the outer loops runs at most M times, where M is the range of array (101 in this case)
            - the inner loop currently runs up to N times per iteration, but could be refactored to run M times, where M is 101
                - the 2-sum search for target could increment by arr[secondNum], thus only up to 101 times
Space: O(M): the count object scales with M, which is the possible values of the array (101 in this case)
    - the sorting algorithm could've used extra space
*/

var threeSumMulti2 = function (arr, target) {
    // sort the array
    arr.sort((a, b) => a - b)
    // build the count object
    const numCount = {}
    for (let num of arr) {
        if (!numCount.hasOwnProperty(num)) {
            numCount[num] = 1
        } else {
            numCount[num] += 1
        }
    }
    // 
    let ans = 0
    const arrLen = arr.length
    let firstNum = 0
    while (firstNum < arrLen) {
        let secondNum = firstNum
        let thirdNum = arrLen - 1
        while (secondNum < thirdNum) {
            if (arr[firstNum] + arr[secondNum] + arr[thirdNum] < target) { // sum too small, increase secondNum
                secondNum++
            } else if (arr[firstNum] + arr[secondNum] + arr[thirdNum] > target) { // sum too large, decrease secondNum
                thirdNum--
            } else { // (arr[firstNum] + arr[secondNum] + arr[thirdNum] == target)
                if (arr[firstNum] != arr[secondNum] && arr[firstNum] != arr[thirdNum] && arr[secondNum] != arr[thirdNum]) { // all three values are distinct
                    ans += numCount[arr[firstNum]] * numCount[arr[secondNum]] * numCount[arr[thirdNum]]
                } else if (arr[firstNum] == arr[secondNum] && arr[firstNum] != arr[thirdNum]) { // the first two values are identical
                    ans += numCount[arr[firstNum]] * (numCount[arr[firstNum]] - 1) * numCount[arr[thirdNum]] / 2
                } else if (arr[firstNum] !== arr[secondNum] && arr[secondNum] == arr[thirdNum]) { // the last two values are identical
                    ans += numCount[arr[firstNum]] * numCount[arr[secondNum]] * (numCount[arr[secondNum]] - 1) / 2
                } else { // all 3 values are identical
                    ans += numCount[arr[firstNum]] * (numCount[arr[firstNum]] - 1) * (numCount[arr[firstNum]] - 2) / 6
                }
                secondNum += numCount[arr[secondNum]]
                thirdNum -= numCount[arr[thirdNum]]
            }
        }
        firstNum += numCount[arr[firstNum]]
    }
    return ans % 1000000007
};



/*
Top solution from leetcode solution in both memory and runtime
Observations:
- the algorithm does not sort the array
- since the possible values range is small ([0,100]), the count object can be instantiated as an array where count[0] is the number of times that 0 has occurred
- the 2-sum search condition is different
Implementation:
- create a count array
    - instead of pre-populating it in the previous solution, this array acts like a "seen" array
- iterate through the entire array (the value num1 is arr[i])
    - perform a 2-sum search for all values "seen" up to the current iteration
        - the search is done on the range of the array, which is [0,100]
        - left and right are values between 0 and 100
            - can also be denoted as num2 and num3
        - the sum is num1 + left + right
        - skip all values not currently "seen"
            - count[num] == 0
        - when the sum matches target:
            - case 1: left matches right (1 repeated value)
                - utilize N choose 2
                - combination does not use the same element twice
                    - num2 and num3 will not be the same element (j != k)
                        - if the value only occured once, 1 choose 2 is 0
            - case 2: left != right
                - the counts simply multiply together
    - add num1 to the "seen" count array
        - as the number is added after the 2-sum search, i is not present in the 2-sum search
            -> meets i != j != k requirement
    - ** the case of 3 identical values is broken up into a sum of multiple 2 identical values

Runtime: O(N*M) - the outer loop runs O(N) times, the inner loop runs up to O(M) times
    - N is the length of the array, M is the range of the array (101 in this case)
Space: O(M) - the count array size depends on range of the array (101 in this case)

Improvements: eliminates the use of sorting algorithm
*/

/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var threeSumMulti3 = function (arr, target) {
    const MOD = 1e9 + 7;
    const n = arr.length;
    const count = new Array(101).fill(0);

    let res = 0;

    // loop through all values in the array
    for (let i = 0; i < n; ++i) {
        const num = arr[i];

        // 2-sum search
        let left = 0;
        let right = 100;

        while (left <= right) { // despite the nested while loops, this while loop runs up to 101 times per iteration
            // skip all values not currently "seen"
            while (left <= right && count[left] == 0) left++;
            while (left <= right && count[right] == 0) right--;

            // if the previous 2 while loops have moved the indexes past the complete condition, the search is complete
            if (left > right) break;

            const sum = num + left + right;

            // sum matches target
            if (sum === target) {
                if (left == right) {
                    res = (res + (count[left] * (count[left] - 1)) / 2) % MOD;
                }
                else {
                    res = (res + (count[left] * count[right]) % MOD) % MOD;
                }
                left++;
                right--;
            } // sum too small
            else if (sum < target) {
                left++;
            } // sum too large
            else {
                right--;
            }
        }

        count[num]++;
    }


    return res;
};