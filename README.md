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