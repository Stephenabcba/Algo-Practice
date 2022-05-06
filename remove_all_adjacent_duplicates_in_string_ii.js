// leetcode problem #1209. Remove All Adjacent Duplicates in String II

/*
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.


Constraints:

1 <= s.length <= 10^5
2 <= k <= 10^4
s only contains lower case English letters.
*/


/*
Attempt 1: runtime exceeded.
Bruteforce searching and slicing the string
*/

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function (s, k) {
    let hasRemoved = true

    while (hasRemoved) {
        hasRemoved = false
        let index = 0
        let prevLetter = ""
        let startIndex = 0
        let req = k - 1
        while (index < s.length) {
            if (s[index] == prevLetter) {
                req--
            } else {
                req = k - 1
                prevLetter = s[index]
                startIndex = index
            }
            if (req == 0) {
                s = s.slice(0, startIndex) + s.slice(index + 1)
                hasRemoved = true
                break
            }
            index++
        }
    }
    return s
};

/*
My solution: idea from leetcode hints
hint1: 
Use a stack to store the characters, when there are k same characters, delete them.
hint2:
To make it more efficient, use a pair to store the value and the count of each character.

Using these 2 hints, a solution is created with a stack
part 1:
- an array is used as a stack to store the previously seen letters
    - each item in the stack is another array, holding the letter and the consecutive number of times it has occurred
- if the letter is the same as the top of the stack, increase the count
- if the letter is different from the top of the stack, push it to the stack with a count of 1
- if the top of the stack has count of k, pop from the stack
part 2:
- after part 1, the stack only contains the letters that should be returned
- starting from the front (not LIFO order of the stack) of the array, rebuild the string using the letters and their count
- return the rebuilt string

Runtime: O(N) for the stack and rebuilding the string
    - even though the rebuilding involves nested for-loops, in the worst case the operation only runs N times,
        which rebuilds the original string.
Space: O(N) for the stack and the return array used to rebuild the string
*/

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var removeDuplicates = function (s, k) {
    // build the stack
    let stack = []
    for (let letter of s) {
        if (stack.length > 0 && letter == stack[stack.length - 1][0]) {
            stack[stack.length - 1][1]++
        } else {
            stack.push([letter, 1])
        }
        if (stack.length > 0 && stack[stack.length - 1][1] == k) { // if the top of the stack has k characters, pop it.
            stack.pop()
        }
    }

    // rebuild the string from the stack
    let returnArr = []
    for (let letterPair of stack) {
        for (let i = 0; i < letterPair[1]; i++) {
            returnArr.push(letterPair[0])
        }
    }
    return returnArr.join("")
};


/*
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
*/