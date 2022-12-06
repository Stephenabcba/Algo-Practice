# leetcode problem # 328. Odd Even Linked List

"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.


Example 1:
https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]


Constraints:
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6
"""

"""
My solution: "Leapfrog" 2 Pointer approach

- Keep track of the odd and even pointers, and where the head of the even nodes start
- The next node on an unprocessed odd node is the next node of the unprocessed even node after it
    - While traversing the SLL, the pointers leapfrog each other
- In this algorithm, if the list has odd number of nodes, the last node in the even list needs to have its next pointer reset to None.

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1) Memory usage does not scale with input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        evenHead = head.next
        currOdd = head
        currEven = evenHead

        while currEven != None:
            currOdd.next = currEven.next
            if currOdd.next == None:
                currEven.next = None
                break
            currOdd = currOdd.next
            currEven.next = currOdd.next
            currEven = currEven.next

        currOdd.next = evenHead

        return head
