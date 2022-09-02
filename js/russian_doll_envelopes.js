// leetcode problem # 354. Russian Doll Envelopes

/*
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.


Constraints:

1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= w_i, h_i <= 10^5
*/

/*
My incomplete solution: 
Sort the envelopes based on its largest side (regardless of width or height)
- this way, an envelope on the right cannot fit into an envelope on the left
Attempt to apply dp and build up the chain one by one
- try to fit a smaller envelope with the longest chain into the current envelope

Shortcoming: there is no fast way of determining which envelope is the best one to continue the chain
The solution has a O(N^2) runtime.
Another sorting condition may be needed.
*/

/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function (envelopes) {
    envelopes.sort((a, b) => {
        let maxA = a[0]
        let maxB = b[0]
        let minA = a[1]
        let minB = b[1]

        if (a[0] < a[1]) {
            maxA = a[1]
            minA = a[0]
        }

        if (b[0] < b[1]) {
            maxB = b[1]
            minB = b[0]
        }

        if (maxA != maxB) {
            return maxA - maxB
        } else {
            return minA - minB
        }
    })

    const dp = []
    for (let i = 0; i < envelopes.length; i++) {
        dp.push(1)
    }

    let outerMax = 0
    for (let i = 1; i < envelopes.length; i++) {
        let innerMax = 0
        for (let j = 0; j < i; j++) {
            if (envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]) {
                if (dp[j] > innerMax) {
                    innerMax = dp[j]
                }
            }
        }
        innerMax += 1
        dp[i] = innerMax
        if (innerMax > outerMax) {
            outerMax = innerMax
        }
    }
    return outerMax
};


/*
Solution from leetcode discussion by sahil_d70 (originally written in C++)
The idea of binary search is further emphasized in discussion by rhythm_varshney

*** the explanation assumes that the data is given in [width, height] format. ***
    - the actual solution does not matter whether width or height comes first
    - the distinction only serves to make explanation clearer

2-step process:
1. Sort the envelopes array
    - sort condition: first sort based on width(ascending), then by height (descending)
        - only sort by height if the width of 2 envelopes are the same
    - result: 
        - the width will be in non-decreasing order from left to right
        - if the width is equal, the height will be in non-increasing order from left to right
    // e.g. -> env => (3,8) (4,5) (2,1) (2,6) (7,8) (5,3) (5,7)
    // sorted version => (2,6) (2,1) (3,8) (4,5) (5,7) (5,3) (7,8)
2. Find the longest increasing subsequence (lis) of heights (building the "Russian Doll")
    - iterate through each envelope in the sorted array of envelopes
        - for each height of the envelope, search for the first index in the lis that has a larger height
            - it is possible that the current height is the largest height
        case 1: if the current height is the largest height, add it to the back of the LIS array
            - a new envelope now fits over all the previous chain of envelopes
        - otherwise, replace the height in the LIS array at the found index with the current height
            - this enables more envelopes to be added potentially.
            - the envelope with larger dimensions is replaced with a smaller envelope, enabling more envelopes to encapsule it.
    - the lis will be maintained such that it will always be sorted
        - binary search can be utilized for improved runtime
    - with the way the array is sorted, envelopes of the same width will not add to the length of the lis
        - at best, it will decrease values in the lis

The length of the lis is the longest chain of envelopes that meet the condition.

Runtime: O(N * LogN)
- The sorting algorithm likely uses O(N * LogN) time
- Part 2 of the solution iterates through every item O(N) * binary search through the LIS array O(LogN)
** N is the length of the envelopes array.

Space: O(N) 
- The LIS array could be the entire envelopes array
- The sorting algorithm may also take up to O(N) space
** N is the length of the envelopes array.
*/

/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function (envelopes) {
    let n = envelopes.length

    envelopes.sort((a, b) => {
        if (a[0] == b[0]) {
            return b[1] - a[1]
        } else {
            return a[0] - b[0]
        }
    })

    // initialize the longest increasing subsequence
    const lis = []

    for (let i = 0; i < n; i++) {
        let element = envelopes[i][1]

        let idx = 0

        // this should be implemented with a binary search
        // the original used lower_bound() function, which probably used binary search
        while (idx < lis.length && lis[idx] < element) {
            idx++
        }

        if (idx >= lis.length) { // if the element is larger than all items in the LIS, add it to the LIS
            lis.push(element)
        } else { // otherwise, replace the first value larger than the element
            lis[idx] = element
        }

    }

    return lis.length
};



/*

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
*/