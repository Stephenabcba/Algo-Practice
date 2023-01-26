# leetcode problem # 787. Cheapest Flights Within K Stops

"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


Example 1:
https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 10^4
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""

"""
My Solution: BFS with steps limit

Intuition:
Starting from the source city, explore all flight paths that are at most K steps from the city
Find the cheapest path from source city to destination city

Modifying BFS: 
-In the queue, keep track of the number of steps taken to reach the current city
-Do not traverse further if it has already taken k steps to reach the current city

Optimization:
- Keep track of the shortest flight with the cheapest price to reach any city
- If the current flight takes longer AND is more expensive than the recorded flight,
    don't continue processing the flight
    -> the previous flight could've completed the trip for cheaper and in shorter time


Runtime: O(N^2) where N is number of cities
Space: O(N)
"""




from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        lowestPrice = float('inf')
        distances = [[float('inf'), float('inf')] for _ in range(n)]

        outBoundFlights = {}
        for flight in flights:
            outBoundFlights[flight[0]] = outBoundFlights.get(flight[0], [])
            outBoundFlights[flight[0]].append((flight[1], flight[2]))

        q = deque()
        q.append((src, 0, 0))
        distances[src] = [0, 0]

        while len(q) > 0:
            curNode, curPrice, steps = q.popleft()
            for flight in outBoundFlights.get(curNode, []):
                if flight[0] == dst:
                    lowestPrice = min(lowestPrice, curPrice + flight[1])
                elif steps + 1 <= k and curPrice + flight[1] < lowestPrice:
                    curShortest = distances[flight[0]]
                    if curPrice + flight[1] <= curShortest[0] or steps + 1 <= curShortest[1]:
                        q.append((flight[0], curPrice + flight[1], steps + 1))
                        if curPrice + flight[1] <= curShortest[0] and steps + 1 <= curShortest[1]:
                            distances[flight[0]] = [
                                curPrice + flight[1], steps + 1]

        return lowestPrice if lowestPrice < float('inf') else -1
