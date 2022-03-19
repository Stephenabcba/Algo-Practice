// leetcode problem #895. Maximum Frequency Stack
/*
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
*/

/*
My attempt (failed due to slow run time)
idea: 
implement the stack as a singly linked list (SLL)
also keep an object/dictionary to keep track of frequency for each unique value in the stack
implementation:
- when pushing:
    - push the value to the stack as usual for a SLL stack
    - increment the frequency count for the value in the dictionary
- when popping:
    - find the max frequency value of the frequency dictionary
    - starting from the top of the stack, move down until the frequency of current node (from the dictionary) matches the max frequency
    - when found:
        - pop the value
        - decrement the value's frequency count
    - return the popped value

Problem:
    - to search for the max frequency in the object when popping, the function must search through every value in the dictionary
        - this results in O(N^2) runtime for popping N items after pushing N items

Commented portion in the code were attempts to create other data structures to minimize runtime for finding the max frequency
*/
var FreqStack = function () {
    this.top = null
    this.freq = {}
    // this.maxFreq = 0
    // this.maxFreqCount = 0
    // this.maxFreqObj = null
};

/** 
 * @param {number} val
 * @return {void}
 */
FreqStack.prototype.push = function (val) {
    this.freq[val] = this.freq.hasOwnProperty(val) ? this.freq[val] + 1 : 1
    const curNumFreq = this.freq[val]
    if (this.top === null) {
        this.top = { val: val, next: null }
    } else {
        const next = this.top
        this.top = { val, next: next }
    }
    return null
    // attempts to make popping functionality faster
    // if (this.freq[val] > this.maxFreq) {
    //     this.maxFreq = this.freq[val]
    //     this.maxFreqCount = 1
    // } else if (this.freq[val] == this.maxFreq) {
    //     this.maxFreqCount++
    // }
    // if (this.maxFreqObj === null) {
    //     this.maxFreqObj = {val: curNumFreq, count:1, next:null}
    // } else if (curNumFreq > this.maxFreqObj.val) {
    //     if (this.maxFreqObj.count == 1) {
    //         this.maxFreqObj.val++
    //     } else {
    //         this.maxFreqObj.count--
    //         const newMaxFreq = {val: curNumFreq, count:1, next:this.maxFreqObj}
    //         this.maxFreqObj = newMaxFreq
    //     }
    // }else if (curNumFreq == this.maxFreqObj.val) {
    //     this.maxFreqObj.count++
    //     if (curNumFreq > 1) {
    //         this.maxFreqObj.next.val--
    //     }
    // } else {
    //     // handle maxFrequency SLL if curNumFreq is lower than max
    // }
};

/**
 * @return {number}
 */
FreqStack.prototype.pop = function () {
    let maxFreq = 0
    for (let keyNum of Object.keys(this.freq)) {
        if (this.freq[keyNum] > maxFreq) {
            maxFreq = this.freq[keyNum]
        }
    }
    const dummyNode = { next: this.top }
    let prevNode = dummyNode
    let runner = this.top
    while (runner !== null) {
        if (this.freq[runner.val] == maxFreq) {
            const popped = runner
            prevNode.next = runner.next
            this.top = dummyNode.next
            this.freq[runner.val] = this.freq[runner.val] - 1
            return popped.val
            // if (this.maxFreqObj.count > 1) {
            //     this.maxFreqObj.count--
            // } else {
            //     this.maxFreqObj.val --
            //     if (this.maxFreqObj.val == 0) {
            //         this.maxFreqObj = null
            //     } else if (this.maxFreqObj.next && this.maxFreqObj.val == this.maxFreqObj.next.val) {
            //         this.maxFreqObj = this.maxFreqObj.next
            //         this.maxFreqObj.count++
            //     }
            // }
        } else {
            prevNode = runner
            runner = runner.next
        }
    }
    return -1
};

/** 
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */

