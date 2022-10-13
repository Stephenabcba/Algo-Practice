# leetcode problem # 237. Delete Node in a Linked List

"""
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.


Example 1:
https://assets.leetcode.com/uploads/2020/09/01/node1.jpg
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
https://assets.leetcode.com/uploads/2020/09/01/node2.jpg
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique.
The node to be deleted is in the list and is not a tail node.
"""

"""
My solution: Delete the next node instead of the current node

As the program does not have access to the node before the given node to be deleted, it is impossible to change the pointer to the given node.
However, as the problem guarantees that the given node is not the last node, the program can copy information from the next node, 
    and then delete the next node.
    - This way, the information of the current node is removed, and a node is removed from the linked list
    - the order of the nodes before and after the given node are maintained.

Pseudocode:
1. Check that the current node is not the last node
- The logic does not work if the current node is the last node.
2. Copy the value of the next node to the current node
3. (Optional) Delete the next pointer of the next node after saving the location of the next pointer
    - this removes the link from the next pointer into the rest of the linked list
4. Change the next pointer of the given node to the next pointer of the next node
    - this effectively removes the next node from the linked list.

Runtime: O(1), length of the linked list does not affect runtime
Space: O(1), memory usage does not depend on input size.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is None:
            return False

        node.val = node.next.val
        temp = node.next.next
        node.next.next = None
        node.next = temp
