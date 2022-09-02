// leetcode problem # 1631. Path With Minimum Effort

/*
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^6
*/

/*
Solution from leetcode discussion by midnightsimon: BinarySearch on answer + BFS
Solution originally written in c++
- binary search is used to search the answer space for the minimum effort required in the path
    - find the lowest maximum effort that is valid -> minimum effort required to go from top left to bottom right
- breadth-first search is used to confirm whether a path is possible given a maximum effort
    - inside the BFS, in addition to the regular requirements, a node is only added to the queue if it is reachable under the given maximum effort
    - if the BFS can reach the bottom right, the maximum effort is valid
        - otherwise, the maximum effort is invalid
            - i.e. if the queue has finished before reaching the bottom right, due to the additional requirement of the queue.
*/

/**
 * @param {number[][]} heights
 * @return {number}
 */
var minimumEffortPath = function (heights) {
    const isValid = (heights, max) => {
        // initialize directions
        const dirs = [
            [-1, 0], [0, -1], [0, 1], [1, 0]
        ]

        // initialize the queue and the number of rows/columns in the matrix
        const queue = []
        let rows = heights.length
        let cols = heights[0].length

        // initialize the seen boolean matrix, with none of the nodes seen yet
        let seen = []
        for (let i = 0; i < rows; i++) {
            seen.push([])
            for (j = 0; j < cols; j++) {
                seen[i].push(false)
            }
        }

        // add the top left node as start of the path
        queue.push([0, 0])
        seen[0][0] = true

        while (queue.length > 0) {
            // get the first item of the queue
            let node = queue[0]
            queue.shift()

            // extract the position of the node
            let curRow = node[0]
            let curCol = node[1]

            // the bottom right node is reachable, return true.
            if (curRow == rows - 1 && curCol == cols - 1) {
                return true
            }

            // check the 4 directions that a current node can go
            for (let direction of dirs) { // up down left right
                let modRow = direction[0] + curRow
                let modCol = direction[1] + curCol

                // skip calculations if the node in that direction is already seen or out of bounds
                if (modRow < 0 || modRow >= rows) continue
                if (modCol < 0 || modCol >= cols) continue
                if (seen[modRow][modCol]) continue

                // if the new node takes too much effort, it cannot be reached from the current node.
                // do not add it to the queue.
                if (Math.abs(heights[curRow][curCol] - heights[modRow][modCol]) > max) continue

                // if the new node takes less than the effort limit, add it to the queue
                seen[modRow][modCol] = true
                queue.push([modRow, modCol])
            }
        }
        return false
    }

    let left = 0
    let right = 1000000
    let best = 1000000
    while (left <= right) {
        let middle = Math.floor((left + right) / 2)
        if (isValid(heights, middle)) {
            right = middle - 1
            if (middle < best) {
                best = middle
            }
        } else {
            left = middle + 1
        }
    }
    return best
};

/*
Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
*/

/*
Dijkstra's algorithm, also written by midnightsimon.
- uses a priority queue and a distance matrix.
- the distance matrix holds the minimum effort required to reach a given node from the start
    - this value is not necessarily the effort required to move from an adjacent node
    - the matrix is continuously updated, so the value in an intermediate state may not be the minimum value
- the priority queue holds the "weight" (effort) and the coordinate of a new node to relax the distance matrix
*/