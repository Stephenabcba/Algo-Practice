# leetcode problem # 2073. Time Needed to Buy Tickets

"""
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

Example 1:
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

Example 2:
Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.

Constraints:
n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
"""

"""
My solution: Not using a queue

Observation: If the person at position k needs to buy X tickets:
- every person in front of them need to buy X tickets for it it be person k's turn to buy the last ticket
    - if any person only needs to buy Y tickets, where Y < X, then only Y tickets are bought
- every person behind them need to buy X - 1 tickets, so the queue keeps moving
    - if any person only needs to buy Z tickets, where Z < X - 1, then only Z tickets are bought

Runtime: O(N) where N is the number of tickets
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        target = tickets[k]

        for idx, ticket in enumerate(tickets):
            if idx <= k:
                ans += min(target, ticket)
            else:
                ans += min(target - 1, ticket)
        return ans
