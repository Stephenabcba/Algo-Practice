// leetcode problem # 1192. Critical Connections in a Network

/*
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Constraints:

2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= a_i, b_i <= n - 1
a_i != b_i
There are no repeated connections.
*/

/*
My solution: runtime exceeded
From the hint in leetcode, a modified Tarjan's algorithm is applied.

The algorithm was based on the pseudocode found on wikipedia: https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

The solution involved removing each edge and running Tarjan's algorithm for set with removed edges, which led to O(N^2) run time.
*/

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
var criticalConnections = function (n, connections) {
    const tarjan = (n, connections) => {
        const strongConnect = (vertex, indexes, lowLink, index, stack, connections, onStack) => {
            indexes[vertex] = index
            lowLink[vertex] = index

            index += 1
            stack.push(vertex)
            onStack[vertex] = true


            for (let edge of connections) {
                let otherNode = -1
                if (edge[0] == vertex) {
                    otherNode = edge[1]
                } else if (edge[1] == vertex) {
                    otherNode = edge[0]
                } else {
                    continue
                }
                if (indexes[otherNode] < 0) {
                    strongConnect(otherNode, indexes, lowLink, index, stack, connections, onStack)
                } else if (onStack[otherNode]) {
                    if (lowLink[vertex] > indexes[otherNode]) {
                        lowLink[vertex] = indexes[otherNode]
                    }
                }
            }
            if (lowLink[vertex] == indexes[vertex]) {
                if (stack.length < indexes.length) {
                    return true
                }
            }
            return false
        }

        const indexes = []
        const lowLink = []
        const onStack = []
        for (let i = 0; i < n; i++) {
            indexes.push(-1)
            lowLink.push(-1)
            onStack.push(false)
        }

        let index = 0
        let stack = []

        return strongConnect(0, indexes, lowLink, index, stack, connections, onStack)
    }
    const ans = []
    for (let i = 0; i < connections.length; i++) {
        const isCritical = tarjan(n, connections.slice(0, i).concat(connections.slice(i + 1)))
        if (isCritical) {
            ans.push(connections[i])
        }
    }
    return ans
};

/*
Solution by D4tZ in Leetcode discussions (originally written in c++)
The algorithm is used to find bridges in the graph, known as critical edges in this problem.

It is a modification of DFS.
It is also an application of Tarjan's Algorithm

Basic Idea:
follow the dfs logic of accessing nodes
    - recursively visit all unvisited nodes that a node is connected to

Tarjan's algorithm logic:
keep track of when the first time a node is seen
    - with DFS, a node is always able to reach another node with higher index
keep track of the earliest node (same node indexing as the first time index) that a node can connect to (directly and indirectly)
    - ignore the node that branched to this node in DFS
this way, if a node's connected node has an earliest node larger than the current node's index, the current node is a bridge
    - essentially, the current node is the only node that connects to the connected node from the chain of nodes
    - add the edge to the answer array.

*/
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number[][]}
 */
var criticalConnections = function (n, connections) {
    const ans = []
    const graph = []

    const firstTime = []
    const minTime = []
    const visited = []

    let time = 1

    const dfs = (node, parent = -1) => {
        firstTime[node] = time
        minTime[node] = time
        time++
        visited[node] = true
        for (let child of graph[node]) {
            if (child == parent) {
                continue
            }

            if (!visited[child]) {
                dfs(child, node)
            }

            minTime[node] = Math.min(minTime[child], minTime[node])

            if (firstTime[node] < minTime[child]) {
                ans.push([node, child])
            }
        }
    }

    // initialize the arrays
    for (let i = 0; i < n; i++) {
        firstTime.push(-1)
        minTime.push(-1)
        visited.push(false)
        graph.push([])
    }

    // build a network of the vertexes each vertex is connected to from the list of edges
    for (let edge of connections) {
        let nodeA = edge[0]
        let nodeB = edge[1]
        graph[nodeA].push(nodeB)
        graph[nodeB].push(nodeA)
    }
    dfs(0)
    return ans
};

/*
Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
*/