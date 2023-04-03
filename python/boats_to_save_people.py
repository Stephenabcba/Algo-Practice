# leetcode problem # 881. Boats to Save People

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.


Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Constraints:
1 <= people.length <= 5 * 10^4
1 <= people[i] <= limit <= 3 * 10^4
"""

"""
My solution: Sort then count

Observation 1: To minimize the number of boats used, the number of boats with 2 people
on them should be maximized, with the remaining people on 1 boat each.
-> To do so, the heaviest person remaining should be attempted to be matched with the
lightest person remaining
    - if their combined weight is lower than (or equal to) the limit, put them on a boat
    - if their combined weight is higher than the limit, put the heaviest person on a boat
    - repeat until everyone is on a boat

By sorting the people by their weight beforehand, the heaviest and the lightest person at any
given time can be found in O(1) time when using a two-pointer approach

Runtime: O(N*logN) where N is the number of people to be placed on boats
Space: O(1), memory usage does not depend on input (assuming sort is done in-place)
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        front = 0
        back = len(people) - 1
        boats = 0

        while (front <= back):
            if people[front] + people[back] <= limit:
                front += 1
            back -= 1
            boats += 1

        return boats
