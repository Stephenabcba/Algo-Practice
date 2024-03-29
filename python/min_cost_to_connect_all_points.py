# leetcode problem # 1584. Min Cost to Connect All Points

"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
https://assets.leetcode.com/uploads/2020/08/26/d.png
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
https://assets.leetcode.com/uploads/2020/08/26/c.png
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All pairs (xi, yi) are distinct.
"""

"""
Solution by leetcode user vanAmsen: Prim's algorithm
https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/4045874/94-85-prim-kruskal-with-min-heap/?envType=daily-question&envId=2023-09-15

The problem is essentially looking for a minimum spanning tree connecting all the points.

Prim's algorithm can be used to find a minimum spanning tree
- starts from arbitrary node
- greedily chooses the edge with the smallest weight that connects a visited and an unvisited node
- makes use of a priority queue (heap) to complete the task

Runtime: O(N^2 * logN) where N is the number of points
Space: O(N)


"""

def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap_dict = {0: 0}  
        min_heap = [(0, 0)]
        
        mst_weight = 0
        
        while min_heap:
            w, u = heappop(min_heap)
            
            if visited[u] or heap_dict.get(u, float('inf')) < w:
                continue
            
            visited[u] = True
            mst_weight += w
            
            for v in range(n):
                if not visited[v]:
                    new_distance = manhattan_distance(points[u], points[v])
      
                    if new_distance < heap_dict.get(v, float('inf')):
                        heap_dict[v] = new_distance
                        heappush(min_heap, (new_distance, v))
        
        return mst_weight