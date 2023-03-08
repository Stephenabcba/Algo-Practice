# leetcode problem # 875. Koko Eating Bananas

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

"""
My solution: binary search

Observations:
1. From problem constraints, it is known that Koko can finish all piles of bananas if she eats
1 pile per hour before the guards return
2. At the minimum, Koko must eat at least 1 banana an hour to make any progress on finishing the bananas
=> From 1 and 2, the minimum k to eat each hour should be between 1 and max(piles)

Using binary search, the alogrithm can make guesses at k, using the average of the current range
- check whether Koko can finish all the bananas at the guessed rate k
    - if she can finish all the bananas, the minimum K is less than or equal to the guessed K
    - if she can't finish all the banas, the minimum K must be higher than the guessed K
Repeat until the range is minimized to 1 possible value of K


Runtime: O(N * logM) where N is the length of piles list and M is the maximum bananas in a pile
Space: O(1), memory usage does not depend on input
"""




from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            hoursTaken = 0
            for pile in piles:
                hoursTaken += ceil(pile / mid)
            if hoursTaken > h:
                low = mid + 1
            else:
                high = mid
        return low
