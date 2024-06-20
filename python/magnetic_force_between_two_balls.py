# leetcode problem # 1552. Magnetic Force Between Two Balls

"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Example 1:
https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:
Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.

Constraints:
n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
"""

"""
My solution: Binary Search

Idea: Make a guess (X) to the correct answer, then check
- To check, place a ball at the smallest position, then try to place a ball at every X interval
    - the intervals must be greater than or equal to X, otherwise skip the position to place at the next position
    - if at least m balls can be placed, the answer is greater than or equal to X
    - otherwise, the answer is smaller than X
-> Binary search allows half the solution space to be eliminated every iteration

Logic:
1. Sort the position list to allow binary search
2. Binary search for the highest minimum magnetic force
    - the minimum space is 1, and the maximum spacing is (range of position list) / (m - 1)
        - the maximum spacing is when all balls are evenly spaced from the smallest position to the highest position
    - the spacing to check is rounded up every time
    * If m == 2, then simply place the balls at the smallest and the largest positions
3. Return the found result

Runtime: O(N*logM) where N is the length of position list, and M is the range of position list
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]

        N = len(position)

        low = 0
        high = (position[-1] - position[0]) // (m - 1)

        while low < high:
            mid = math.ceil((low + high) / 2)
            ballsPlaced = 1
            idx = 1
            prev = position[0]
            while idx < N:
                if position[idx] >= prev + mid:
                    ballsPlaced += 1
                    prev = position[idx]
                idx += 1
            if ballsPlaced >= m:
                low = mid
            else:
                high = mid - 1

        return high
