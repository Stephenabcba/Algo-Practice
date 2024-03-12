# leetcode problem # 1171. Remove Zero Sum Consecutive Nodes from Linked List

"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.
"""


"""
My solution: Make use of running sums

Idea: When looking at the running sums, nodes that create a zero sum sequence can be identified with two
running sums that have the same value
-> remove the values between the two running sums
* If the running sum is 0, the sum of all values up to the current point is 0, and can all be removed.

Misc. Implementation Details
1. By using a dummy head, the special case of the head being removed can be easily handled.
2. Using a dictionary, the program can quickly identify and move to nodes at a specific running sum
3. When deleting nodes, the dictionary entries related to the nodes must also be deleted

Runtime: O(N) where N is the number of nodes in the linked list
Space: O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums = {}

        dummy = ListNode()
        dummy.next = head

        curSum = 0
        cur = head
        while cur:
            curSum += cur.val

            if curSum == 0:
                dummy.next = cur.next
                sums = {}
            elif curSum in sums:
                temp = sums[curSum].next
                tempSum = curSum
                while temp != cur:
                    tempSum += temp.val
                    del sums[tempSum]
                    temp = temp.next
                sums[curSum].next = cur.next
            else:
                sums[curSum] = cur

            cur = cur.next

        return dummy.next
