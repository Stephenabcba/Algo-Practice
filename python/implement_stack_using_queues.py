# leetcode problem # 225. Implement Stack using Queues

"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
"""

"""
My solution: Handle the Timely operations at push()

Create 2 queues to handle operations
- main queue holds the data
- supporting queue will temporarily hold values during certain opertions
    - empty at the start and end of every operation

Logic:
- Push:
    1. Swap the main and supporting queues
    2. Add the new value to the main queue
    3. Add the values from supporting queue to main queue one by one

- Pop: dequeue the first value and return it
- Top: peek at the first value and return it (without removing)
- Empty: Return whether the length of main queue is 0

Runtime: O(N^2) where N is the number of operations
- MyStack(): initialization takes O(1) time
- push(): O(M), where M is the number of values currently in the stack
- pop(): O(1)
- top(): O(1)
- empty(): O(1)
-> In the worst case, N values are pushed, and M becomes N.
Space: O(N) where N is the number of operations
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.mainQueue = deque()
        self.suppQueue = deque()

    def push(self, x: int) -> None:
        self.mainQueue, self.suppQueue = self.suppQueue, self.mainQueue
        self.mainQueue.append(x)
        while len(self.suppQueue) > 0:
            self.mainQueue.append((self.suppQueue.popleft()))
        

    def pop(self) -> int:
        return self.mainQueue.popleft()

    def top(self) -> int:
        return self.mainQueue[0]

    def empty(self) -> bool:
        return len(self.mainQueue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()