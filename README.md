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
- Recursion: any function that calls on itself
  - backtracking
    - explore the problem space by processing partial solutions
    - accept a solution if it is valid (meets requirements)
    - eliminate the solution if it is invalid (does not meet requirements)
  - memoization
    - if the algorithm requires the result of previous recursions, or repeated calculation of the same values
    - keep the previous results in memory to quickly re-access again later
      - typically done with an array