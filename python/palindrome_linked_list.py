# leetcode problem # 234. Palindrome Linked List

"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.


Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false


Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

"""
My solution: Recursion

Using the properties of recursion, the program can trace back to the previous node using
the call stack.
- If the recursive function traverses to the next node each recursion, returning to the previous
    call returns to the previous node of the current node

Logic:
1. Recurse to the end of the SLL, traversing one node one at a time
2. The recursive function has two possible return values
    i. the next node to compare to the node in the current stack
    ii. False (boolean), the SLL is not a palindrome
3. After recursion, if the returned value is not False, the SLL is a palindrome

Runtime: O(N) where N is the length of SLL
Space: O(N)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def recurse(back):
            front = head
            if back.next:
                front = recurse(back.next)

            if front and front.val == back.val:
                return front.next
            return False

        return recurse(head) is not False


"""
Solution by cs_iitian on leetcode: 2 Pointers and list reversal

Logic:
1. Using 2 pointers, the program can find the midpoint within the SLL
2. Reverse the second half of the SLL
3. Compare the first half of the SLL to the second half, one by one
    - if any nodes do not match, the SLL is not a palindrome

Runtime: O(N)
Space: O(1)
"""


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True
