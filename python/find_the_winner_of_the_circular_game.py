# leetcode problem # 1823. Find the Winner of the Circular Game

"""
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.

Example 1:
https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png
Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

Example 2:
Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

Constraints:
1 <= k <= n <= 500

Follow up:
Could you solve this problem in linear time with constant space?
"""

"""
My solution: Simulation using queue

The game can be simulated using a queue

Logic:
1. queue every person from 1 to N
2. move the first k - 1 person to the back of the queue
3. remove the kth person from the queue
4. repeat steps 2 and 3 until there's only 1 person left
    - in total, there are N - 1 rounds to eliminate N - 1 people
5. Return the last remaining person as the winner

Slight Optimization: when the number of people left over (N) is smaller than k, instead of
moving people through the queue multiple times, only k % N moves is needed

Runtime: O(N * K) where N and K are the input integers n and k
Space: O(N)
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([idx + 1 for idx in range(n)])

        for turn in range(n - 1):
            modK = (k - 1) % len(q) + 1

            for person in range(modK - 1):
                q.append(q.popleft())
            q.popleft()

        return q[0]


"""
Solution by leetcode: Iterative

Converts the recurrence relation into an iterative one to eliminate the need for recursion overhead
- Starts from the base case and works backwards from 2 to N

Original Recurrence Relation:
    Base Case: f(1,k) = 0
    Recursive Case: f(n,k) = (f(n-1,k) + k) % n

Runtime: O(N)
Space: O(1)
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        # add 1 to convert back to 1 indexing
        return ans + 1
