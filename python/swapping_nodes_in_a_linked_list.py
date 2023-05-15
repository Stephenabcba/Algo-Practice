# leetcode problem # 1721. Swapping Nodes in a Linked List

"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
https://assets.leetcode.com/uploads/2020/09/21/linked1.jpg
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
"""


"""
My solution: find length and swap

Find the length of the linked list, then find the positions of the two nodes
and swap their values.

Runtime: O(N) where N is length of linked list
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLen = 0
        cur = head
        while cur != None:
            cur = cur.next
            listLen += 1

        first = None
        second = None
        cur = head
        for idx in range(listLen):
            if idx + 1 == k:
                first = cur
            if idx == listLen - k:
                second = cur
            if first is not None and second is not None:
                break
            cur = cur.next

        temp = first.val
        first.val = second.val
        second.val = temp
        return head
