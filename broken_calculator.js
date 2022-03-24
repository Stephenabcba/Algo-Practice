// leetcode problem # 991. Broken Calculator
/*
There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.
Constraints:

1 <= x, y <= 10^9
*/

/*
My Solution: work backwards from target
Idea:
- When working backwards, the options available are more limited
    - the available options are add the number by 1 or divide the number by 2
    - we cannot divide an odd number by 2 as this introduces decimals, which is impossible when working forwards
- With the limitations of working backwards, the divide (multiply in forwards operation) operation can be prioritized
    - when working forwards, both the multiply and subtract operations can be done at any time the number is greater than 0
    - division/multiplication is a lot more efficient in changing the order of magnitudes of the number
- Explanation found from leetcode comments by jxbcalex: 
    - If with subtraction and multiplication, the effect of earlier subtraction will be amplified by later multiplications
        -hence, greedily doing multiplication might not reach optimal solution as an additional early subtraction can have a huge effect.
    - Whereas with addition and division, earlier addition will be diminished by later divisions. 
        - It is thus always better to do division wherever possible.

Implementation:
- Start from the target value
- repeat the following until the the current number reaches the start value:
    - if the current number is even and larger than startVal, divide the current number by 2
    - otherwise (if the current number is larger and odd OR the current number is smaller) add 1
- keep track of of the number of operations done and return the number

Improvement:
- When the current number is smaller than startVal, we are always adding
    - the number of operations to go from that point to the startVal is constant, and thus do not need iterative manipulation
    - total operations = cur operation count + startValue - current number
*/

/**
 * @param {number} startValue
 * @param {number} target
 * @return {number}
 */
var brokenCalc = function (startValue, target) {
    let numSteps = 0
    let curNum = target
    while (curNum !== startValue) {
        if (curNum > startValue && curNum % 2 === 0) {
            curNum = curNum / 2
        } else {
            curNum += 1
        }
        numSteps += 1
    }
    return numSteps
};

/*
Test Cases:
Example 1:
Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:
Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example 3:
Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
*/