# leetcode problem # 86. Partition List

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
https://assets.leetcode.com/uploads/2021/01/04/partition.jpg
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

"""
My solution: Partition then reconnect

Intuition:
- Create two SLLs, the first containing all nodes with node.val < x, and the second
    containing all nodes with node.val >= x
- Separate all nodes in input SLL into the two SLLs, then connect the SLLs

Runtime: O(N) where N is the number of nodes in the SLL
Space: O(1) memory usage does not depend on input
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        frontHead = ListNode()
        backHead = ListNode()
        frontCur = frontHead
        backCur = backHead

        curNode = head

        while curNode != None:
            nextNode = curNode.next
            if curNode.val < x:
                frontCur.next = curNode
                frontCur = frontCur.next
            else:
                backCur.next = curNode
                backCur = backCur.next
                
            curNode.next = None
            curNode = nextNode
        
        frontCur.next = backHead.next
        
        return frontHead.next