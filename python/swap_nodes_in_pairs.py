# leetcode problem # 24. Swap Nodes in Pairs

"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

"""
My solution: make the swaps

Basic Logic: If there's at least two more nodes left to process,
swap the nodes and move 2 nodes down the list

Using an empty head: by using an empty (dummy) head, the entire list
could be processed with the same logic, without doing separate work
for the first 2 nodes (since it changes the head)

Runtime: O(N) where N is the the length of SLL
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        cur = dummy

        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = temp.next
            temp.next = cur.next.next
            cur.next.next = temp
            cur = cur.next.next

        return dummy.next
