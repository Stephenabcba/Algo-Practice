# Data Structures and Algos
- Keeps track of most algos I've done
  - Algos under `morning-algo` are done in morning algorithm sessions during Coding Dojo
  - Other algos are mostly taken from LeetCode and CodeWars
## Notes
- Information that could be useful to solve future algorithms
- For loops:
  - Usually used for iterating through a collection (arrays, etc)
  - It is sometimes useful to iterate through an array backwards
- Singly Linked List (SLL)
  - Chain of nodes containing a `val` and `next` each
    ``` js
    class Node {
        constructor(val) {
            this.val = val; // value stored on the node
            this.next = null; // pointer to the next node
        }
    }
    ```
  - The `head` of the node is the entry point into the SLL
    - regular SLLs do not hold any other information besides pointer variable to head
  - Most common way to traverse through the SLL is with a `runner` pointer variable
    - runner starts at `head`, and moves right using `runner.next`
    - the list ends when runner is `null`
      - the last item in the list will have `runner.next == null`
  - Once runner has moved pass a node, we cannot access the node without restarting from the head
  - To remove a node, we change the `.next` of the node before the target node
    - hence, we cannot remove a node the runner is on
      - runner has no access to its previous node
  - To remove a node at head, point head to the second node
    - `head = head.next`
    - this could become an edge case for many algos
  - One way to handle the edge case of processing head node:
    - create a `dummy` node with `dummy.next = head`
      - the dummy node has no `.val` property
      - now, the dummy node temporarily becomes the head of the SLL
        - the real `head` node can be treated like any other node in the SLL
        - by starting `runner` at `dummy`, we do not need to write separate logic to handle `head`
      - at any given point, `dummy.next` should be the real `head` node
  - Some algorithms may require many pointer variables to solve
  - Checking if a SLL is a loop:
    - create a walker that moves 1 node per iteration
    - create a runner that moves 2 nodes per iteration
    - if runner ends up at the same node as walker, the SLL has a loop
      - without a loop, runner should never "catch up" to walker
- Doubly Linked List (DLL)
  - Similar to SLL, but each node also has `.prev` property
    - `.prev` provides access to the previous node, and `.next` provides access to the next node
    ```js
    class Node {
        constructor(val) {
            this.val = val
            this.prev = null
            this.next = null
        }
    }
    ```
  - DLLs typically keeps track of the `head` and `tail` of the list as access points
    - these pointer variables refer to the start and end of the DLL, respectively
    - both `head` and `tail` are edge cases to handle
  - `runner` can be implemented similar to SLL
    - `runner` is now able to move left and right
  - To add or remove a node
    - change `.next` of the previous node
    - change `.prev` of the next node
- Binary Tree
  - "Tree" of nodes, each holding `.val`, `.left`, and `.right` properties
    - `.left` and `.right` are two "children" nodes of the current node
    ```js
    class Node {
        this.val = val
        this.left = null
        this.right = null
    }
    ```
  - The entry point to a tree is its `root` node
  - A node is a `leaf` if both of its children point to null
    - otherwise, it is a `stem`
  - The `height` of a binary tree is the number of nodes (inclusive) from the `root` to the furthest `leaf` node
  - A pointer (current) node can be used to traverse through the tree
- Binary Search Tree (BST)
  - Special variation of binary tree
    - all properties of binary tree apply to BST
  - Major variance from binary tree is the placement of nodes based on value
    - ALL descendent nodes to the left of any given node have values less than or equal to the current node
    - ALL descendent nodes to the right of any given node have values greater than the current node
    - to search through the tree, compare the desired value to the value at current node and move accordingly
  - Most BST operations can be done recursively
    - logic is often repeated on the children nodes
    - if desired, the logic can be translated into while loops
  - The minimum value within a BST is the left-most node in the BST
    - repeated shifting `current=current.left` until `current.left` is null
  - The maximum value within a BST is the right-most node in the BST
    - repeated shifting `current=current.right` until `current.right` is null
  - If a BST is mostly balanced, many operations have time complexity on O(logN)
  - The order in which nodes are inserted into the tree matters
    - if nodes are inserted least to greatest or greatest to least, the tree becomes similar to SLL
      - performance on accessing and manipulating suffers as all operations become linear in time complexity
