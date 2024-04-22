# leetcode problem # 752. Open the Lock

"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

Constraints:
1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

"""
My solution: BFS

The lock can be seen as a 4-dimensional maze, where a move is a change in one of the dimensions
Each deadend is a block in the maze that cannot be accessed

Using Breadth-First Search, the program can find the shortest path from the start of the maze (0,0,0,0) to the target
- The first time any position is reached by BFS is one of the shortest path to the position
    - there may be multiple shortest paths of the same length
- BFS takes the first item in the queue, and add all accessible unexplored items to the back of the queue
    - this is repeated until the target is found or all accessible paths have been taken

Runtime: O(1), runtime does not depend on input
- although the time taken does depend on input, the loops are restricted to run for at most 10,000 times
- the runtime depends more on the problem constraints than the input
Space: O(1)
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dp = [[[[100000 for _ in range(10)] for __ in range(
            10)] for ___ in range(10)] for ____ in range(10)]
        for deadend in deadends:
            first, second, third, fourth = int(deadend[0]), int(
                deadend[1]), int(deadend[2]), int(deadend[3])
            dp[first][second][third][fourth] = -1

        t1, t2, t3, t4 = int(target[0]), int(
            target[1]), int(target[2]), int(target[3])
        queue = deque()

        if dp[0][0][0][0] != -1:
            queue.append((0, 0, 0, 0))
            dp[0][0][0][0] = 0

        while len(queue) > 0:
            first, second, third, fourth = queue.popleft()
            steps = dp[first][second][third][fourth]
            if first == t1 and second == t2 and third == t3 and fourth == t4:
                return dp[t1][t2][t3][t4]

            if dp[(first + 1) % 10][second][third][fourth] > steps + 1:
                dp[(first + 1) % 10][second][third][fourth] = steps + 1
                queue.append(((first + 1) % 10, second, third, fourth))

            if dp[(first - 1) % 10][second][third][fourth] > steps + 1:
                dp[(first - 1) % 10][second][third][fourth] = steps + 1
                queue.append(((first - 1) % 10, second, third, fourth))

            if dp[first][(second + 1) % 10][third][fourth] > steps + 1:
                dp[first][(second + 1) % 10][third][fourth] = steps + 1
                queue.append((first, (second + 1) % 10, third, fourth))

            if dp[first][(second - 1) % 10][third][fourth] > steps + 1:
                dp[first][(second - 1) % 10][third][fourth] = steps + 1
                queue.append((first, (second - 1) % 10, third, fourth))

            if dp[first][second][(third + 1) % 10][fourth] > steps + 1:
                dp[first][second][(third + 1) % 10][fourth] = steps + 1
                queue.append((first, second, (third + 1) % 10, fourth))

            if dp[first][second][(third - 1) % 10][fourth] > steps + 1:
                dp[first][second][(third - 1) % 10][fourth] = steps + 1
                queue.append((first, second, (third - 1) % 10, fourth))

            if dp[first][second][third][(fourth + 1) % 10] > steps + 1:
                dp[first][second][third][(fourth + 1) % 10] = steps + 1
                queue.append((first, second, third, (fourth + 1) % 10))

            if dp[first][second][third][(fourth - 1) % 10] > steps + 1:
                dp[first][second][third][(fourth - 1) % 10] = steps + 1
                queue.append((first, second, third, (fourth - 1) % 10))

        return -1
