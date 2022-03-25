// leetcode problem #1029. Two City Scheduling
/*
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
*/

/*
My solution: Opportunity Costs and Sorting
Idea:
- The opportunity cost is defined as "the loss of potential gain from other alternatives when one alternative is chosen."
    - in this case, how much does it ACTUALLY cost when a person goes to city B instead of city A
    - if it costs more to send the person to city B, the opportunity cost is positive, with value being the extra cost
        - if possible, this person should not go to city B
    - if it costs less to send the person to city B, the opportunity cost is negative, with value being the saved amount
        - if possible, this person should go to city B
    - when opportunity cost is negative, money is saved when the person is sent to city B instead of city A
        - numbers closer to negative infinity saves more money
        - -1000 saves more money than -10
- By optimizing for the lowest overall opportunity costs, the least money is spent
    - even if all opportunity cost of going to city B is positive, sending the people with the lowest opportunity costs will lead the least money spent
- The minimum cost can then be found by the following:
    - compute the cost of sending every person to city A
    - compute the opportunity cost of sending each person to city B
    - send half of the people with the lowest opportunity costs to city B
        - for each person sent to city B, the cost is changed by the opportunity cost

Implementation:
1. iterate over the array of people
    - add the cost of sending person to city A to the total cost
    - compute the opportunity cost of sending the person to city B instead of city A
        - add the result to the opportunity costs array
2. sort the opportunity costs array from smallest to largest
    - it is a lot easier to find the minimum opportunity costs
3. iterate for half of the people array
    - increase the total cost by the opportunity cost
        - if the opportunity cost is negative, total cost is decreased instead
    - if there's 2n people in the array, only send n people to city B
4. return the total cost
*/

/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function (costs) {
    let totalCost = 0
    const opportunityCosts = []
    for (let cost of costs) {
        totalCost += cost[0]
        opportunityCosts.push(cost[1] - cost[0])
    }
    opportunityCosts.sort((a, b) => a - b)
    for (let i = 0; i < costs.length / 2; i++) {
        totalCost += opportunityCosts[i]
    }
    return totalCost
};

//Example 1:

// Input: 
const costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
// Output: 110
/*
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
*/

// Example 2:

// Input: 
const costs2 = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
// Output: 1859

// Example 3:

// Input: 
const costs3 = [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]
// Output: 3086

console.log(twoCitySchedCost(costs3));