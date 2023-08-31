# leetcode problem # 1326. Minimum Number of Taps to Open to Water a Garden

"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

Example 1:
https://assets.leetcode.com/uploads/2020/01/16/1685_example_1.png
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]

Example 2:
Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.


Constraints:
1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
"""

"""
My solution: Greedy solution with 2 stacks

Idea:
- Open a tap if it covers a radius > 0 and a portion of garden previously not covered
- Close a previously opened tap if the area it covers are overlapped by other taps.

Criteria for a collection of taps to cover the whole garden:
1. The taps should cover the land up to N
2. There should not be any unwatered portion in the garden
-> if either criteria is violated, the garden is not fully watered; return -1

Note: the entire garden should be watered, not just the locations where the taps are
-> any tap with a radius of 0 does not offer any area of coverage, and should never be included

Logic:
1. Keep track of the areas covered in a stack -> "stack" stack
2. Keep track of portions of areas not covered in another stack-> unIncluded stack
3. Iterate through each tap
    i. the very first tap should be opened
    ii. for all other taps, only process taps with a non-zero radius
    iii. if opening the current tap leaves unwatered area, add the first unwatered area to the
    unIncluded stack
        - only the first unwatered area needs to be marked, since another tap to the right could water all
        unwatered areas if it can water the first unwatered area.
    iv. close all previous taps with areas that the current tap can cover
    v. open the tap if it covers previously uncovered areas
        - this includes areas newly uncovered after closing taps
4. If the garden cannot be fully watered (see above), return -1
5. Otherwise, return the number of taps opened


Runtime: O(N) where N is the input integer n
Space: O(N)
"""

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        stack = [0]
        unIncluded = []
        for idx, tap in enumerate(ranges):
            if len(stack) == 1:
                stack.append(idx + tap)
            elif tap > 0:
                tapMin = idx - tap
                tapMax = min(idx + tap, n)
                if tapMin > stack[-1]:
                    unIncluded.append(stack[-1])
                if tapMax >= stack[-1]:
                    while len(unIncluded) > 0 and tapMin <= unIncluded[-1]:
                        unIncluded.pop()
                    while len(stack) >= 2 and tapMin <= stack[-2]:
                        stack.pop()
                    if tapMax > stack[-1]:
                        stack.append(tapMax)

        if stack[-1] < n or len(unIncluded) > 0:
            return -1
        return len(stack) - 1