# leetcode problem # 1523. Count Odd Numbers in an Interval Range

"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
0 <= low <= high <= 10^9
"""

"""
My solution: Math

Idea:
In continuous whole number ranges, roughly half of the numbers are odd
- The numbers alternate between odd and even
- Need to check the edge of the ranges to find out exactly how many odd numbers are in the range

Execution:
Baseline: there are at least floor(range / 2) odd numbers in a number line
- range = high - low
- the result is floored as there can't be 0.5 odd numbers
If range is even:
- both low and high must be even or odd; it is impossible for low to be even and high be odd and vice versa
- if both low and high are odd, there is 1 odd number not accounted for by range/2
    - +1 to answer
If range is odd:
- either low or high must be even, and the other value must be odd
- range/2 will always miss 1 odd number in this case
    - +1 to answer

Runtime: O(1), runtime does not depend on input
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            ans += 1
        return ans