/*
Solution from Leetcode: Stacks of Stacks
(originally shown in java and python)
Idea:
Keep a frequency dictionary of all unique pushed values
Additionally, keep track of when the value was pushed at the current frequency
    - the last pushed value of a given frequency should be popped first
    - this information can be saved to a stack
        - as such, the resulting data structure is a tiered collection of stacks, or a stack of stacks
As the values with the highest frequency should be popped first, keep track of the max frequency of the frequency dictionary at all times

if we push the values [2,5,7,5,7,4,5] in the given order, the resulting data structure looks like:
frequency 3: 5
frequency 2: 5,7
frequency 1: 2,5,7,4
currently, the max frequency is 3.

if all values are popped, the popped values will be in the following order: [5,7,5,4,7,5,2]
- the popped value is always the last pushed value (highest index) at the highest possible frequency
- the first popped value is the 5 at frequency 3, then the 7 at frequency 2, and so on

Implementation
- the outer stack is implemented as a dictionary / object, which makes insert and access to any given frequency constant time
- the inner stack is currently written as a default javascript array with .push() and .pop() functionality for convenience
    - performance improvement could exist for using a simpler implementation of stacks such as a singly-linked list
I1. note: if the value v exists in the stack at frequency f, v is also present in the stacks for (f-1), (f-2),...,1
    - the frequency of v can be also expressed as (f-1) + 1, (f-2) + 2, etc.
    - from the example above: since 5 exists in the stack for frequency 3, 5 also exists in the stacks for frequencies 2 and 1
I2. when pushing:
    - I2.1 increment the frequency dictionary for the inserted value
    - I2.2 update the max frequency if needed
    - I2.3 push the current value into the inner stack for the current frequency
        - initialize the inner stack as required
        - excluding all popped instances, the first instance is inserted at frequency 1, second at frequency 2, and so on
            - this ensures that (I1) is fulfilled
            - if the third instance is popped, the next instance of the same value pushed will still be the third instance
I3. when popping:
    - I3.1 pop a value from the stack at max frequency
        - max frequency is managed by (I2.2) and (I3.3)
        - (I3.3) additionally ensures that there is at least 1 value in the stack at max frequency
            - this assumes that pop() is not executed when the stack is completely empty
    - I3.2 decrement the frequency dictionary for the popped value
    - I3.3 if the inner stack at max frequency is now empty, decrement max frequency as well
        - as explained in I1 and implemented in (I2.3), there must be at least 1 value in the stack in the decremented max frequency
    - I3.4 return the popped value

Performance:
Runtime: O(N) for N push and pop operations
    - each singular push or pop operation can be executed in constant time
Memory Usage: O(N) for N push and pop operations
    - the frequency dictionary could take up to O(N) spaces if N unique values were pushed
    - the total count of numbers in the stack of stacks is O(N) for N pushed values, if no values have been popped
*/


var FreqStack = function () {
    this.freq = {}
    this.group = {}
    this.maxFreq = 0
};

/** 
 * @param {number} val
 * @return {void}
 */
FreqStack.prototype.push = function (val) {
    // modify frequency dict
    const curFreq = this.freq.hasOwnProperty(val) ? this.freq[val] + 1 : 1
    this.freq[val] = curFreq

    // if needed, update maxFrequency
    if (curFreq > this.maxFreq) {
        this.maxFreq = curFreq
    }

    // if the stack array for the current frequency doesn't exist, initialize it 
    if (!this.group.hasOwnProperty(curFreq)) {
        this.group[curFreq] = []
    }
    // push the value into the stack array at current frequency of val
    this.group[curFreq].push(val)
};

/**
 * @return {number}
 */
FreqStack.prototype.pop = function () {
    const poppedVal = this.group[this.maxFreq].pop()
    this.freq[poppedVal]--
    if (this.group[this.maxFreq].length == 0) {
        this.maxFreq--
    }
    return poppedVal
};

/** 
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */