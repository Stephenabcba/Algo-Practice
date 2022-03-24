// leetcode problem # 881. Boats to Save People
/*
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
*/

/*
My solution: sort then match
idea:
- if possible, pair the heaviest person with the lightest person
    - if the lightest person pairs with someone else, the heaviest person might require an extra boat
- for optimization, sort the array first
    - if searching the array for min and max every iteration, the runtime becomes O(N^2)
    - by sorting first, finding the min and max afterwards is an O(1) operation
    - having the search in parallel with the sort has the overall runtime of O(sorting algorithm)
        - typically, the runtime of sorting is O(N * logN)

implementation:
1. sort the input array
    - JavaScript built-in sort is used here, but better sort methods can be used if needed
2. initialize the variables required
    - 2 pointers / moving indexes are used for the array
        - the front index start at the start of the array, the back index starts at the back of the array
        - all indexes before the front index AND all indexes after the back index are on a boat
    - at the beginning, noone is in a boat, so number of boats is 0
3. iterate through the now sorted array
    - iteration stops when the back index is no longer larger than the front index
    - if the sum of the weight of 2 people at the front and back index is less than the limit, both can enter the same boat
        - increment the front index and decrement the back index
    - otherwise, only the heaviest person enters the boat
        - decrement the back index
    - exactly 1 boat is occupied every iteration
        - increment the number of boats every iteration
4. if the front index and back index are equal, the person is alone and hasn't entered the boat
    - incement the numebr of boats by 1
5. return the number of boats

Efficiency:
runtime: O(N * logN)
    - sorting is typically O(N * logN)
    - the remaining logic is in parallel with sorting, and has runtime of O(N)

space: O(N) ?
    - the space complexity depends on the sorting algorithm used
        - JavaScript sort seems to use merge sort -> O(N)
    - The remaining logic only works with indexes and counters -> O(1) space complexity
*/


/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function (people, limit) {
    people.sort((a, b) => a - b)
    let frontIdx = 0
    let backIdx = people.length - 1
    let numBoats = 0
    while (backIdx > frontIdx) {
        if (people[frontIdx] + people[backIdx] <= limit) {
            frontIdx++
            backIdx--
        } else {
            backIdx--
        }
        numBoats++
    }
    if (backIdx === frontIdx) {
        numBoats++
    }
    return numBoats
};

// Input: 
const people = [1, 2]
const limit = 3
// Output: 1
// Explanation: 1 boat (1, 2)

// Input: 
const people2 = [3, 2, 2, 1]
const limit2 = 3
// Output: 3
// Explanation: 3 boats (1, 2), (2) and (3)

// Input: 
const people3 = [3, 5, 3, 4]
const limit3 = 5
// Output: 4
// Explanation: 4 boats (3), (3), (4), (5)

console.log(numRescueBoats(people, limit))
console.log(numRescueBoats(people2, limit2))
console.log(numRescueBoats(people3, limit3))