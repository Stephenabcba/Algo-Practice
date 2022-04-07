// leetcode problem # 1046. Last Stone Weight

/*
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.
Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
*/

/*
My solution: sort and pop
Idea:
- sort the stones array from smallest to largest
    - maintain the order throughout the iterations
- the largest 2 stones are always at the end of the array
    - if the largest 2 stones are equal in weight, pop both from the array
    - if the second largest stone is smaller, "float" the remaining weight within the array
Implementation:
- Sort the stones array with built-in sort function
- iterate through the stones array until at most 1 element remains
    - case 1: largest 2 stones equal in weight
        - pop both stones from the array
    - case 2: the second largest stone is smaller
        - "float" the remaining weight to its proper position
            - swap the remaining weight with the element to its left if the remaining weight is smaller
            - maintains the order of the remaining array
        - pop one stone
- return either weight of remaining stone, or 0 if there's no remaining stones
runtime: O(N^2), the outer loop repeats O(N) times, and the inner "float" loop repeats O(N) times
space: O(1) or O(N), depending on the sorting algorithm

Available Improvements:
1. from leetcode discussion by zayne-siew:
- utilize a heap data structure to reduce runtime
    - converting an array to a heap takes O(N) time
    - pushing and popping from a heap takes O(logN) time
        - in a max heap, the popped value is always the largest value
            - this can also be achieved by setting all values to negative in a min heap
    - there is no need to use sort anymore
- overall runtime becomes O(N*logN)
- space is still O(1), the heap can be done in-place within the array

2. from submission data for javascript:
- using sort() every iteration seems to be popular
- splice() and shift() also seems to be popular
*/

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
    // sort the array
    stones.sort((a, b) => a - b)
    // main logic
    while (stones.length > 1) {
        if (stones[stones.length - 1] == stones[stones.length - 2]) { // largest 2 stones equal in weight
            stones.pop()
        } else { // the second largest stone is smaller
            stones[stones.length - 2] = stones[stones.length - 1] - stones[stones.length - 2]
            let i = stones.length - 2
            while (i > 0 && stones[i] < stones[i - 1]) {
                let temp = stones[i]
                stones[i] = stones[i - 1]
                stones[i - 1] = temp
                i--
            }
        }
        stones.pop()
        // console.log(stones)
    }
    return (stones.length == 1) ? stones[0] : 0
};



// Example 1:

// Input: 
const stones = [2, 7, 4, 1, 8, 1]
// Output: 1
// Explanation: 
// We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
// we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
// we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
// we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

// Example 2:

// Input: 
const stones2 = [1]
// Output: 1