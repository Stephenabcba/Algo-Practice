# leetcode problem # 427. Construct Quad Tree

"""
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer to the wiki.

Quad-Tree format:

The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.

It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
Explanation: The explanation of this example is shown below:
Notice that 0 represnts False and 1 represents True in the photo representing the Quad-Tree.

Example 2:



Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4 sub-grids where each has the same value.
Explanation is shown in the photo below:

 

Constraints:

n == grid.length == grid[i].length
n == 2^x where 0 <= x <= 6
"""

"""
My Solution: Build Bottom Up

Initial Strategy:
1. Check if the entire grid has the same value, if yes, the answer is 1 quadTree with no subnodes
2.If the grid has different values, check the 4 sub-grids and recurse as needed
Problem: each value in the grid could be checked multiple times, leading to excessive runtime

Improved Strategy:
1. Break the grid down into 4 subgrids, and continue to break each subgrid until all subgrids have
a single value
2. A single value must be a leaf node; create a quadTree node for it
3. at the parent quadTree level, check if all children nodes are leaf nodes and have the same value
    - if both are true, the parent quadTree can be a single quadTree with no subnodes
    - otherwise, the parent quadTree must save the information of all 4 children nodes

Runtime: O(N^2) where N is the sidelength of the grid
Space: O(N^2)
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def buildNode(yStart, xStart, subgridLength):
            if subgridLength == 1:
                return Node(grid[yStart][xStart], 1)
            halfGridLength = subgridLength // 2
            topLeft = buildNode(yStart, xStart, halfGridLength)
            topRight = buildNode(
                yStart, xStart + halfGridLength, halfGridLength)
            bottomLeft = buildNode(
                yStart + halfGridLength, xStart, halfGridLength)
            bottomRight = buildNode(
                yStart + halfGridLength, xStart + halfGridLength, halfGridLength)

            isLeaf = 0
            gridVal = topLeft.val
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                    isLeaf = 1

            if isLeaf:
                return Node(gridVal, isLeaf)
            else:
                return Node(gridVal, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

        return buildNode(0, 0, len(grid))
