// leetcode problem # 1338. Reduce Array Size to The Half

/*
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.



Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.


Constraints:
2 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
*/

/*
My solution: Make use of Heaps

Observation: the values with the highest frequencies are always the ones removed.
-> Find the counts and removed the ones with the highest counts

Pseudocode:
1. Find the frequencies of each unique values in arr
- this can be done with a for-loop and a dictionary
2. Sort the values from largest to smallest
- This could be done with a heap
- As the current heap-building process takes O(N*logN) time, this step can also be done with building an array of counts and sorting the array.
    - the next steps do not change the order of the sorted array.
3. Remove the first X counts until more than half of the array is removed
- X is the answer
- Remove the number with the highest counts first

Runtime: O(N*log(N)) where N is the length of the input array
- finding the frequencies of each unique number takes O(N) time
- building the heap takes O(M * log M) time, where M is the number of unique values in input array
    - as M ~= N, the runtime can also be changed to O(N log N)
Space: O(N) where N is the length of the input array
- The count dictionary can take up to O(N) space
- The heap can take up to O(N) space
*/


/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function (arr) {
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

    // find the count of each unique value in arr
    let frequencies = {}

    for (let num of arr) {
        if (frequencies.hasOwnProperty(num)) {
            frequencies[num] += 1
        } else {
            frequencies[num] = 1
        }
    }

    // insert the counts into a heap to find the largest
    let heap = new MinHeap()
    for (value of Object.values(frequencies)) {
        // as the implementation is a minheap, inserting values as negatives creates a max heap
        heap.insert(-value)
    }

    // remove the first x largest values until the total count of removed numbers reaches half of arr's length
    // x will be the answer.
    let removedCount = 0
    let ans = 0
    while (removedCount < arr.length / 2) {
        removedCount += - heap.remove()
        ans += 1
    }

    return ans
};

/*
Alternative solution: Using sorting instead of heaps
Step 2 of the above logic is replaced with a sorted array.

Runtime and Memory usage remains the same order of magnitude
However, the O(log N) operation of each heap removal is replaced by O(1) with array indexing.
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize2 = function (arr) {
    let frequencies = {}

    for (let num of arr) {
        if (frequencies.hasOwnProperty(num)) {
            frequencies[num] += 1
        } else {
            frequencies[num] = 1
        }
    }

    let counts = Object.values(frequencies)
    counts.sort((a, b) => b - a)

    let removedCount = 0
    let ans = 0
    while (removedCount < arr.length / 2) {
        removedCount += counts[ans]
        ans += 1
    }

    return ans
};