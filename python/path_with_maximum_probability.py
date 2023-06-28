# leetcode problem # 1514. Path with Maximum Probability

"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
https://assets.leetcode.com/uploads/2019/09/20/1558_ex1.png
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
https://assets.leetcode.com/uploads/2019/09/20/1558_ex2.png
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
https://assets.leetcode.com/uploads/2019/09/20/1558_ex3.png
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:
2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""

"""
My attempt 1: DFS

Attempted to use dfs to find the highest probability.
Failed due to not finding the correct values in some cases.

Runtime: O(N^2) where N is the number of nodes
Space: O(N^2)
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edgesDict = {}

        probabilities = [0 for _ in range(n)]
        visited = [False for _ in range(n)]

        for idx, [node1, node2] in enumerate(edges):
            edgesDict[node1] = edgesDict.get(node1, [])
            edgesDict[node1].append((node2, succProb[idx]))
            edgesDict[node2] = edgesDict.get(node2, [])
            edgesDict[node2].append((node1, succProb[idx]))


        def dfs(node, probability):
            if node == end:
                return probability
            visited[node] = True
            bestRate = 0
            for connectedNode, successRate in edgesDict.get(node, []):
                if visited[connectedNode] == False:
                    bestRate = max(dfs(connectedNode, successRate), bestRate)
                else:
                    bestRate = max(bestRate, probabilities[connectedNode] * successRate)
            probabilities[node] = bestRate
            return bestRate * probability

        dfs(start, 1)

        return probabilities[start]

"""
My attempt 2: BFS from the end

Failed; the outcome probability is lower than expected sometimes still

Runtime: O(N^2) where N is the number of nodes
Space: O(N^2)
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edgesDict = {}

        probabilities = [0 for _ in range(n)]
        visited = [False for _ in range(n)]

        for idx, [node1, node2] in enumerate(edges):
            edgesDict[node1] = edgesDict.get(node1, [])
            edgesDict[node1].append((node2, succProb[idx]))
            edgesDict[node2] = edgesDict.get(node2, [])
            edgesDict[node2].append((node1, succProb[idx]))


        queue = [end]
        visited[end] = True
        probabilities[end] = 1
        queueIdx = 0

        while queueIdx < len(queue):
            curNode = queue[queueIdx]
            queueIdx += 1
            for connectedNode, successRate in edgesDict.get(curNode, []):
                if probabilities[connectedNode] < successRate * probabilities[curNode]:
                    probabilities[connectedNode] = successRate * probabilities[curNode]
                if not visited[connectedNode]:
                    visited[connectedNode] = True
                    queue.append(connectedNode)
    

        return probabilities[start]
    

"""
Solution by leetcode: Dijkstra's Algorithm

-> BFS doesn't find the shortest path in weighted graphs

Runtime: O(M + N*logN) for N nodes and M edges
Space: O(N + M)
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        max_prob = [0.0] * n
        max_prob[start] = 1.0
        
        pq = [(-1.0, start)]    
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:

                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        return 0.0