- Binary Search
  - has a time complexity of O(log(N)), where N is the search range
  - typically used for a `sorted array`
  - however, its principles can also be extended for other types of algorithm
    - ex:
      - sorted matrixes -> treat the entire matrix as if it's one continuous sorted array
      - searching for a minimum that meets a requirement
        - typically requires some sort of processing each iteration, and thus more expensive than O(log(N))
        - finding the duplicated number in n+1 length array with [1,n] value range
          - binary search for the SMALLEST value N where `count(x<N) > N` where x is each value in the nums array
        - finding the minimum largest sum for splitting an array into m continuous subarrays
          - binary search in the range of `[max(nums),sum(nums)]` for the smallest value that allows the nums array to be split into m subarrays
- Heap
  - Also known as priority queue
  - a data structure highly efficient in finding the max or min of its contents (one of the two)
    - min heap: finding the min value takes O(1) time
    - max heap: finding the max value takes O(1) time
  - a heap has a tree structure
    - the parent is always smaller (or larger in a max heap) than its children
      - unlike a BST, a heap does not promise any other order besides the root being the smallest (or largest)
    - typically, a heap is a binary tree
  - heaps are often implemented as an array
    - converting a regular array to a heap takes O(N) time
    - the heap takes O(N) space
    - the "root" of the heap is at index 0
      - the smallest value (or largest)
    - the children of any given node at index k (if the node's children exist) are at index 2k+1 and 2k+2
  - Adding an element to a heap takes O(logN) time
    - the value is added at the end of the array
    - the added value will "swim" to its correct position
      - follows the heap rule of parent smaller than children
  - Removing an element from a heap takes O(logN) time
    - the returned value is always the smallest in the heap (the root)
    - replace the root with the last item in the array
    - the root will then "sink" to its correct position
      - heap rule applies
  - Replacing an element takes O(logN) time
    - the returned value is always the smallest
    - replace the root with the new value
      - the new value will "sink" as needed
  - In python:
    - the heap is stored in a list, and converted using heapify
    - common methods:
      - heapq.heapify(list) - convert list to heap
      - heapq.heappush(list,item) - add item
      - heapq.heappop(list) - remove item
      - heapq.heappushpop(list,item)
        - push first and then pop, more efficient than separate method calls
      - heapq.heapreplace(list,item)
        - pop first and then push
  - In Java:
    - the heap has its own class called PriorityQueue
    - common methods:
      - PriorityQueue<Integer> heap = new PriorityQueue<>();
      - heap.offer(item) - add item
      - heap.poll() - remove item
      - heap.size() - size of the heap
      - heap.peek() - get head without removing it from the heap
      - heap.contains(Object o) - check whether the heap contains the item
  - Javascript Min Heap implementation
    - if a max heap is needed, it is possible to insert the negative of the values into the min heap
      - by using the negatives, the min heap will act like a max heap.
    ``` js
        // min heap implementation by Ankita Masand on medium / bits and pieces
        // https://blog.bitsrc.io/implementing-heaps-in-javascript-c3fbf1cb2e65
        // Slightly modified because the remove function would not finish sinking a value if the node did not have 2 children.
        class MinHeap {

            constructor() {
                /* Initialing the array heap and adding a dummy element at index 0 */
                this.heap = [null]
            }

            getMin() {
                /* Accessing the min element at index 1 in the heap array */
                return this.heap[1]
            }

            insert(node) {

                /* Inserting the new node at the end of the heap array */
                this.heap.push(node)

                /* Finding the correct position for the new node */

                if (this.heap.length > 1) {
                    let current = this.heap.length - 1

                    /* Traversing up the parent node until the current node (current) is greater than the parent (current/2)*/
                    while (current > 1 && this.heap[Math.floor(current / 2)] > this.heap[current]) {

                        /* Swapping the two nodes by using the ES6 destructuring syntax*/
                        [this.heap[Math.floor(current / 2)], this.heap[current]] = [this.heap[current], this.heap[Math.floor(current / 2)]]
                        current = Math.floor(current / 2)
                    }
                }
            }

            remove() {
                /* Smallest element is at the index 1 in the heap array */
                let smallest = this.heap[1]

                /* When there are more than two elements in the array, we put the right most element at the first position
                    and start comparing nodes with the child nodes
                */
                if (this.heap.length > 2) {
                    this.heap[1] = this.heap[this.heap.length - 1]
                    this.heap.splice(this.heap.length - 1)

                    if (this.heap.length === 3) {
                        if (this.heap[1] > this.heap[2]) {
                            [this.heap[1], this.heap[2]] = [this.heap[2], this.heap[1]]
                        }
                        return smallest
                    }

                    let current = 1
                    let leftChildIndex = current * 2
                    let rightChildIndex = current * 2 + 1

                    while (this.heap[leftChildIndex] && this.heap[current] > this.heap[leftChildIndex]
                      || this.heap[rightChildIndex] && this.heap[current] > this.heap[rightChildIndex]) {
                        if (this.heap[leftChildIndex] && this.heap[rightChildIndex] && this.heap[leftChildIndex] < this.heap[rightChildIndex] || !this.heap[rightChildIndex]) {
                            [this.heap[current], this.heap[leftChildIndex]] = [this.heap[leftChildIndex], this.heap[current]]
                            current = leftChildIndex
                        } else {
                            [this.heap[current], this.heap[rightChildIndex]] = [this.heap[rightChildIndex], this.heap[current]]
                            current = rightChildIndex
                        }

                        leftChildIndex = current * 2
                        rightChildIndex = current * 2 + 1
                    }
                }

                /* If there are only two elements in the array, we directly splice out the first element */

                else if (this.heap.length === 2) {
                    this.heap.splice(1, 1)
                } else {
                    return null
                }

                return smallest
            }
        }
    ```
- Recursion: any function that calls on itself
  - backtracking
    - explore the problem space by processing partial solutions
    - accept a solution if it is valid (meets requirements)
    - eliminate the solution if it is invalid (does not meet requirements)
  - memoization
    - if the algorithm requires the result of previous recursions, or repeated calculation of the same values
    - keep the previous results in memory to quickly re-access again later
      - typically done with an array

- Graphs
  - Breadth-First Search (BFS)
    - Iterative solution (no recursion required)
    - BFS explores a graph from a starting node
    - Idea: search through nodes in the order that they are discovered
      - keep a queue of nodes
      - for each node in the queue, process all nodes that have an edge connected to the given node
        - look for unprocessed nodes and add them to the queue
    - Is able to find the shortest path in a UNWEIGHTED, UNDIRECTED graph
      - if the graph meets these 2 requirements, the path from the previous node is the shortest path to the starting node
      - The visited graph can hold the distance from the start or the previous node's location if needed.
    - Required data storage:
      - visited graph - same size as the actual graph
        - if the graph is an n x n grid, the visited graph is also an n x n grid.
        - could be holding values of boolean or distance from start
      - queue - keep track of queues to manage
        - could use array indexing for ease of managing the queue
          - helps avoid O(N) dequeue runtime
    - The target node is found is the current node in the iteration is the target node
      - if the iteration ends (there's no more nodes in the queue), there's no path from start node to target node

- Dynamic Programming (with information from Geeks for Geeks)
  - Can be considered if the following 2 conditions are met
    1. Overlapping subproblems
      - Sub problems depends on the solutions to other subproblems
      - all DP problems must satisfy this condition
    2. Optimal substructure
       - subpaths are also optimal solutions
       - a -> c can be broken up into a -> b + b -> c
         - not all problems satisfy this condition
       - Most DP problems satisfy this condition
  - "Typically, all the problems that require maximizing or minimize certain quantities or counting problems that say to count the arrangements under certain conditions or certain probability problems can be solved by using Dynamic Programming."
  - Solutions involve tabulating or memoizing the solution
    - Tabulating: no recursion, build the solution bottom-up
    - Memoizing: supporting memory structure to recursion, builds solution top down
      - don't need to recurse if the answer is already memoized
  - When building a DP structure, consider what actually needs to be saved
    - ex: in a matrix problem, maybe only the previous row's dp information is important
      - saving an array instead of the entire matrix reduces space usage from O(M*N) to O(N)