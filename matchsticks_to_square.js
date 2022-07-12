// leetcode problem # 473. Matchsticks to Square

/*
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
*/

/*
My attempt:Brute Force
Hint1: Treat the matchsticks as an array. Can we split the array into 4 equal halves?
Hint2: Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
Hint3: For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. We can make use of recursion for this.
Hint4: We don't really need to keep track of which matchsticks belong to a particular side during recursion. We just need to keep track of the length of each of the 4 sides.
Hint5: When all matchsticks have been used we simply need to see the length of all 4 sides. If they're equal, we have a square on our hands!

Runtime: O(4^N) where N is the length of the matchsticks array
-> The runtime takes too long at max input size of 15
*/

/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquareAttempt = function (matchsticks) {
    let recursion = (index, side1, side2, side3, side4) => {
        if (index < matchsticks.length) {
            return recursion(index + 1, side1 + matchsticks[index], side2, side3, side4) ||
                recursion(index + 1, side1, side2 + matchsticks[index], side3, side4) ||
                recursion(index + 1, side1, side2, side3 + matchsticks[index], side4) ||
                recursion(index + 1, side1, side2, side3, side4 + matchsticks[index])
        } else if (side1 == side2 && side1 == side3 && side1 == side4) {
            return true
        } else {
            return false
        }
    }

    return recursion(0, 0, 0, 0, 0)

};

/*
Solution from Leetcode: Dynamic Programming (originally written in Java)
Uses a binary array (effectively an integer) to keep track of the number of matchsticks used during recursion.
The memoization keeps track of the matchsticks used (through the binary array) and the maximum number of sides done

Due to the nature of a square, once 3 sides of the correct length has been constructed, the 4th side will also be of the correct length

Time: O(N * 2^N)
Space: O(N + 2^N)
*/

/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function (matchsticks) {
    // Memoization for recursion
    let memo = new Map()

    let nums = matchsticks

    // The side length of the completed square (if possible)
    // This value is the sum of lengths of all matchsticks divided by 4
    let possibleSquareSide = 0

    // Main recursion logic
    let recurse = (mask, sidesDone) => {
        let total = 0
        let L = nums.length

        // memo key for the memo Map
        // as JS does not have a Pair class, a string is used instead
        // the Map does not recognize new arrays and objects as a key, and thus making the memo useless
        let memoKey = "" + mask + "," + sidesDone

        // sum of lengths of all matchstick used
        for (let i = L - 1; i >= 0; i--) {
            if ((mask & (1 << i)) == 0) {
                total += nums[L - 1 - i]
            }
        }

        // If the sum if divisible by our square's side, then we increment our number of complete sides formed variable.
        if (total > 0 && total % possibleSquareSide == 0) {
            sidesDone++
        }

        // Base case.
        if (sidesDone == 3) {
            return true
        }

        // Return precomputed results
        if (memo.has(memoKey)) {
            return memo.get(memoKey)
        }
        let ans = false
        let c = Math.floor(total / possibleSquareSide)

        // Remaining vlength in the current partially formed side.
        let rem = possibleSquareSide * (c + 1) - total

        // Try out all remaining options (that are valid)
        for (let i = L - 1; i >= 0; i--) {
            if (nums[L - i - 1] <= rem && (mask & (1 << i)) > 0) {
                if (recurse(mask ^ (1 << i), sidesDone)) {
                    ans = true
                    break
                }
            }
        }

        // Cache the computed results.
        memo.set(memoKey, ans)
        return ans
    }

    // Calling the functions

    // don't need to process if matchsticks array is empty
    if (nums == null || nums.length == 0) {
        return false
    }

    // Find the perimeter of the matchsticks (total length)
    let L = nums.length
    let perimeter = 0
    for (let i = 0; i < L; i++) {
        perimeter += nums[i]
    }

    // It's impossible if the perimeter is not divisible by 4
    possibleSquareSide = Math.floor(perimeter / 4)
    if (possibleSquareSide * 4 != perimeter) {
        return false
    }

    return recurse((1 << L) - 1, 0)
};