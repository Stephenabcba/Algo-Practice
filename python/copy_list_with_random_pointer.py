# leetcode problem # 138. Copy List with Random Pointer

"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
https://assets.leetcode.com/uploads/2019/12/18/e1.png
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
https://assets.leetcode.com/uploads/2019/12/18/e2.png
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
https://assets.leetcode.com/uploads/2019/12/18/e3.png
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""

"""
My solution: Connect the regular list first, then connect the random nodes

Logic:
1. create a copy of the list
    - create a new node for every node in the original list
    - connect the nodes together
2. find and connect the random nodes
    - go through the list and find where the random node is
    - connect the random pointer in the new list accordingly

Runtime: O(N^2) where N is length of the list
Space: O(1), memory usage does not depend on input
    - output memory usage excluded
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyHead = Node(0)
        newCur = dummyHead

        cur = head

        while cur is not None:
            newCur.next = Node(cur.val)
            cur = cur.next
            newCur = newCur.next

        cur = head
        newCur = dummyHead.next


        while cur is not None:
            if cur.random is not None:
                runner = head
                newRunner = dummyHead.next
                while runner is not cur.random:
                    runner = runner.next
                    newRunner = newRunner.next
                newCur.random = newRunner

            cur = cur.next
            newCur = newCur.next

        return dummyHead.next


"""
Solution on leetcode sample 14ms submission
-> create the copied list then reconnect

Logic:
1. create the copy within the original list
    - at the end, the list would look like:
        node1 -> node1copy -> node2 -> node2copy...
2. connect the random nodes for the copied properly
    - from the format above, the correct new random node is the next node
    after the original random node
3. separate and reconnect the original and copied list
    - both lists contain every other node, offset by 1 node
4. return the copied list

Runtime: O(N)
Space: O(1)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        root = Node(0, head, None)
        
        size = 0
        while head:
            head.next = Node(head.val, head.next, head.random)
            head = head.next.next
            size += 1
            
        curr = root
        for _ in range(size):
            curr = curr.next.next
            if curr.random:
                curr.random = curr.random.next
            
        copy_root = Node(0, root.next.next, None)
        orig, copy = root.next, root.next.next
        for _ in range(size):
            orig.next = copy.next
            orig = orig.next
            copy.next = orig.next if orig else None
            copy = copy.next
            
        return copy_root.next