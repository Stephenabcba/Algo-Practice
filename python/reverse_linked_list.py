# leetcode problem # 206. Reverse Linked List

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

"""
My solutions: 

1. Iterative
- Steps:
    1. Create a pointer for the new head of the reversed list (newHead)
        - initially, the pointer points to nothing
    2. iteratively reconnect and reverse the list
        - save a pointer to the next node
        - redirect the current node's next node to the newHead
        - make the current node the newHead
        - set the next node as the node to process for the next iteration
    3. return newHead after the cycle is done

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1)

2. Recursive
Create a recursive function within the solution
- The recursive function takes in the current node, and the head of the previous nodes to connect to
- The previous nodes are the already in reversed order

- Base Case: There is no more nodes to process (current node is None)
    -> return the head of the previous nodes, the SLL is reversed
- Recursive Case: There are nodes to process
    - keep a pointer to the next node (nextNode)
    - connect the current node to the head of previous nodes
    - the current node becomes the head of the previous nodes (for the next recursion)
    - call and return the recursive function with nextNode and current node as inputs

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1), memory usage does not depend on input (the memory used for recursion is excluded)

These two solutins satisfies the followup, which asks for a recursive and an iterative solution
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.reverseListRecursive(head)
        newHead = None

        cur = head

        while cur:
            newCur = cur.next

            cur.next = newHead

            newHead = cur

            cur = newCur

        return newHead

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def connections(node, prevNode):
            if node:
                nextNode = node.next
                node.next = prevNode
                return connections(nextNode, node)
            else:
                return prevNode

        return connections(head, None)
