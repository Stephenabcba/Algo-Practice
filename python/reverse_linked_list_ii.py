# leetcode problem # 92. Reverse Linked List II

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

"""
My solution: reverse one by one

To handle the edge case where the reversal starts from the head of the list:
- Add a dummy node with no value as head
-> allows the rest of the logic to work with the edge case with no other additional steps

Logic:
1. Traverse to the node before the start of the reversal
- keep track of the index to correctly identify where the logic should stop
2. Bring each node within the index to be changed to the front of the reversed chain
- reconnect nodes accordingly
3. Once the nodes are reversed, return the resulting list
- the rest of the list do not need to be processed


This solution completes the logic in 1 pass, which satisfies the follow-up.

Runtime: O(N) where N is the length of the linked list
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        curIdx = 0
        curNode = dummyHead

        while curIdx < left - 1:
            curIdx += 1
            curNode = curNode.next

        connectLeft = curNode

        curNode = curNode.next
        curIdx += 1

        while curIdx < right:
            newReverseHead = curNode.next
            connectRight = curNode.next.next
            curNode.next.next = connectLeft.next
            curNode.next = connectRight
            connectLeft.next = newReverseHead
            curIdx += 1
        
        return dummyHead.next