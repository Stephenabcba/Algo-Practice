# leetcode problem # 50. Pow(x, n)

"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= x^n <= 10^4
"""

"""
My solution: iterative building

Property of powers: X^M * X^N = X^(M+N)
ex: 2^5 * 2^7 = 2^12

Idea: double the power each time a calculation is performed, then
multiply the answer by the largest power currently calculated without
exceeding N

Keep a stack of the previous results
- if the current power + the last power in the stack <= N, multiply the
current result by the value in the stack, and add the last power to the current
power
    - add the new result and the new power to the stack
- otherwise, pop from the stack until the requirement above is satisfied

For cases where N < 0, start with 1/X in the stack and change N to -N

Runtime: O(logN) where N is the power to raise X to
Space: O(logN)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        ans = 1
        stack = []

        curPower = 0

        if n < 0:
            stack.append((1, 1 / x))
            n = -n
        else:
            stack.append((1, x))
        
        while curPower < n:
            if curPower + stack[-1][0] <= n:
                ans *= stack[-1][1]
                curPower += stack[-1][0]
                stack.append((curPower, ans))
            else:
                stack.pop()

        return ans
    

"""
Solution by leetcode: Recursion with binary exponention

Binary Exponention: a property of powers where X^2N == (X^2) ^ N
ex: 2^100 == 4^50 == 16^25

Moreover, X^N == X * X^(N-1)
ex: 16^25 == 16 * 16^24 == 16 * 256^6

Thus, the power X^N can be broken down into larger bases with smaller powers
and reconstructed instead of iteratively multiplying X by itself N times.

Runtime: O(logN)
Space: O(logN)
"""

class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1
       
        # Handle case where, n < 0.
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)
       
        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)