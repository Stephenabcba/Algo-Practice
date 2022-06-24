// leetcode problem # 1354. Construct Target Array With Multiple Sums

/*
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.


Example 1:
Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:
Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:
Input: target = [8,5]
Output: true

Constraints:

n == target.length
1 <= n <= 5 * 10^4
1 <= target[i] <= 10^9
*/

/*
My solution after utilizing leetcode hints:
Work backwards from the target array towards an array of all 1's

when working backwards, the largest value can be replaced by (largestValue - sumOfRemainingValues)
    - if the sum of remaining values is larger than the largest value, the target array is impossible to create with the given constraints.
        - return false
    - to efficiently find the largest value every iteration, a heap is used to maintain a sorted order of the values
    - implementation optimization:
        - it is possible to repeatedly decrease the value at the same index multiple times if it remains the largest value multiple times
            - the cumulative result becomes ((largestValue - 1) % sumOfRemainingValues + 1)
                - the - 1 and + 1 ensures that the value is reduced to 1 if the largest value can be perfectly divided by the sum of remaining values
        - to save space, indexes with values of 1's are not held in the heap
            - if the largest value in the heap is 1, the target array is possible to create

Runtime: O(N*log(N)), where N is the length of the target array
Space: O(N), where N is the length of the target array
*/

/**
 * @param {number[]} target
 * @return {boolean}
 */
var isPossible = function (target) {
    // smallest value has to be combined first
    // how to choose which value to change?
    //  changing different values can produce different results
    // related topics from leetcode: array, heap (priority q)
    // leetcode hints:
    // 1. work backwards
    // the largest value - the sum of the rest of the array is the previous value of the index

    // edge case of only 1 value in the target array
    if (target.length == 1) {
        // if the only value is 1, it's possible; otherwise, it is not.
        if (target[0] == 1) {
            return true
        } else {
            return false
        }
    }

    // min heap implementation by Ankita Masand on medium / bits and pieces
    // https://blog.bitsrc.io/implementing-heaps-in-javascript-c3fbf1cb2e65
    // Slightly modified because the remove function would not finish sinking a value if the node did not have 2 children.
    class MinHeap {

        constructor() {
            /* Initialing the array heap and adding a dummy element at index 0 */
            this.heap = [null]
        }

        getMin() {
            /* Accessing the min element at index 1 in the heap array */
            return this.heap[1]
        }

        insert(node) {

            /* Inserting the new node at the end of the heap array */
            this.heap.push(node)

            /* Finding the correct position for the new node */

            if (this.heap.length > 1) {
                let current = this.heap.length - 1

                /* Traversing up the parent node until the current node (current) is greater than the parent (current/2)*/
                while (current > 1 && this.heap[Math.floor(current / 2)] > this.heap[current]) {

                    /* Swapping the two nodes by using the ES6 destructuring syntax*/
                    [this.heap[Math.floor(current / 2)], this.heap[current]] = [this.heap[current], this.heap[Math.floor(current / 2)]]
                    current = Math.floor(current / 2)
                }
            }
        }

        remove() {
            /* Smallest element is at the index 1 in the heap array */
            let smallest = this.heap[1]

            /* When there are more than two elements in the array, we put the right most element at the first position
                and start comparing nodes with the child nodes
            */
            if (this.heap.length > 2) {
                this.heap[1] = this.heap[this.heap.length - 1]
                this.heap.splice(this.heap.length - 1)

                if (this.heap.length === 3) {
                    if (this.heap[1] > this.heap[2]) {
                        [this.heap[1], this.heap[2]] = [this.heap[2], this.heap[1]]
                    }
                    return smallest
                }

                let current = 1
                let leftChildIndex = current * 2
                let rightChildIndex = current * 2 + 1

                while (this.heap[leftChildIndex] && this.heap[current] > this.heap[leftChildIndex]
                    || this.heap[rightChildIndex] && this.heap[current] > this.heap[rightChildIndex]) {
                    if (this.heap[leftChildIndex] && this.heap[rightChildIndex] && this.heap[leftChildIndex] < this.heap[rightChildIndex] || !this.heap[rightChildIndex]) {
                        [this.heap[current], this.heap[leftChildIndex]] = [this.heap[leftChildIndex], this.heap[current]]
                        current = leftChildIndex
                    } else {
                        [this.heap[current], this.heap[rightChildIndex]] = [this.heap[rightChildIndex], this.heap[current]]
                        current = rightChildIndex
                    }

                    leftChildIndex = current * 2
                    rightChildIndex = current * 2 + 1
                }
            }

            /* If there are only two elements in the array, we directly splice out the first element */

            else if (this.heap.length === 2) {
                this.heap.splice(1, 1)
            } else {
                return null
            }

            return smallest
        }
    }
    // populate the heap and find the sum
    const minHeap = new MinHeap()
    let sum = 0

    for (let num of target) {
        if (num > 1) {
            minHeap.insert(-num)
        }
        sum += num
    }

    // iterate until the array only has 1's or the target array is invalid:
    // choose the largest value
    // subtract the largest value from the sum
    // subtract the sum from the largest value
    // replace the largest value with the new value
    while (minHeap.getMin() != undefined) {
        let largest = -minHeap.remove()
        sum -= largest
        if (largest <= sum) {
            return false
        }

        let newVal = (largest - 1) % sum + 1
        sum += newVal
        if (newVal > 1) {
            minHeap.insert(-newVal)
        }
    }

    return true
};

const targets = [
    [1, 1000000000] // true
    , [9, 3, 5] // true
    , [1, 1, 1, 2] // false
    , [8, 5] // true
    , [2, 2, 2, 2] // false
    , [1, 3, 17] // true
    , [1, 2, 10] // false
    , [100] // false
    , [2, 900000002] // false
]

for (let target of targets) {
    console.log(target, isPossible(target))
}