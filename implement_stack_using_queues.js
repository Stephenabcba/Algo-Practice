// leetcode problem #225. Implement Stack using Queues

/*
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.


Follow-up: Can you implement the stack using only one queue?

*/

/*
My solution: 2 queues with processing at popping

When pushing to the stack, simply enqueue the value to the queue.
- runtime: O(1)
- space: O(N)

When popping from the stack:
    1. dequeue all values from the main queue
    2. enqueue all values except the last value to a second queue
    3. replace the first queue with the second queue
    4. return the last value in the original first queue
- runtime: O(N)
- space: O(N)

peek() : same as pop(),  except push the last value back to the queue
- runtime: O(N)
- space: O(N)

empty() : check the size of the queue
- runtime: O(1)
*/

var MyStack = function () {
    this.queue = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function (x) {
    this.queue.push(x)
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function () {
    let tempQ = []
    let poppedVal = null
    while (this.queue.length > 0) {
        if (poppedVal != null) {
            tempQ.push(poppedVal)
        }
        poppedVal = this.queue.shift()
    }
    this.queue = tempQ
    return poppedVal
};

/**
 * @return {number}
 */
MyStack.prototype.top = function () {
    let tempQ = []
    let peekVal = null
    while (this.queue.length > 0) {
        peekVal = this.queue.shift()
        tempQ.push(peekVal)
    }
    this.queue = tempQ
    return peekVal
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function () {
    return this.queue.length == 0
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */

/*
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

*/

/*
Additional solution concepts from leetcode solutions:
both ideas involve structuring the data inside the queue as a stack, but with different implementations

idea 1: 2 queues, processing at push()
- at the start of any operation, the queue is in the order of the stack, where the value dequeued is the value that would be popped from the stack
- to do so, the following is done at push()
    1. any value inserted is placed in a second queue
    2. dequeue all values from the main queue and enqueue them into the second queue
    3. swap the two queues
    - now, the values are in the order of a stack

ex: 
initial state: (pushing 4)
queue1 : [3,2,1]
queue2 : []

state 2:
queue1 : [3,2,1]
queue2 : [4] // place 4 at the "front"

state 3:
queue1 : [] // dequeue from queue 1
queue2 : [4,3,2,1] // enqueue to queue 2

state 4:
queue1 : [4,3,2,1] // swapped with queue2
queue2 : [] // swapped with queue1


idea 2: 1 queue, processing at push()
- at the start of any operation, the queue is in the order of the stack, where the value dequeued is the value that would be popped from the stack
- instead of using a second queue like idea 1, dequeue size - 1 times from the front and enqueue at the back

ex:
initial state: (pushing 4)
queue : [3,2,1]

state 2:
queue : [3,2,1,4] // 4 is enqueued at the back, the size is 4

state 3:
queue : [4,3,2,1] // dequeued size - 1 times (4 - 1 = 3) and enqueued the values at the back


for both approaches:
push() : runtime O(N) - use the approach above
pop() : runtime O(1) - dequeue from the front of the queue
peek() : runtime O(1) - check the first value of the queue
empty() : runtime O(1) - check size of the queue

*/