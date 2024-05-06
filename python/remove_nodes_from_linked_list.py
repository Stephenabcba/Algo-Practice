# leetcode problem # 2487. Remove Nodes From Linked List

"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

Example 1:
https://assets.leetcode.com/uploads/2022/10/02/drawio.png
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.

Constraints:
The number of the nodes in the given list is in the range [1, 10^5].
1 <= Node.val <= 10^5
"""

"""
My solution: Reverse the SLL twice

Idea: Going from back to front is deterministic
- going from front to back requires backtracking nodes and it is unclear whether the current node should be kept
    - going in both directions at the same time is difficult for a SLL
- when going from back to front, the very last node (the tail of the SLL) is always kept
    - any node larger than or equal to the current node is kept, and other nodes are removed

Logic:
1. Reverse the SLL
2. Iterate through the SLL to pick the nodes to keep
3. Reverse the SLL again (to the correct order)
4. Return the head of the SLL

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head
            reversedHead = head
            while cur:
                nextNode, cur.next, prev = cur.next, prev, cur
                reversedHead = cur
                cur = nextNode

            return reversedHead

        reversedHead = reverse(head)
        cur = reversedHead

        while cur.next:
            if cur.val > cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return reverse(reversedHead)
