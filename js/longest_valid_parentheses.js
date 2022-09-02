// leetcode problem #32. Longest Valid Parentheses

/*
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
*/

/*
Attempt 1: failed
Used hint of implementing a stack
Unable to account for too many opening parens
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
    const stack = []
    let max = 0
    let cur = 0
    for (let paren of s) {
        if (paren == "(") {
            stack.push(1)
        } else if (paren == ")") {
            if (stack.length > 0) {
                cur += 2
                stack.pop()
            } else {
                if (max < cur) {
                    max = cur
                }
                cur = 0
            }
        }
    }
    if (max < cur) {
        max = cur
    }
    return max
};

/*
My solution:Stack
Part 1: find the largest valid parens
- setback: unable to handle too many open parens
    - will be handled in part 2 of solution
- basic idea, consider the parens as valid if there are enough opening parens when a closing parens is found
    - in other words, the set of parens is invalid if a closing parens is found when there are no available opening parens
- a closing parens will always close the last available opening parens (if it exists)
    - if available opening parens are at indexes 0 and 4, the first closing paren found will close the paren at index 4 first.
- save the indexes of the opening parens in the stack
    - pop from the stack when a closing paren is found
- there are 2 situations when the maximum could be updated
    1. the set has been invalidated by a closing parens
    2. the end of the string has been reached
    - only update the max if the current value is actually larger than the max

Part 2: case of too many open parens
- Until the end of the string has been reached, the part 1 of solution cannot decide whether there are too many unmatched open parentheses
    - it may consider a set of parens as valid, even though it is not
- Part 2 of solution breaks the set of parens into segments, broken up by the unmatched open parentheses
    - each segment is a valid set of parens
- The stack holds the indexes of all unmatched open parens, sorted from smallest to largest
    - work from the back to the front, breaking the segments one by one
- The longest valid set of parens could be before the earliest unmatched open parens
    - update the value found in part 1 for this case
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
    const stack = []
    let max = 0
    let cur = 0

    // calculate the largest set of valid parens
    // handle the open parens problem later
    for (let i = 0; i < s.length; i++) {
        let paren = s[i]
        if (paren == "(") {
            stack.push(i)
        } else if (paren == ")") {
            if (stack.length > 0) {
                cur += 2
                stack.pop()
            } else { // too many closing parens, reset the count
                if (max < cur) {
                    max = cur
                }
                cur = 0
            }
        }
    }

    // handling too many opening parens
    if (stack.length > 0) {
        let idx = s.length - 1
        while (stack.length > 0) {
            let last = stack.pop()
            // the length of a valid segment is the difference between the current index and the last unmatched open parens
            let segment = idx - last
            // update the number of "valid" parens found in part 1
            // the answer could be the segment before the earliest unmatched open parens
            cur -= segment
            // don't count the unmatched open parens in the next set
            idx = last - 1
            if (max < segment) {
                max = segment
            }
        }
    }

    // if the end of string is reached, update the maximum if necessary
    if (max < cur) {
        max = cur
    }
    return max
};

/*
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0
*/

/*
Additional test cases:
Too many opening parens:
"()(()(()(()(()(()"
"()(()"
The first segment is the largest valid parens:
"(())("
"(())(()(()"
*/


/*
Dynamic Programming solution from leetcode
the dp array saves the length of the current set of valid parens at index i
a valid set of parens always ends with ), so ignore ( when iterating
always check if the index is in bounds before attempting to access the value of the array

( has a dp value of 0, because no valid set of parens ends with (

if ( is before a ), then the length of the set is 2 + dp[i-2]
if ) is before a ), check if s[i - dp[i-1] -1] is a (
    if it is, the set is still valid, add 2 to the set
        the sum is the current set of (((())) + the values before the nested parens (could be 0)

at every ) check if the updated dp value is a new maximum
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
    let maxAns = 0
    let dp = []
    for (let i = 0; i < s.length; i++) {
        dp.push(0)
    }

    for (let i = 1; i < s.length; i++) {
        if (s[i] == ")") {
            if (s[i - 1] == "(") {
                dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2
            } else if (i - dp[i - 1] > 0 && s[i - dp[i - 1] - 1] == "(") {
                dp = dp[i - 1] + ((i - dp[i - 1]) >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2
            }
            maxAns = Math.max(maxAns, dp[i])
        }
    }

    return maxAns
};

/*
Leetcode solution stack improvement:
instead of the 2 part process, the current counter length is just the difference between the current position and the top of the stack

modifications:
initialize the stack with -1
pop every time a ) is reached
if the stack is empty after popping, push the location of )
if the stack is not empty after popping, the valid parens is from current position to top of the stack
    - update max if necessary
*/