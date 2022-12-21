# leetcode problem # 886. Possible Bipartition

"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 10^4
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
"""

"""
My Solution: BFS

The problem can be framed as a graph problem where each person is a node, and each
dislike relationship is an edge.
- There is an added requirement where the nodes are split into 2 groups, and every
    edge must connect nodes that are not in the same group

Using BFS, the graph can be traversed and mapped accordingly
- Each node is placed in one of two groups, and all nodes connected to the node
    must be placed in the other group
- It might be necessary to initiate BFS multiple times, as it's possible that some
    nodes are completely disconnected from other nodes

Using a dictionary, the dislikes list can be converted into a data structure where
finding all people that a person dislikes can be done in constant time.
- Although the dislikes list seems to be an one-way relationship, the link has to
    be created both in both directions as person A cannot be in the same group
    as person B, regardless of whether person A or person B was placed in a group
    first.

If the graph can be constructed without conflict (edges connecting nodes in the same
group), return True
    otherwise, return False

Time: O(N) where N is the input integer n, which is the number of people in the group
Space: O(N + M) where N is the input integer n and M is the length of dislikes list
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislikesDict = {}
        for dislike in dislikes:
            if dislike[0] - 1 not in dislikesDict:
                dislikesDict[dislike[0] - 1] = []
            if dislike[1] - 1 not in dislikesDict:
                dislikesDict[dislike[1] - 1] = []
            dislikesDict[dislike[0] - 1].append(dislike[1] - 1)
            dislikesDict[dislike[1] - 1].append(dislike[0] - 1)

        visited = [0 for _ in range(n)]

        for node in range(n):
            if visited[node] == 0:
                queue = []
                queueIdx = 0
                queue.append(node)
                visited[node] = 1

                while queueIdx < len(queue):
                    curNode = queue[queueIdx]
                    queueIdx += 1
                    for dislike in dislikesDict.get(curNode, []):
                        if visited[dislike] == 0:
                            if visited[curNode] == 1:
                                visited[dislike] = 2
                            else:
                                visited[dislike] = 1
                            queue.append(dislike)
                        elif visited[dislike] == visited[curNode]:
                            return False
        return True
