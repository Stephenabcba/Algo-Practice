// leetcode problem # 1473. Paint House III

/*
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.



Example 1:
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.

Example 2:
Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.

Example 3:
Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.


Constraints:
m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
*/

/*
Solution from Leetcode Solutions (approach 3) (originally written in Java)
Intuition:
A painted house (houses[i] != 0) will not be painted again
- if the current house is set to be painted another color, it is impossible
- if the current house is the same as the desired color, it costs nothing for the given house.
An unpainted house (houses[i] == 0) can be painted any color
- the corresponding costs will be required

If a house is different colors from the previous house, a new neighborhood is added.

Due to how the logic is set up, the color of the last house will decide how the previous houses are painted.
- find the lowest cost out of all the colors of the last house from the prevMemo matrix

This solution is a space-optimized solution, where instead of holding the cost information of all previous houses, only hold the information for the previous and the current house
    - this reduces the memory usage from O(M*N*T) to O(N*T), where M is the number of houses, N is the number of colors, and T is the target neighborhood number.

Runtime: O(M*T*N^2), where M is the number of houses, N is the number of colors, and T is the target neighborhood number.
Memory: O(N*T), where N is the number of colors and T is the target neighborhood number.
*/


/**
 * @param {number[]} houses
 * @param {number[][]} cost
 * @param {number} m
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var minCost = function (houses, cost, m, n, target) {
    // initialize the previous memo matrix
    let prevMemo = []
    for (let i = 0; i <= target; i++) {
        prevMemo.push([])
        for (let j = 0; j < n; j++) {
            prevMemo[i].push(Infinity)
        }
    }

    // populate the costs to paint the first house as every color
    for (let color = 1; color <= n; color++) {
        if (houses[0] == color) {
            prevMemo[1][color - 1] = 0
        } else if (houses[0] == 0) {
            prevMemo[1][color - 1] = cost[0][color - 1]
        }
    }

    for (let house = 1; house < m; house++) {
        // create and initialize the memo matrix
        let memo = []

        for (let i = 0; i <= target; i++) {
            memo.push([])
            for (let j = 0; j < n; j++) {
                memo[i].push(Infinity)
            }
        }

        // iteration boundary is set such that there cannot be more neighborhoods than houses.
        for (let neighborhoods = 1; neighborhoods <= Math.min(target, house + 1); neighborhoods++) {
            for (let color = 1; color <= n; color++) {
                // the painter cannot paint a painted house another color.
                if (houses[house] != 0 && color != houses[house]) {
                    continue
                }

                // find the smallest cost to paint the previous houses
                let currCost = Infinity


                // check the costs to paint i-1 houses
                // if the previous color is different from the current color, a new neighborhood is added
                // -> check at neighborhoods-1 in the memo
                // otherwise, the current house is part of the previous neighborhood
                // -> check at neighborhoods in the memo
                for (let prevColor = 1; prevColor <= n; prevColor++) {
                    if (prevColor != color) {
                        currCost = Math.min(currCost, prevMemo[neighborhoods - 1][prevColor - 1])
                    } else {
                        currCost = Math.min(currCost, prevMemo[neighborhoods][color - 1])
                    }
                }

                // if the house is already painted, it's free
                let costToPaint = houses[house] != 0 ? 0 : cost[house][color - 1]

                memo[neighborhoods][color - 1] = currCost + costToPaint
            }
        }
        prevMemo = memo
    }

    let minCost = Infinity

    for (let color = 1; color <= n; color++) {
        minCost = Math.min(minCost, prevMemo[target][color - 1])
    }

    return minCost == Infinity ? -1 : minCost
};