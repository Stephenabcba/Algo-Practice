# leetcode problem # 


"""
Solution by leetcode: top down dynamic programming

The algorithm uses two DP arrays length and count
    - the values are only computed the first time
        - in all subsequent calls, no extra processing is done
length[i] is the length of the longest increasing subsequence up to index i
count[i] is the number of LIS with length[i]

With top down DP, the algorithm checks all the previous sequence chains for any chains that could be extended
by the current value.
- Keep count of the number of chains that connect up to the longest length with the current value

In the end, find the length of the LIS and the count of sequences with that length.

Runtime: O(N^2)
Space: O(N)
"""


class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        length = [0] * n
        count = [0] * n

        def calculate_dp(i):
            if length[i] != 0:
                return

            length[i] = 1
            count[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    calculate_dp(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = 0
        result = 0
        for i in range(n):
            calculate_dp(i)
            max_length = max(max_length, length[i])

        for i in range(n):
            if length[i] == max_length:
                result += count[i]

        return result