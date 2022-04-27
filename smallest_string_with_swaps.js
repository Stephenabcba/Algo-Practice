// leetcode problem # 1202. Smallest String With Swaps

/*
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

Constraints:
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
*/


/*
Solution taken from leetcode solutions
My solution was greedy swaps, which didn't work because order mattered.

Treat the indexes of the string as nodes
Treat the pairs as two-way edges

Run DFS on the graph created from the conditions above



*/

/**
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function (s, pairs) {
    const DFS = (s, vertex, characters, indices, visited, adj) => {
        characters.push(s[vertex])
        indices.push(vertex)

        visited[vertex] = true

        for (let adjacent of adj[vertex]) {
            if (!visited[adjacent]) {
                DFS(s, adjacent, characters, indices, visited, adj)
            }
        }
    }
    const adj = []
    const visited = []
    for (let i = 0; i < s.length; i++) {
        adj.push([])
    }

    for (let edge of pairs) {
        let source = edge[0]
        let destination = edge[1]

        adj[source].push(destination)
        adj[destination].push(source)
    }

    const answer = []
    for (let i = 0; i < s.length; i++) {
        answer.push(s[i])
    }

    for (let vertex = 0; vertex < s.length; vertex++) {
        if (!visited[vertex]) {
            const characters = []
            const indices = []

            DFS(s, vertex, characters, indices, visited, adj)
            characters.sort()
            indices.sort((a, b) => a - b)

            for (let index = 0; index < characters.length; index++) {
                answer[indices[index]] = characters[index]
            }
        }
    }
    return answer.join("")

};


/*
Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
*/