# leetcode problem # 1921. Eliminate Maximum Number of Monsters

"""
You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

Example 1:
Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.
All 3 monsters can be eliminated.

Example 2:
Input: dist = [1,1,2,3], speed = [1,1,1,1]
Output: 1
Explanation:
In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.

Example 3:
Input: dist = [3,2,4], speed = [5,3,2]
Output: 1
Explanation:
In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.

Constraints:
n == dist.length == speed.length
1 <= n <= 10^5
1 <= dist[i], speed[i] <= 10^5
"""

"""
My solution: Kill based on time from city

Idea: The monster that reaches the city the soonest must be eliminated first
- As their speed is constant, the time to reach the city can be found by dividing distance by speed

Logic:
1. Find the initial time to reach the city for each monster
2. Sort the monsters based on their time from city
3. Iterate and find out which monsters to kill
    - the first monster is always killed
        - the attack is charged at time 0, and the monster cannot be at the city at time 0
    - the number of monsters killed is also the time from start of when the next shot is ready
        - if the shot is ready before the next monster arrives, shoot the monster and move to the next
        - if the monster has reached the city when the shot is ready, the game is over
            - end iteration if this is the case
4. Return the number of monsters killed

Runtime: O(N * logN) where N is the number of monsters
Space: O(N)
"""


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        timeFromCity = []

        for idx in range(len(dist)):
            timeFromCity.append(dist[idx] / speed[idx])

        timeFromCity.sort()

        monstersKilled = 1

        for idx in range(1, len(timeFromCity)):
            if timeFromCity[idx] <= monstersKilled:
                break
            else:
                monstersKilled += 1

        return monstersKilled
