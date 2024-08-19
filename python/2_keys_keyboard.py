# leetcode problem # 650. 2 Keys Keyboard

"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

Example 1:
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:
Input: n = 1
Output: 0

Constraints:
1 <= n <= 1000
"""

"""
My solution: Hard-coded prime factoring

Observation 1: The number of operations can be lowered if a larger value can be copied and pasted
Observation 2: If n is a prime number, it takes exactly n operations to reach n
    - copying and pasting a value greater than 1 implies that n has factors besides 1 and n, which goes against the definition of prime numbers

Idea: The number of operations is the sum of all prime factors of n, where n = x * y * z * ...
- from 1, the value is copied and pasted until it reaches x  (x operations)
- from x, the value is copied and pasted until it reaches x * y (y operations)
- from x * y, the value is copied and pasted until it reaches x * y * z (z operations)
- the process is repeated until n is reached, and the total operations is x + y + z + ...

Example 1: n is a prime number, n = 11
-> There is no other way besides copying then pasting 10 times, resulting in 11 operations
Example 2: n is not a prime number, n = 100
- After prime factoring, n = 100 = 2 * 2 * 5 * 5
-> The total number of operations is 2 + 2 + 5 + 5 = 14

Logic: Find all prime factors of n, then sum them up
- iterate through the list of pre-occupied prime numbers and divide by the prime number if the remainder is 0
- return the sum of all prime factors


This solution should be slightly faster than leetcode's solution, but scales poorly if the limit of N is increased.

Runtime: O(M) where M is the number of prime factors under N, which is the limit of the input integer N
Space: O(M)


"""


class Solution:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
              449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        ans = 0
        leftover = n
        for prime in self.primes:
            if prime > leftover:
                break
            while leftover % prime == 0:
                leftover //= prime
                ans += prime

        return ans


"""
Solution by leetcode: Prime Factoring without hard-coding

By iterating through all values from 2 to n, every possible prime number is passed through, yielding the same result without needing to
hard-code every prime value
- As the values are iterated in ascending order, the non-primes are already processed in their own prime factors.

Runtime: O(N)
Space: O(1)
"""


class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until is no longer divisible
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
