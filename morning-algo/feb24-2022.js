// DLLNodes have a .next and .prev
class DLLNode {
    constructor(data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}

// DLLists have both a .head and .tail pointer
class DLList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    // == Main Methods ==

    // add node before target
    // target is the value of a node in the list
    // consider the edge case where you may have to move the head
    // consider the edge case where you do not find the target
    prepend(target, node) {
        if (this.head == null && this.tail == null) {
            return false;
        } else {
            if (this.head.data == target) {
                this.head.prev = node;
                node.next = this.head;
                this.head = node;
                return true;
            }
            let runner = this.head;
            while (runner != null) {
                if (runner.data == target) {
                    runner.prev.next = node;
                    node.next = runner;
                    node.prev = runner.prev;
                    runner.prev = node;
                    return true;
                } runner = runner.next;
            }
            return false;
        }
    }


    // return true or false if a node exists with data === val
    exists(val) { }

    // push to head
    addHead(node) {
        if (!this.head) { // empty list
            this.head = node;
            this.tail = node;
        } else {
            this.head.prev = node;
            node.next = this.head;
            this.head = node;
        }
    }

    // pop from tail
    removeTail() {
        if (this.head == null) return; // empty list
        if (this.head === this.tail) { // one node
            var temp = this.tail; // set a temp
            this.head = null; // disconnect the head
            this.tail = null; // disconnect the tail
            return temp;
        }
        var temp = this.tail; // set a temp
        this.tail = tail.prev; // move the tail back
        this.tail.next = null; // null out the new tail's next
        temp.prev = null; // null out the temp's prev
        return temp;
    }

    // return is empty
    isEmpty() {
        return this.head === null;
    }

    // == Bonus Methods, just inverted versions of the first set ==

    // push to tail
    addTail(node) { }

    // pop from head
    removeHead() { }
}

// instantiate the DLL
// add a few nodes
// test!
let DLL1 = new DLList();
DLL1.addHead(new DLLNode(51));
DLL1.addHead(new DLLNode(52));
DLL1.addHead(new DLLNode(53));
DLL1.addHead(new DLLNode(55));
DLL1.prepend(55, new DLLNode(54));
console.log(DLL1);