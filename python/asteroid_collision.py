# leetcode problem # 735. Asteroid Collision

"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

"""
My solution: use a stack to manage the asteroids

A stack can be used to main a record of currently encountered asteroids that have not been destroyed yet.
When a new asteroid is encountered, there are multiple cases that could happen
1. the stack is 0, there's no asteroid to collide yet
    -> add the asteroid to the stack
2. the asteroid is going to the right
    - the stack is to the left of the asteroid, there's nothing to collide
    -> add the asteroid to the stack
3. the last asteroid in the stack is going to the left
    - this suggests that all asteroids in the stack are going to the left
        - otherwise, they would have collided already
    - if all the asteroids are going to the left, there's nothing to collide
    -> add the asteroid to the stack
4. the last asteroid in the stack is going to the right, and the current asteroid is going to the left
    - there are 3 subcases:
        i. the asteroids are the same size
            - both asteroids are destroyed
            -> remove the last asteroid in the stack and don't add the new one
        ii. the new asteroid is larger
            - the last asteroid in the stack is destroyed
            -> remove the last asteroid in the stack
            -> check if the new asteroid is going to collide with other asteroids in the stack
                - if they do, check these 3 subcases again
        iii. the last asteroid in the stack is larger
            - the new asteroid is destroyed
            -> the stack remains unchanged

At the end, return the stack as it holds all remaining asteroids

Although the while loop is nested inside the for loop, the while loop could only run for a total of N times
- there is at most N asteroids that could be added to the stack, and thus could only be removed N times

A list can be used as a stack using append() and pop()

Runtime: O(N) where N is the number of asteroids
Space: O(N)
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if len(stack) == 0 or asteroid > 0 or stack[-1] < 0:
                stack.append(asteroid)
            else:
                if stack[-1] == -asteroid:
                    stack.pop()
                elif stack[-1] < -asteroid:
                    stack.pop()
                    addAsteroid = True
                    while len(stack) > 0 and stack[-1] > 0:
                        if stack[-1] == -asteroid:
                            stack.pop()
                            addAsteroid = False
                            break
                        elif stack[-1] < -asteroid:
                            stack.pop()
                        elif stack[-1] > -asteroid:
                            addAsteroid = False
                            break
                    if addAsteroid:
                        stack.append(asteroid)

        return stack