# leetcode problem # 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Example 1:
https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:
https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

Constraints:
2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""

"""
My solution: Dijkstra's Algorithm

Dijkstra's logic from: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/#

Using Dijkstra's algorithm, the shortest path to each node can be found
- as the graph is weighted, BFS is unable to find the shortest paths
- the shortest paths can be used to determine whether two cities are connected within the threshold

Dijkstra's Logic:
- Initialization:
    - Distances to all nodes are initially infinite
    - The distances to the starting node is 0
    - The SPT set starts empty
- In each iteration:
    - Add a node to the shortest spanning tree set (SPT set)
        - the node is the node with the shortest distance to any node in the tree
    - Perform "Edge relaxation"
        - from the node, reduce the distance to all connected nodes if possible

Problem Specific Logic:
- Keep track of the city with the least connections
- Perform Dijkstra's algorithm on each city
- Count the number of connected cities after Dijkstra's algorithm is complete
- Update the city with the least connections when needed

Runtime: O(N^3) where N is the number of cities
Space: O(N^2)
"""


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        cityConnections = [[0 for _ in range(n)] for __ in range(n)]
        for city1, city2, distance in edges:
            cityConnections[city1][city2] = distance
            cityConnections[city2][city1] = distance

        lowestCity = 0
        lowestConnections = 100
        for city in range(n):
            distances = [distanceThreshold + 1] * n
            distances[city] = 0
            connections = 0
            sptSet = [False] * n
            for _ in range(n):
                newCity = -1
                shortest = distanceThreshold + 1
                for x in range(n):
                    if distances[x] < shortest and sptSet[x] == False:
                        newCity = x
                        shortest = distances[x]
                sptSet[newCity] = True

                for y in range(n):
                    if cityConnections[newCity][y] > 0 and sptSet[y] == False and distances[y] > distances[newCity] + cityConnections[newCity][y]:
                        distances[y] = distances[newCity] + \
                            cityConnections[newCity][y]
            for curCity in range(n):
                if distances[curCity] <= distanceThreshold:
                    connections += 1

            if connections <= lowestConnections:
                lowestCity = city
                lowestConnections = connections

        return lowestCity
