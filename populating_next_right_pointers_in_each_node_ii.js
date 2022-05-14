// leetcode problem #117. Populating Next Right Pointers in Each Node II

/*
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
*/

/*
Attempt 1, incomplete
The recursive attempt tries to traverse laterally before moving onto the next level
However, the current conditions do not start at the correct node when moving onther the next level
*/
/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connectIncomplete = function (root) {
    const recurse = (root, level, last) => {
        if (root == null) {
            return
        }
        if (root.left) {
            if (last.level == level + 1) {
                last.node.next = root.left
            }
            last.node = root.left
            last.level = level + 1
        }
        if (root.right) {
            if (last.level == level + 1) {
                last.node.next = root.right
            }
            last.node = root.right
            last.level = level + 1
        }
        recurse(root.next, level, last)
        recurse(root.left, level + 1, last)

    }
    recurse(root, 0, { level: 0, node: root })
    return root
};

/*
My solution: loops
Basic idea:
1. traverse through each level of the tree laterally, connecting the children of each node to the next node
2. when the current level is fully traversed, move on to the first node of the next level
3. repeat steps 1 & 2 until there are no nodes remaining


- at any given time, the current level is already connected to its next node (if it exists)
    - thus, current node.next is always set to the correct value (either next node or null)
    - the algorithm connects the children node through the iterations
    - the root, which is the start of the loop, is correctly connected to nothing.

- the loop ends when there are no nodes in the child level of the current node
    - look for the first node of the child level when connecting (used for step 2)

- when connecting the children nodes:
    - if a node (A) exists and there is a previous node (B) in the level, connect them.
        - connect B's next pointer to A
    - the current node is now the previous node to connect to the next node
*/

var connect = function (root) {
    let curNode = root
    let nextLevel = null
    let last = null

    while (curNode != null) {
        if (nextLevel == null) { // attempt to set a next level start node if none exists yet
            if (curNode.left != null) {
                nextLevel = curNode.left
            } else if (curNode.right != null) {
                nextLevel = curNode.right
            }
        }

        // connect the child level
        if (curNode.left != null) {
            if (last != null) {
                last.next = curNode.left
            }
            last = curNode.left
        }

        if (curNode.right != null) {
            if (last != null) {
                last.next = curNode.right
            }
            last = curNode.right
        }

        // either move laterally or to the start of the next level
        if (curNode.next != null) {
            curNode = curNode.next
        } else {
            curNode = nextLevel
            nextLevel = null
            last = null
        }
    }
    return root
};

/*
Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []
*/

