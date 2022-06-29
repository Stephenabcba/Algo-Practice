// leetcode problem # 406. Queue Reconstruction by Height

/*
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).


Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Constraints:

1 <= people.length <= 2000
0 <= hi <= 10^6
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
*/

/*
My solution (with help from leetcode hints)
Hint 1: 
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?

Hint 2:
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?

Attempt logic 1:
1. Sort the people array from the lowest height to the largest height
2. Iterate through the people array
    - greedily try to place each person at the index that is equal to the number of people taller than them (k_i)
    - if the index is already occupied, linearly move down to the next available index
- shortcoming: this logic does not always place enought taller people in front of a person

New logic:
1. Sort the people array from the lowest height to the largest height
2. Iterate through the people array
    - instead of starting at index ki, start at index 0
    - find the first available location where the number of ((empty spaces) + (number of heights == h_i)) equals k_i


Runtime: O(N^2) where N is the length of input array
    - the most time-intensive portion of this algorithm is 
Space: O(N) where N is the length of input array
*/

/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function (people) {
    people.sort((a, b) => a[0] - b[0])

    const queue = []
    for (let i = 0; i < people.length; i++) {
        queue.push(null)
    }

    for (let person of people) {
        let index = 0
        let spaces = 0
        while (index < people.length && (spaces < person[1] || queue[index] !== null)) {
            if (queue[index] === null || queue[index][0] == person[0]) {
                spaces++
            }
            index++
        }
        queue[index] = person
    }

    return queue
};

/*
Another solution by constantine786 in leetcode discussions (originally written in python)

1. sort the array from largest to smallest height
    - if two items have the same height, the value with lower k comes first
2. greedily insert each person into the output array at index k_i
    - if needed, push other values back by 1 index
    - as the people array is sorted from tallest to shortest, new values inserted do not affect the order of values already in the output array

Runtime: O(N^2) where N is the length of input array
    - the insertion is an O(N) operation, repeated N times.
Space: O(N) where N is the length of input array
*/

/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue2 = function (people) {
    people.sort((a, b) => {
        if (a[0] == b[0]) {
            return a[1] - b[1]
        }
        return b[0] - a[0]
    })

    const queue = []

    for (let person of people) {
        queue.splice(person[1], 0, person)
    }

    return queue
};