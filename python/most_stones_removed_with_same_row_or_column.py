# leetcode problem # 947. Most Stones Removed with Same Row or Column

"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


Constraints:
1 <= stones.length <= 1000
0 <= xi, yi <= 10^4
No two stones are at the same coordinate point.
"""

"""
Solution in Leetcode discussion (solution) by md2030: BFS

Preprocessing: save information such that searching by x and y
    values provide all the stones with the given x/y value

BFS to search for the number of "connected components"
- everytime a new BFS is started on a new node, a connected component is created
    -> it was impossible to reach the node from previous BFS searches
- for each connected component, there will be 1 stone that cannot be removed.

The answer becomes the total number of stones - total number of connected components

Runtime: O(N) for the number of stones in stones list
Space: O(N) for the number of stones in stones list
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # construct graph
        # Uing two hash map to store the neighbors on the x-axis and y-axis
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        for x, y in stones:
            graphX[x].append(y)
            graphY[y].append(x)

        # For each stone, if we haven't seen it before, use a BFS to find all stones connects to it
        # For each connected component, there will always be 1 stone that can not be removed
        # so once we know the number of connected component,
        # we can subtract it from totoal number of stones to find the number of removed stones
        connectedComponent = 0
        # each stone should only be visited once.
        visited = set()
        for x, y in stones:
            # if the current stone has not been visited, do a BFS from it.
            if (x, y) not in visited:
                q = deque([(x, y)])
                while q:
                    xo, yo = q.popleft()
                    # check to see if the current stone has been visited,
                    # if not, get its neighbors
                    if (xo, yo) not in visited:
                        visited.add((xo, yo))
                        # since we used two hash map to store the neighbors,
                        # we need to get all the neighbors fron the current stone.
                        for neiY in graphX[xo]:
                            q.append((xo, neiY))
                        for neiX in graphY[yo]:
                            q.append((neiX, yo))
                # we find another connected component
                connectedComponent += 1

        return len(stones)-connectedComponent
