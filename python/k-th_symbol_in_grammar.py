# leetcode problem # 779. K-th Symbol in Grammar

"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:
Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01

Example 3:
Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01

Constraints:
1 <= n <= 30
1 <= k <= 2^(n - 1)
"""

"""
My solution: Recursive solution

Observations: 
1. Regardless of the row number, the value at index i (as long as i is a valid index in the row)
    is always the same
    -> The solution logic does not need to account for the row number n
        - the problem boundaries already limits the range of k to be valid
        - even if the problem did not bound k to be valid, the check is trivial
2. The value at index k is dependent on the value at index floor(k / 2)
    - this relation is recursive, until the base case of k = 0 or k = 1
    - this is due to the fact that each value becomes two values with each subsequent row

Solution: Find the "parent" value that the current value is based on
1. Recursively find the "parent" value
    i. the parent value is the value at index floor(k / 2)
    ii. base cases:
        - k = 0: value is 0
        - k = 1: value is 1
    iii. if k is odd, the value of k is the opposite of the value of its parent
    iv. if k is even, the value of k is the same as the value of its parent
2. Return the value at index k


Runtime: O(N) where N is the input integer k
Space: O(N)
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def findParent(num):
            if num <= 1:
                return num
            parent = findParent(num // 2)
            if num % 2:
                if parent == 1:
                    return 0
                else:
                    return 1
            else:
                return parent

        return findParent(k - 1)