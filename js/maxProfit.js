/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy = prices[0]
    let profit = 0
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] < buy) {
            buy = prices[i]
        } else if (prices[i] - buy > profit) {
            profit = prices[i] - buy
        }
    }
    return profit
};

console.log(maxProfit([7,1,5,3,6,4]));
console.log(maxProfit([[7,6,4,3,1]]));
console.log(maxProfit([2,3,1,6]));
console.log(maxProfit([2,9,1,6]));