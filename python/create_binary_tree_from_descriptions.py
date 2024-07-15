# leetcode problem # 2196. Create Binary Tree From Descriptions

"""
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

Example 1:
https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

Example 2:
https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

Constraints:
1 <= descriptions.length <= 10^4
descriptions[i].length == 3
1 <= parenti, childi <= 10^5
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
"""

"""
My Solution: Use dictionaries to manage the relationship

2 Dictionaries are used to manage the parent-child relationship and to find the parent
1. Parent-Children dictionary
- the key is a parent node, and the value is a list
    - the first item in the list is the value of the left child
    - the second item in the list is the value of the second child
    - if either child doesn't exist, set the value to -1
2. Find Parent dictionary
- Holds the reversed relation, where the key is a child, and the value is the parent
- Can be used to trace a node back to find the root

Logic:
1. Populatate both dictionaries by iterating through each description
2. Find the root using find parent dictionary
3. Build the Tree from the root using parent-children dictionary
4. Return the completed tree


Runtime: O(N) where N is the number of nodes in the tree
Space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treeDict = defaultdict(list)
        findParentDict = {}

        for parent, child, isLeft in descriptions:
            if isLeft:
                isLeft = 0
            else:
                isLeft = 1
            while len(treeDict[parent]) < 2:
                treeDict[parent].append(-1)

            treeDict[parent][isLeft] = child
            findParentDict[child] = parent

        rootVal = descriptions[0][0]

        while rootVal in findParentDict:
            rootVal = findParentDict[rootVal]

        def buildTree(parent):
            parentNode = TreeNode(parent)
            if parent in treeDict:
                leftVal, rightVal = treeDict[parent]
                if leftVal > 0:
                    parentNode.left = buildTree(leftVal)
                if rightVal > 0:
                    parentNode.right = buildTree(rightVal)
            return parentNode

        return buildTree(rootVal)


"""
Solution By leetcode: Constructing Tree From Directly Map and TreeNode Object

Instead of saving the parent-child relationship in lists, the created nodes are directly saved to the dictionary

To find the root, a set is created and filled with all nodes marked as children
-> the only node not marked as a child of another node is the root

Runtime: O(N)
Space: O(N)
"""


class Solution:
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        # Maps values to TreeNode pointers
        node_map = {}

        # Stores values which are children in the descriptions
        children = set()

        # Iterate through description to create nodes and set up tree structure
        for description in descriptions:
            # Extract parent value, child value, and whether
            # it is a left child (1) or right child (0)
            parent_value = description[0]
            child_value = description[1]
            is_left = bool(description[2])

            # Create parent and child nodes if not already created
            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                node_map[child_value] = TreeNode(child_value)

            # Attach child node to parent's left or right branch
            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]

            # Mark child as a child in the set
            children.add(child_value)

        # Find and return the root node
        for node in node_map.values():
            if node.val not in children:
                return node  # Root node found

        return None  # Should not occur according to problem statement
