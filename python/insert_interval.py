# leetcode problem # 57. Insert Interval

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

"""
My solution: binary search then merge

Pseudo Code:
1. Find where the new Interval should be inserted
- this can be done with binary search
2. Check if the interval needs to be merged with the interval before
- the new interval will merge with at most one interval before it
3. merge the new interval with the intervals after as necessary

Special Cases:
1. the new interval could be completely within another interval
    - no change is made
2. the new interval could be added as the last interval
    - due to how the binary search is set up, the found index is at
        an interval with start value larger than the new interval
        - a special check has to be made if the index is at the last
            index
3. an interval could be added to an empty list
    - if the intervals list was originally empty, the extra steps
        do not need to be done

Runtime: O(N^2), where N is the length of the intervals list
- it is possible that the new interval is inserted at the start of the list
    and merged with the rest of the entire list, which requires all other
    values to be removed.
Space: O(1), memory usage does not scale with input
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        start = 0
        end = len(intervals) - 1
        middle = (start + end) // 2

        while start < end:
            if intervals[middle][0] > newInterval[0]:
                end = middle
            elif intervals[middle][0] < newInterval[0]:
                start = middle + 1
            else:
                break
            middle = (start + end) // 2

        if middle == len(intervals) - 1:
            if newInterval[0] > intervals[-1][0]:
                middle += 1

        if middle == 0:
            intervals.insert(0, newInterval)
        elif newInterval[0] <= intervals[middle - 1][1]:
            intervals[middle -
                      1][1] = max(newInterval[1], intervals[middle - 1][1])
            middle -= 1
        else:
            intervals.insert(middle, newInterval)

        while middle < len(intervals) - 1 and intervals[middle][1] >= intervals[middle + 1][0]:
            intervals[middle][1] = max(
                intervals[middle][1], intervals[middle + 1][1])
            intervals.pop(middle + 1)

        return intervals
