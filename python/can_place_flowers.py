# leetcode problem # 605. Can Place Flowers

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

"""
My solution: greedily plant the flowers

Intuition: By greedily planting the flowers in the first available space, the number of flowers that can be planted is maximized
- the greedy method does not decrease the number of plantable flowers
ex: [1,0,0,0,0,1]
greedy: [1,0,1,0,0,1]
alternative: [1,0,0,1,0,1]
both have planted 1 flower, the only difference is the location planted.

Logic:
1. Iterate through all the spaces
    - Check the space and the spaces before and after to make sure that they are all empty (all == 0)
    - if they are all empty, plant a flower (change the space to 1)
        - there is 1 fewer flower to plant, decrement n by 1
2. At the end, if there is no more flowers to plant (n <= 0), return True
- otherwise, return False

Runtime: O(N) where N is the length of the flowerbed
Space: O(1) memory usage does not depend on input
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for idx, flower in enumerate(flowerbed):
            if flower == 0:
                if idx > 0:
                    if flowerbed[idx - 1] == 1:
                        continue
                if idx < len(flowerbed) - 1:
                    if flowerbed[idx + 1] == 1:
                        continue
                n -= 1
                flowerbed[idx] = 1

        return n <= 0
