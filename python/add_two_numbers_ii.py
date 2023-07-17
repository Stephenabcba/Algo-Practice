# leetcode problem # 445. Add Two Numbers II

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
https://assets.leetcode.com/uploads/2021/04/09/sumii-linked-list.jpg
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
"""

"""
My solution: recursion

Using recursion, the carrying values can be passed to the previous place
    - ex: 9 + 9 = 18, the 10 needs to be added to the previous place as +1

Intuition: Add the shorter integer to the longer integer
- when the sum at the current place is greater or equal to 10, carry the 1 over to the previous place
- for places where the shorter integer is 0, move on to the next place and check if there's carrying values later

Edge case: the longer integer starts with a 9 and the carrying value is 1 at that place:
-> create a new node for the newly added place

Runtime: O(N) where N is the length of the linked lists
Space: O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Len = 0
        l2Len = 0

        curNode = l1
        while curNode is not None:
            l1Len += 1
            curNode = curNode.next

        curNode = l2
        while curNode is not None:
            l2Len += 1
            curNode = curNode.next

        longer = l1
        shorter = l2
        offset = l1Len - l2Len

        if l2Len > l1Len:
            longer = l2
            shorter = l1
            offset = l2Len - l1Len

        def recurse(longer, shorter, offset, hasPrev):
            if not longer or not shorter:
                return 0

            carryVal = 0
            if offset > 0:
                carryVal = recurse(longer.next, shorter, offset - 1, True)
            else:
                carryVal = recurse(longer.next, shorter.next, 0, True)
            if offset == 0:
                longer.val += carryVal + shorter.val
            else:
                longer.val += carryVal
                
            carryVal = 0
            if longer.val >= 10:
                carryVal = 1
                longer.val -= 10
                if hasPrev:
                    return carryVal
                else:
                    newNode = ListNode(longer.val, longer.next)
                    longer.val = 1
                    longer.next = newNode
            return carryVal

        recurse(longer, shorter, offset, False)
        return longer