# leetcode problem # 435. Non-overlapping Intervals

"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""

"""
My Solution: Sort then use stack

Idea: 
1. sort the intervals in increasing order for the starting value, then decreasing order for the
ending value.
2. using a stack, keep track of the ending values of the included intervals
3. Iterate through each interval
    i. remove all intervals that have higher ending values than the new interval
        - increase the number of removed intervals by 1 for each interval removed
    ii. include the new interval if the start value of the interval is larger than the ending interval of the included intervals
    iii. otherwise, don't include the new interval
        - increase the number of removed intervals by 1

Runtime: O(N * logN) where N is the number of intervals
Space: O(N)
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:[x[0], -x[1]])
        stack = []
        removeCount = 0

        nextInterval = False
        for interval in intervals:
            nextInterval = False
            if len(stack) == 0:
                stack.append(interval[1])
            else:
                while stack[-1] > interval[1]:
                    stack.pop()
                    removeCount += 1
                    if len(stack) == 0:
                        stack.append(interval[1])
                        nextInterval = True
                        break
                if not nextInterval:
                    if stack[-1] <= interval[0]:
                        stack.append(interval[1])
                    else:
                        removeCount += 1
        return removeCount

"""
Solution by leetcode: just sort

After sorting by the ending interval, greedily choose the smaller ending interval
- if the new interval doesn't overlap with the current highest interval, include the new interval
- otherwise, don't include the new interval to keep the highest interval minimal

Runtime: O(N * logN) where N is the number of intervals
Space: O(N), or depending on the sorting logic.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans = 0
        k = -inf
        
        for x, y in intervals:
            if x >= k:
                # Case 1
                k = y
            else:
                # Case 2
                ans += 1
        
        return ans