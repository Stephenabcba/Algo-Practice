# leetcode problem # 343. Integer Break

"""
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Constraints:
2 <= n <= 58
"""

"""
My solution: Break into 3's

Observation:
In almost all cases, breaking all values into 3's yields the highest product
    - breaking values into 2s usually yields the same result as breaking values into 4s
* Exception: if the remainder is 1, it's better to remove a 3 and add it to the remainder
    - ex: if n == 10, 3 * 3 * 3 * 1 = 27, but 3 * 3 * 4 = 36

Implementation detail:
1. If the remainder is 0, also change a 3 to the remainder side
    - this makes the case of n == 3 easier to process
2. If the number of 3s to break == 0, split the remainder into halves and multiply them
    - this also applies when remainder is 3 and no other 3s are present
3. If there are multiple 3s, then the product is 3 ^ (number of 3) * remainder

Runtime: O(1), Runtime does not depend on input
Space: O(1), Space does not depend on input
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        rem = n % 3
        quotient = n // 3

        if rem < 2 and quotient > 0:
            quotient -= 1
            rem += 3

        if quotient == 0:
            split1 = rem // 2
            return split1 * (rem - split1)
        else:
            return 3 ** quotient * rem