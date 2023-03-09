# leetcode problem # 142. Linked List Cycle II

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.


Example 1:
https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""

"""
My Attempt: Runner + Walker

Using a Runner (travels 2 nodes every iteration) and a Walker (travels 1 node every iteration),
a cycle can be detected when the runner meets with the walker.

Problem, without further logic, the algorithm can only detect cycles without finding the start of the cycle.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        walker = head
        while walker != None:
            if runner.next and runner.next.next:
                runner = runner.next.next
            else:
                return None
            walker = walker.next
            if walker != None and runner == walker:
                return walker
        return None


"""
Solution by N7_BLACKHAT on leetcode: Floyd's Cycle-Finding algorithm:

Continuing from the walker/runner logic, after runner and walker meet:
1. reset walker to start of SLL
2. move walker and runner 1 node at a time until they meet
3. where the nodes meet is the start of the cycle

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1), memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        walker = head
        while walker != None:
            if runner.next and runner.next.next:
                runner = runner.next.next
            else:
                return None
            walker = walker.next
            if walker != None and runner == walker:
                walker = head
                while walker != runner:
                    walker = walker.next
                    runner = runner.next
                return walker
        return None
