// leetcode problem # 869. Reordered Power of 2

/*
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.


Example 1:
Input: n = 1
Output: true

Example 2:
Input: n = 10
Output: false

Constraints:
1 <= n <= 10^9
*/

/*
My solution: compare digit counts

Observation:
As n cannot be reordered such that the leading digit is 0, the reordered number cannot lose orders of magnitude
- ex: 1000 cannot be reordered to 0100 or 0010, which would've effectively lost digits
As a result, the algorithm only needs to check up to 4 values of power of two that have the same number of digits as n
- ex: if n = 5678, the algorithm only needs to check 1024, 2048, 4096, 8192
    - powers of 2 below 512 and powers of 2 above 16384 cannot be candidates for n = 5678

From the up to 4 candidates above, validity can be easily checked by comparing the number of each unique digit of the candidate to that of n
- The counts can be kept in dictionaries (objects)
- ex: 1024 has one 1, one 0, one 2, and one 4, if n also has the same counts (1024, 4201, 1204, etc), then n can be reordered into 1024
    - return true in this case
- if the digit count of n cannot match any of the 4 candidates, n cannot be reordered into a power of 2
    - return false in this case

Runtime: O(log N) where N is the input number n
- every digit counting loop only iterates based on the number of digits (up to 9 from constraints)
- in the only nested loop, the outer loop only runs up to 4 times, and inner loops are digit-dependent loops
Space: O(1), memory usage does not scale with input
-> both dictionaries can have up to 10 entries each, for the 10 unique digits in base 10
*/

/**
 * @param {number} n
 * @return {boolean}
 */
var reorderedPowerOf2 = function (n) {
    let nString = n.toString()
    let nDigits = {}

    for (let digit of nString) {
        if (nDigits.hasOwnProperty(digit)) {
            nDigits[digit] += 1
        } else {
            nDigits[digit] = 1
        }
    }

    let powerOfTwo = 1

    let minVal = Math.pow(10, nString.length - 1)

    // find the smallest candidate that has the correct number of digits
    while (powerOfTwo < minVal) {
        powerOfTwo *= 2
    }

    let pTwoDigits = {}

    // loop until the power of two value exceeds the target number of digits
    while (powerOfTwo < minVal * 10) {
        pTwoDigits = {}
        let powerOfTwoString = powerOfTwo.toString()

        for (let digit of powerOfTwoString) {
            if (pTwoDigits.hasOwnProperty(digit)) {
                pTwoDigits[digit] += 1
            } else {
                pTwoDigits[digit] = 1
            }
        }
        let valid = true
        for (let digit of Object.keys(pTwoDigits)) {
            if (pTwoDigits[digit] != nDigits[digit]) {
                valid = false
                break
            }
        }

        if (valid) {
            return true
        }

        powerOfTwo *= 2
    }

    return false

};