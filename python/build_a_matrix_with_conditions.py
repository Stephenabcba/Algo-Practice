# leetcode problem # 2392. Build a Matrix With Conditions

"""
You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

Example 1:
https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.

Example 2:
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.

Constraints:
2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 10^4
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
"""

"""
Solution By Leetcode: DFS

Intuition
During depth-first traversal in a graph, starting from node A, DFS explores all paths stemming from A before completing its recursion for A and moving to other nodes. 
Consequently, all nodes in these paths have A as an ancestor, making A a prerequisite for all paths originating from it.

Now, we know how to get all the integers that have a particular integer as a prerequisite. If a valid ordering of integers is possible, the node A would come before all 
the other sets of integers that have it as a prerequisite. This idea for solving the problem can be explored using a depth-first search.

Initialize a recursive function given by dfs where the recursive stack will contain the topologically sorted order of the courses in our graph. Construct the adjacency 
list from input edge pairs, where [a, b] denotes that course a must precede course b, forming edges a ➔ b in the graph.

For each node in our graph, we will run a depth-first search in case that node was not already visited in some other node's DFS traversal. Once the processing of all 
the neighbors is done, we will add this node to the stack. We are using the recursion stack to simulate the ordering we need.

Once all the nodes have been processed, we will return the nodes as they are returned in the recursion stack from top to bottom.

Now that we have topologically sorted arrays for both rowConditions and colConditions, how can we utilize them to construct the matrix? Each row and column should 
correspond to their respective sorted arrays. Therefore, the value at position matrix[i][j] is derived from rowConditions[i] and colConditions[j].

Runtime: O(max(k * k, n)) where k is the input integer k, and n is the length of the conditions
Space: O(max(k * k, n))
"""


class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> List[List[int]]:
        # Store the topologically sorted sequences.
        order_rows = self.__topoSort(rowConditions, k)
        order_columns = self.__topoSort(colConditions, k)

        # If no topological sort exists, return empty array.
        if not order_rows or not order_columns:
            return []
        matrix = [[0] * k for _ in range(k)]
        pos_row = {num: i for i, num in enumerate(order_rows)}
        pos_col = {num: i for i, num in enumerate(order_columns)}

        for num in range(1, k + 1):
            if num in pos_row and num in pos_col:
                matrix[pos_row[num]][pos_col[num]] = num
        return matrix

    def __topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = defaultdict(list)
        order = []
        visited = [0] * (n + 1)
        has_cycle = [False]

        # Build adjacency list
        for x, y in edges:
            adj[x].append(y)
        # Perform DFS for each node
        for i in range(1, n + 1):
            if visited[i] == 0:
                self.__dfs(i, adj, visited, order, has_cycle)
                # Return empty if cycle detected
                if has_cycle[0]:
                    return []
        # Reverse to get the correct order
        order.reverse()
        return order

    def __dfs(
        self,
        node: int,
        adj: defaultdict,
        visited: List[int],
        order: List[int],
        has_cycle: List[bool],
    ):
        # Mark node as visiting
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.__dfs(neighbor, adj, visited, order, has_cycle)
                # Early exit if a cycle is detected
                if has_cycle[0]:
                    return
            elif visited[neighbor] == 1:
                # Cycle detected
                has_cycle[0] = True
                return
        # Mark node as visited
        visited[node] = 2
        # Add node to the order
        order.append(node)
