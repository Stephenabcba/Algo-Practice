# leetcode problem # 2816. Double a Number Represented as a Linked List

"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.


Example 1:
https://assets.leetcode.com/uploads/2023/05/28/example.png
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:
https://assets.leetcode.com/uploads/2023/05/28/example2.png
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 

Constraints:
The number of nodes in the list is in the range [1, 10^4]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""

"""
My solution: Process in the reversed direction

- As the value of a node affects the nodes to the left of it, it is easier to process from
right to left than from left to right
- To do so, reverse the SLL first
- Double the values at each node
    - if the value exceeds 10, carry the 1 over to the next node
        - the value at the current node is subtracted by 10
    - to carry the 1 for the last node, create a new node at the tail with a value of 1
- After processing, reverse the SLL again to get the correct answer

Runtime: O(N) where N is the number of nodes
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            cur = head
            prev = None
            reversedHead = cur

            while cur:
                temp, cur.next, prev = cur.next, prev, cur
                reversedHead = cur
                cur = temp

            return reversedHead

        reversedHead = reverse(head)
        carry = 0
        cur = reversedHead
        lastNode = cur

        while cur:
            doubledVal = 2 * cur.val + carry
            if doubledVal >= 10:
                carry = 1
                doubledVal -= 10
            else:
                carry = 0
            cur.val = doubledVal
            lastNode = cur
            cur = cur.next

        if carry == 1:
            lastNode.next = ListNode(1)

        return reverse(reversedHead)
