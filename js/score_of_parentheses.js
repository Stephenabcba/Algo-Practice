// leetcode problem #856. Score of Parentheses
/*
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
*/


/*
my solution:
**observations:**
O1. every opening parentheses "(" marks the start of potential addition
    O1.1 either the following parenthesis group is alone, or some addition is done with all parentheses in the same "level"
    O1.2 a chain of consecutive opening parentheses denotes multiplication
O2. the first closing parentheses ")" in a consecutive chain of closing parenthesis is always marking a "()", which has a value of 1
    O2.1 all remaining closing parentheses in the consecutive chain are always matching with the opening parentheses from O1.2, multiplying enclosed components by 2
**variables:**
- curScore: integer keeping track of the score of in the current "level"
    - as a balanced parenthesis ends on the top "level", curScore also holds the total score at the end of the function
- multiply: a flag that decides whether the next closing parentheses should multiply (true) or add (false)
- openParenCount: keeps count of number of open parens for the current "level"
    - when it is 0, the current position is the same "level" as the state saved at the top of the stack
- workStack: saves the current state as a layer in the stack, each state/layer keeps track of the three variables described above
    - every layer in the stack also denotes a new "level" has been saved
    - used to retain information while the states are reset to evaluate other elements in the "level"
**actual logic:**
L1. for every opening parentheses:
    L1.1 save the current status in a stack and start evaluating for the next parentheses to come
        - this prepares the coming parentheses in the same "level" as described in O1.1
        - reset all trackers and flags
    L1.2 if the current working "level" has no values, it does not need to be pushed to the stack
    L1.3 however, consecutive opening parentheses chains need to be tracked for O1.2 and O2.1
L2. for every closing parentheses, distinguish between O2 and O2.1 with a flag
    L2.1 if the flag is true, multiply (O2.1)
    L2.2 if the flag is false, set the value to 1 (O2)
        - all previous values should've been saved and re-initialized in L1.1
    L2.3 decrement the number of consecutive opening parentheses managed in L1.3
        L2.3.1 if the number has reached 0, operations have been complete for the element, and the current position is on the same "level" as the status previously saved in L1.1 
            - the previous status can be retrieved and merged with the current status
            - as both statuses are on the same "level", their scores can be summed
            - all previous open parentheses counts are carried over
            - the flag is also carried over
L3. for every character of the input string, L1 and L2 are mutually exclusive, and depend on previous values in the string
    - the operation can be done in a single for-loop with linear time
*/
/**
 * @param {string} s
 * @return {number}
 */
var scoreOfParentheses = function (s) {
    let curScore = 0
    let multiply = false
    let openParenCount = 0
    let workStack = []
    for (let i = 0; i < s.length; i++) {
        if (s[i] == ")") {
            if (multiply) {
                curScore *= 2
            } else {
                curScore = 1
                multiply = true
            }
            openParenCount--
            if (openParenCount == 0) {
                if (workStack.length > 0) {
                    let prevWork = workStack.pop()
                    curScore += prevWork.score
                    openParenCount = prevWork.parenCount
                    multiply = prevWork.multiply
                } else {
                    break
                }
            }

        } else {
            if (curScore == 0) {
                openParenCount++
            } else {
                workStack.push({ score: curScore, parenCount: openParenCount, multiply: multiply })
                curScore = 0
                openParenCount = 1
            }
            multiply = false
        }
    }
    return curScore
};

// console.log(scoreOfParentheses("(()()()()()()()()()())"))

// Solution from leetcode: count cores
/*
**theory**
an empty parentheses pair "()" is defined as a "core", and has a value of 1 by problem definition
all additional parentheses around the core will eventually multiply the core by 2 for each pair
    the number of pairs around the core is defined as "balance"
the actual score of any core is 1 * 2 ^ balance, and is the same as bit-shifting the value of core by the value of balance
the total score of any parenthesis string is the sum of actual scores for all cores in the string


**implementation**
for every opening parentheses "(", increase balance by 1
for every closing parentheses ")", decrease balance by 1
    if the previous character is an opening parentheses, the current pair is a core
        calculate the actual score of the core and add to the total score
time complexity: O(N)
    the operation can be done with one iteration through the entire length of the string
space complexity: O(1)
    the only variables are the total score, the balance, and the iterating index, which are numbers that take up constant space


example: () is a core, with balance of 0
        (()) contains a core, with balance of 1, which gives the core an actual score of 2
*/
const scoreOfParentheses2 = (s) => {
    let ans = 0
    let bal = 0
    for (let i = 0; i < s.length; i++) {
        if (s[i] == "(") {
            bal++
        } else {
            bal--
            if (s[i - 1] == "(") {
                ans += 1 << bal
            }
        }
    }
    return ans
}

console.log(scoreOfParentheses2("(()()()()()()()()()())"))