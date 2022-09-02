// leetcode problem # 785. Is Graph Bipartite?

/*
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
*/


/*
Solution from leet code discussion by hi-ravi (originally written in c++)
BFS solution:
Assume all nodes are initially "uncolored" (value of 0 at the index in the colors array)
    - the node can then be colored to be either 1 or -1
        - corresponds to set A and set B in the problem statement.

Perform a BFS on all uncolored nodes
    - the BFS will color all nodes a given node is connected to
    - if a directly connected node is the same color as a given node, the graph is not biparte, return false
    - the BFS might have to be run more than once, due to possibility of disconnected graphs
If the logic above executed successfully without conflicts, the graph is biparte, return true.
*/

/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function (graph) {
    let length = graph.length
    let colors = []
    for (let i = 0; i < length; i++) {
        colors.push(0)
    }

    // this loop, combined with the first if statement inside,
    // ensures that nodes that are not connected to node 0 
    // are also considered.
    for (let i = 0; i < length; i++) {
        // skip already "colored" nodes
        if (colors[i] == 0) {
            let queue = []
            let queueIndex = 0
            queue.push(i)

            colors[i] = 1

            // bfs 
            while (queueIndex < queue.length) {
                let node = queue[queueIndex]
                queueIndex++
                for (let edge of graph[node]) {
                    if (colors[edge] == 0) {
                        colors[edge] = -colors[node]
                        queue.push(edge)
                    } else if (colors[edge] != -colors[node]) {
                        return false
                    }
                }
            }
        }
    }
    return true
};

/*
Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
*/


/*
My attempt: brute force greedy algorithm
Failed due to the inability to determine whether a node should be in set A or B
idea:
for each node, add the nodes it's connected to to the opposite set.
if a connected node is in the same set as a node, the graph is not bipartite

if a node has not been included to either sets, add it to set A.

*/

/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartiteAttempt = function (graph) {
    let setA = []
    let setB = []

    for (let i = 0; i < graph.length; i++) {
        let inSetA = setA.includes(i)
        let inSetB = setB.includes(i)
        if (!inSetA && !inSetB) {
            setA.push(i) // problem: it is unknown whether the node should be in set A
            inSetA = true
        }
        for (let edge of graph[i]) {
            if (inSetA) {
                if (setA.includes(edge)) {
                    return false
                } else if (!setB.includes(edge)) {
                    setB.push(edge)
                }
            } else {
                if (setB.includes(edge)) {
                    return false
                } else if (!setA.includes(edge)) {
                    setA.push(edge)
                }
            }
        }
    }
    return true
};