# leetcode problem # 926. Flip String to Monotone Increasing

"""
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.
"""

"""
My Solution: Greedy Algorithm

Intuition:
- The resulting string must have 0's first and 1's after
    - By greedily changing 1's to 0's instead of 0's to 1's, the values that come after can still be
        changed to 0's (changing 0's to 1's would require all remaining values be changed to 1's)
- if a continuous substring beginning with 1 has more 0's than 1's, it takes fewer changes if all 1's
    are changed to 0's
- At the end, if the substring has more 1's than 0's, then change the 0's to 1's

* Leading 0's do not need to be changed

Runtime: O(N) where N is length of string s
Space: O(1), memory usage does not depend on input.
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0

        countZeros = False

        zeroCount = 0
        oneCount = 0

        for number in s:
            if number == '0':
                if countZeros:
                    zeroCount += 1
            else:
                countZeros = True
                if zeroCount >= oneCount:
                    # greedily change 1 to 0 if it takes fewer changes
                    ans += oneCount
                    zeroCount = 0
                    oneCount = 0
                oneCount += 1

        # make the final change, where it's possible to change from 0 to 1
        ans += min(zeroCount, oneCount)

        return ans
