# leetcode problem # 1870. Minimum Speed to Arrive on Time

"""
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 10^7 and hour will have at most two digits after the decimal point.

Example 1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

Example 2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example 3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.

Constraints:
n == dist.length
1 <= n <= 10^5
1 <= dist[i] <= 10^5
1 <= hour <= 10^9
There will be at most two digits after the decimal point in hour.
"""

"""
My solution: Binary Search

Observation: due to the limitations of the train, all trains (except the last) take a minimum of 1 hour
to reach the next train
    - all trains (except the last) must be take in increments of hours
    - the last train can arrive at work in fractions of an hour below 1 hour.
-> The minimum time needed to take all trains (after taking a ceiling function) must not be
lower than the number of trains.

Intuition: Make a guess at the minimum speed, and check if the speed can meet the requirements
- The problem definition limits the train speed from 1 to 1e7 (inclusive), and the guesses can
be structured to eliminate half the solution space with each guess
    -> binary search can be used
- To check if the speed is sufficient, calculate the time it takes by going through each train
and divide the distance by speed.
- if the speed is sufficient, the minimum speed is equal to or lower than the current speed
- if the speed is insufficent, the minimum speed is larger than the current speed

Runtime: O(N * logM) where N is the number of trains and M is the maximum speed
    - in the current case, M is capped at 10^7, and is technically a constant
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if ceil(hour) < len(dist):
            return -1

        low = 1
        high = 10000000

        while low < high:
            mid = (low + high) // 2
            time = 0
            for idx in range(len(dist) - 1):
                time += ceil(dist[idx] / mid)
            time += dist[-1] / mid
            if time < hour:
                high = mid
            elif time > hour:
                low = mid + 1
            else:
                return mid

        return low
                