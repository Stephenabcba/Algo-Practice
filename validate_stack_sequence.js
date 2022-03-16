// leetcode problem #946. Validate Stack Sequences

/*
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
*/

/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
    // initialize variables
    // make a copy of the pushed array in reverse for easy of popping later
    const availableNumsReversed = [...pushed.reverse()]
    const curStack = []

    // repeat for every value in the pop index
    for (let popIndex = 0; popIndex < popped.length; popIndex++) {
        // if the top of the stack does not match what we want to pop, keep pushing values into the stack
        while (curStack[curStack.length - 1] != popped[popIndex]) {
            // if we have nothing to push but also cannot pop from the top, the order is invalid
            if (availableNumsReversed.length == 0) {
                return false
            }
            curStack.push(availableNumsReversed.pop())
        }
        // here, we know that the top of the stack holds what we want to pop since the while loop exited
        // pop the value and continue on to the next loop
        curStack.pop()
    }
    return true
};

const pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
const pushed2 = [5, 4, 3, 2, 1], popped2 = [4, 5, 3, 2, 1]
const pushed3 = [1, 2, 3, 4, 5], popped3 = [4, 3, 5, 1, 2]

validateStackSequences(pushed, popped)

/*
Solution from leetcode: greedy approach
As we push values from the pushed array to our stack, pop as many values that match as possible
This utilizes stack's property to only be able to pop from the top of the stack
*/

function validateStackSeq2(pushed, popped) {
    // initialize
    let j = 0
    const stack = []
    //for each value in pushed array:
    for (let pushVal of pushed) {
        // push the value
        stack.push(pushVal)
        // as long as we have values at top of the stack that we want to pop, pop the value
        while (stack && j < popped.length && stack[stack.length - 1] == popped[j]) {
            stack.pop()
            j++
        }
    }
    // if j is at popped.length, we have successfully popped all values from the stack
    return j == popped.length
}