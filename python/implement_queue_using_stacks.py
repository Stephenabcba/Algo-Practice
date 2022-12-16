# leetcode problem # 232. Implement Queue using Stacks

"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.


Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""

"""
My solution: Implementing queue using lists as stacks

As lists have methods such as append, pop, etc., they can be used as stacks

Logic:
1. Queue initialization:
- create 2 lists, 1 list to hold the actual data while the other
    serves as temporary storage when pushing
2. Push (Enqueue):
- if the main list is empty, directly append the pushed value to the main list
- if the main list is not empty:
    i. pop every value from the main list and append them to the other list
    ii. append the pushed value into the main list
    iii. pop every value from the other list and append them back to the main list
-> At the end, the first popped value of the main list is the item to be dequeued
3. Pop (Dequeue):
- As the list is prepped in the pushing phase, just return the popped value from the main list
4. Peek:
- As the list is prepped in the pushing phase, just return the last value in the main list
5. Empty:
- Check the length of the main list, return True if length is 0, False otherwise

Runtime: O(N^2) where N is the number of operations done
- Initialization: O(1)
- Push: O(M) where M is the number of values currently in the queue
    -> if all operations were push operations, M == N and total runtime becomes O(N^2)
- Pop: O(1)
- Peek: O(1)
- Empty: O(1)
Space: O(N) where N is the number of operations done
"""


class MyQueue:

    def __init__(self):
        self.stack = []
        self.workingStack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
        else:
            while len(self.stack) > 0:
                self.workingStack.append(self.stack.pop())
            self.stack.append(x)
            while len(self.workingStack) > 0:
                self.stack.append(self.workingStack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
