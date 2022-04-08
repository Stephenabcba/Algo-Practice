// leetcode problem #703. Kth Largest Element in a Stream
/*
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Constraints:

1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.

*/


/*
My Solution: Maintain a sorted array
Idea:
- Keep the nums array sorted from largest to smallest
    - sort the array every time a new element is addded
- the kth largest element is the element at k-1 index

Runtime: O(N^2)? Highly dependent on efficiency of the sort algorithm
    - this assumes that the sort() function can sort the array after single insertion in O(N) time

*/
/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function (k, nums) {
    this.k = k
    nums.sort((a, b) => b - a)
    this.nums = nums
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function (val) {
    this.nums.push(val)
    this.nums.sort((a, b) => b - a)
    return this.nums[this.k - 1]
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */

/*
Solution from Leetcode: Use a heap
- a heap can get a min/max (only one of the two) value in O(1) time (depending on if it is a min/max heap)
- insertion and deletion takes O(logN) time
Implementation:
- convert the array into a min heap (min value takes O(1) time to get)
    - remove elements until the heap has length of K
        - the min value is now the k-th largest value
- when adding a value to the stream:
    - add the value to the heap
    - maintain the length of the heap at K
    - return the min value of the heap
Runtime: O(N*log(N) + M*log(k))
- N is the size of num array
    - to maintain the size of the heap at length K, the remove operation might be used N times
        - remove operation is O(logN) runtime
- M is the number of times that a value is added
    - for each value added, the heap must add the value, and then remove an extra (if needed)
        - adding and removing are both O(logN) runtime
Space: O(N)
- the initialized heap has N elements
    - when the add method is run, the heap should have K elements
*/

/*
As JS does not have built-in methods for a heap, here are the methods for Python and Java:

Python:
** Python heaps are minheaps by default
    - to implement a max heap, make a values in the array negative
initializing heap: 
arrayVar = [a,b,c,d,e]
heapq.heapify(arrayVar) (the heap is stored in arrayVar)

removing an item from heap: (removes the smallest item)
heapq.heappop(arrayVar)

adding an item to heap: (stores based on heap logic)
heapq.heappush(arrayVal, item)

getting the min value of the heap:
arrayVal[0]


Java:
** Java heaps are minheaps by default
    - to implement a max heap, make a values in the array negative
initializing heap: 
int [] nums = [a,b,c,d,e];
PriorityQueue<Integer> heap = new PriorityQueue<>();
for (int num : nums) {
    heap.offer(num)
}

removing an item from heap: (removes the smallest item)
heap.poll();

adding an item to heap: (stores based on heap logic)
heap.offer(num);

getting the min value of the heap:
heap.peek();
*/