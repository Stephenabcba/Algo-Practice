// leetcode problem # 858. Mirror Reflection

/*
There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.


Example 1:
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/18/reflection.png
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Example 2:
Input: p = 3, q = 1
Output: 1

Constraints:

1 <= q <= p <= 1000
*/

/*
My solution: Make use of least common multiple

Observation: due to the working area being a square, if the laser ray bounces off the top or bottom wall, the laser will continue bouncing off the left/right wall as if another square is stacked on top of the current square
- the problem becomes finding how many squares it takes to hit a corner of the room, then finding out which corner corresponds to in the original room.
- a square stacked on top is a mirror image flipped across the horizonal axis
    - the top left becomes bottom left, and top right becomes bottom right, etc.

Using least common multiple (LCM), it could be easily found how many squares were stacked on top of the original room
- to find LCM, the formula (A * B / GCD) is used
    - GCD is the greatest common multiple, which can be found with Euclidean algorithm (taken from wikipedia)

From testing and observation:
LCM / q is the number of times the laser bounced off a left or right wall
- if LCM / q = 1, the laser directly went from the bottom left to the top right corner
- if LCM / q is even, the laser either hit the bottom left or top left corner
    - if the laser hit the bottom corner, it till keep bouncing until it hits the top left corner
    - in both cases, the laser will hit corner 2 eventually
- if LCM / q is odd, the laser either hit the bottom right or the top right corner
    - it is inconclusive which corner the laser hit based on LCM / q alone
    - the laser would have hit either corner 0 or corner 1
LCM / p is the number of squares needed for the laser to reach a corner
- if LCM / p = 1, the laser reached a corner in the orinal square
- based on the reflecting property of the stacking squares (a square stacked on top reverses the top and bottom corners), the following conclusions can be made:
    - if LCM / q is odd and LCM / p is odd, then the laser has hit the top right corner
        - the laser has hit corner 1
    - if LCM / q is odd and LCM / p is even, the laser has hit the bottom right corner
        - the laser has hit corner 0
Runtime: O(N) where N is the value of input P
- The main runtime contribution is from the GCD calculation
    - in the worst case, the inputs are 1000 and 999
        - the GCD is 1, but the algorithm has to keep subtracting 1 every iteration until it reaches 0, which would take 1000 iterations
Memory: O(1), the memory usage does not depend on input
*/

/**
 * @param {number} p
 * @param {number} q
 * @return {number}
 */
var mirrorReflection = function (p, q) {
    // the gcd function finds the gcd using the Euclidean algorithm
    let gcd = (a, b) => {
        if (b > a) {
            [a, b] = [b, a]
        }
        let remainder = b
        while (a % b > 0) {
            remainder = a % b
            a = b
            b = remainder
        }
        return remainder
    }

    // find LCM using GCD
    let lcm = p / gcd(p, q) * q

    if ((lcm / q) % 2 === 0) {
        return 2
    } else {
        if ((lcm / p) % 2 === 1) {
            return 1
        }
        return 0
    }

};