// leetcode problem # 1642. Furthest Building You Can Reach

/*
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.


Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:

1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length
*/

/*
My solution: favor bricks while using a heap to manage the bricks used.
- min heap implementation by Ankita Masand on medium / bits and pieces

Two main cases:
- the next building is equal to or lower in height than the current building
    - no bricks or ladders needed.
- the next building is taller than the current building
    - the algorithm must decide whether bricks or ladders should be used
    - this algorithm favors bricks whenever possible.
    - keep track of all bricks used, sorted by their height
        - a heap can continuously keep the heights sorted in log(N) time.
        - a max heap is implemented by inserting negative values into a min heap
    - cases:
        1. there are enough bricks
            - use bricks to reach the next building
            - add the number of bricks used to the heap
        2. there aren't enough bricks, but there are ladders remaining
            - replace the height difference with the most bricks used with a ladder
            - the highest height difference could either be at the current building or at a previous building.
                - the max heap keeps track of the number of bricks used, so the comparison is simple.
        3. there aren't enough bricks, and there are no more ladders
            - it is impossible to reach the next building
            - return the current index

if it is possible to reach all buildings, the index of the last building is the answer.
    - this value is heights.length - 1

Runtime: O(N * logN) where N is the number of buildings
    - in the worst case, the algorithm iterates through every building, and removes values from the heap.
Space: O(N) where N is the number of buildings
    - the heap takes up to O(N) space if bricks are used every iteration.
*/

/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function (heights, bricks, ladders) {

    // min heap implementation by Ankita Masand on medium / bits and pieces
    // https://blog.bitsrc.io/implementing-heaps-in-javascript-c3fbf1cb2e65
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

                while (this.heap[leftChildIndex] &&
                    this.heap[rightChildIndex] &&
                    (this.heap[current] > this.heap[leftChildIndex] ||
                        this.heap[current] > this.heap[rightChildIndex])) {
                    if (this.heap[leftChildIndex] < this.heap[rightChildIndex]) {
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

    const minHeap = new MinHeap()

    for (let i = 0; i < heights.length - 1; i++) {
        let heightDiff = heights[i + 1] - heights[i]

        // if the next building is equal or shorter in height, no bricks or ladders needed.
        if (heightDiff <= 0) {
            continue
        }

        if (heightDiff <= bricks) {
            // there are enough bricks to build up to the next building
            bricks -= heightDiff
            minHeap.insert(-heightDiff)
        } else {
            // there aren't enough bricks to build up to the next building

            // if there are no ladders, there's no way of moving to the next building
            if (ladders < 1) {
                return i
            }

            // if there are ladders, a ladder can be used to replace the building with the most bricks used
            let mostBricks = minHeap.getMin()

            // case 1: if there were no buildings previously reached with bricks, a ladder must be used at the current building.

            // case 2: if the previous building was the largest building reachable by bricks, replace that building's bricks with a ladder
            //      the current building will use bricks.

            // case 3: (not explicitly shown in logic:) if the current height difference is the largest, use the ladder at the current building
            if ((mostBricks != undefined) && heightDiff < -mostBricks) {
                minHeap.remove()
                bricks += -mostBricks - heightDiff
                // an attempt was failed due to not adding the building's bricks back to the heap.
                minHeap.insert(-heightDiff)
            }

            // in all 3 cases above, a ladder is used.
            ladders -= 1
        }
    }

    return heights.length - 1
};