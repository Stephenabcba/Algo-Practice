// leetcode problem #1007. Minimum Domino Rotations For Equal Row
/*
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Constraints:
2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
*/

/*
My solution:
idea:
-since the desired result requires that either the top or the bottom row all have the same value, 
  the value MUST exist as either the top or bottom value of the first domino
    - otherwise, the first value will not match with the rest of the row, and the desired result cannot be achieved
- by keeping track of how many times the top and bottom value appeared at the top and bottom of each domino (4 counters, top at top, top at bottom, etc.), 
  the minimum amount of flips can be obtained by finding the highest count of the value that reaches the requirement
    - the minimum flips is the (total dominos count - highest count that meets requirement)
        - ex: if there are 300 dominos
            - case 1: all 300 dominos contain "2", 160 "2" at the top and 200 "2" at the bottom
                - the higher count of "2" is 200, return 300-200 = 100
            - case 2: 299 dominos contain "2" as its top value, but the last domino does not contain "2"
                - the operation cannot be done, return -1

implementation:
1. initialize all required variables
    - topNum is the value of the top half of the first domino
    - botNum is the value of the bottom half of the first domino
    - 4 counter variables for each case of matching
        - topTopCount is the number of times that topNum was found at the top of a domino
        - topBotCount is the number of times that topNum was found at the bottom of a domino
        - botTopCount is the number of times that botNum was found at the top of a domino
        - botBotCount is the number of times that botNum was found at the bottom of a domino
    - 2 match count variables are also created to check whether at least one of the values on the first domino meets the requirement
        - if both match counters are lower than the total number of dominoes, the desired result cannot be done
2. iterate through the dominos
    - if topNum exists on the domino, increment top match
    - if botNum exists on the domino, increment bot match
    - increment the corresponding counter variables
        - ex: if topNum is 2, botNum is 5, and the domino is [5,6]: botTopCount is incremented
3. check if either topNum or botNum appeared on all the dominos
    - this is done by comparing both match counts against the number of dominos
    - if both numbers met the requirement, all 4 counters can be considered valid
    - if only one number met the requirement, only 2 counters will be considered valid
        - if only topNum met the requirement, only topTop and topBot counters can be considered valid
        - if only botNum met the requirement, only botTop and botBot coutners can be considered valid
    - if neither met the requirement, return -1
    - find the highest valid counter
    - return the total count of dominos - the highest valid counter
*/

/**
 * @param {number[]} tops
 * @param {number[]} bottoms
 * @return {number}
 */
var minDominoRotations = function (tops, bottoms) {
    const topNum = tops[0]
    const botNum = bottoms[0]
    const domCount = tops.length
    let topTopCount = 0
    let botBotCount = 0
    let topBotCount = 0
    let botTopCount = 0
    let topMatchCount = 0
    let botMatchCount = 0
    for (let i = 0; i < domCount; i++) {
        if (tops[i] === topNum || bottoms[i] === topNum) {
            topMatchCount++
        }
        if (tops[i] === botNum || bottoms[i] === botNum) {
            botMatchCount++
        }
        if (tops[i] === topNum) {
            topTopCount += 1
        }
        if (tops[i] === botNum) {
            botTopCount += 1
        }
        if (bottoms[i] === topNum) {
            topBotCount += 1
        }
        if (bottoms[i] === botNum) {
            botBotCount += 1
        }
    }
    // console.log(topMatchCount, botMatchCount);
    // console.log(topTopCount, topBotCount, botTopCount, botBotCount);
    if (topMatchCount === domCount || botMatchCount === domCount) {
        let mostTilesCount
        if (topMatchCount === domCount) {
            if (botMatchCount === domCount) {
                mostTilesCount = topTopCount
                if (topBotCount > mostTilesCount) {
                    mostTilesCount = topBotCount
                }
                if (botTopCount > mostTilesCount) {
                    mostTilesCount = botTopCount
                }
                if (botBotCount > mostTilesCount) {
                    mostTilesCount = botBotCount
                }
            } else {
                mostTilesCount = topBotCount
                if (topTopCount > topBotCount) {
                    mostTilesCount = topTopCount
                }
            }
        } else if (botMatchCount === domCount) {
            mostTilesCount = botBotCount
            if (botTopCount > botBotCount) {
                mostTilesCount = botTopCount
            }
        }
        return domCount - mostTilesCount
    } else {
        return -1
    }
};

const tops = [2, 1, 2, 4, 2, 2]
const bottoms = [5, 2, 6, 2, 3, 2]
const tops2 = [3, 5, 1, 2, 3]
const bottoms2 = [3, 6, 3, 3, 4]
const tops3 = [2, 2, 2, 2, 2, 2]
const bottoms3 = [2, 2, 2, 2, 2, 2]
const tops4 = [1, 2, 1, 1, 1, 2, 2, 2]
const bottoms4 = [2, 1, 2, 2, 2, 2, 2, 2]

console.log(minDominoRotations(tops, bottoms));