# leetcode Problem # 338. Counting Bits

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 10^5

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

"""
My solution: Dynamic Programming

Observations:
1. If the number is a power of 2, there is only one 1
2. When a large power of 2 is added to a smaller number, exactly one 1 is added
- ex: when 8 is added to 3 (8 + 3 = 11), 1000 + 0011 = 1011
    -> One 1 is added, without changing anything else
Edge case: there are zero 1's if and only if the number is 0

Idea: Build on top of of smaller values
- Work incrementally from 0 to N
- any value X can be split in A and B, where:
    - A is the largest power of 2 in X
    - B is the rest of X to make A+B = X
        - B could be 0 or any value greater than 0
- for all values > 0, A > B
    - if B > A, then X could be split into 2A + (B - A), should've be done in
    the first place
    - as A is a power of 2, the single bit that A has is larger than all bits in B
- A stays constant until X becomes 2 * A
    - when X == 2*A, new A becomes 2 * A and B becomes 0
- B has already been processed when X is reached
=> The count of 1 bits in X = 1 + count of 1 bits in B


The solution also satisfies both follow-ups
1. The solution is done in O(N) runtime in a single pass
2. Only list indexing and appending is used, no other built-in functions are used

Runtime: O(N) where N is the input integer n
Space: O(1), memory usage does not depend on input, except for the output list
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        curPowerOfTwo = 0
        nextPowerOfTwo = 1
        ans = [0]

        for num in range(1, n + 1):
            if num == nextPowerOfTwo:
                ans.append(1)
                curPowerOfTwo = nextPowerOfTwo
                nextPowerOfTwo = curPowerOfTwo * 2
            else:
                ans.append(1 + ans[num - curPowerOfTwo])

        return ans