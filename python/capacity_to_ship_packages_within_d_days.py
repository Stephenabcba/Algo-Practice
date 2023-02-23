# leetcode problem # 1011. Capacity To Ship Packages Within D Days

"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1


Constraints:
1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500
"""

"""
My solution: Binary search

Observation:
1. The capacity required is at its lowest when there are more days than packages available
    - the conveyor belt can ship 1 package a day and still meet the deadline.
    - the capacity needed only needs to fit the heaviest package in the list
2. The capacity required is at its highest when only 1 day is given to ship all the packages
    - All packages must be put on the belt in a single day
    - the capacity needed is the total weight of all packages
Thus, the capacity of the ship must be between [maxPackageWeight, totalWeight]

Using binary search, half of the solution space can be eliminated every iteration.
1. check the number of days it takes to ship all packages with the weight at middle of the range
2. compare the number of days in step 1 to the days limit given
    - if the required days exceeds the day limit, the belt capacity must be raised
    - if the required days is under or equal to the day limit, the belt capacity is either correct or can be lowered
3. repeat steps 1 and 2 until only 1 value remains in the solution space

Runtime: O(N * log N) where N is the length of the weights list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = max(weights)
        upper = sum(weights)

        while upper >= lower + 1:
            middle = (lower + upper) // 2
            requiredDays = 1
            idx = 0
            curWeight = 0
            while idx < len(weights):
                if curWeight + weights[idx] > middle:
                    requiredDays += 1
                    curWeight = 0
                curWeight += weights[idx]
                idx += 1
            if requiredDays <= days:
                upper = middle
            else:
                lower = middle + 1

        return lower
