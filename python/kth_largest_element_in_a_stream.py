# leetcode problem # 703. Kth Largest Element in a Stream

"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
1 <= k <= 10^4
0 <= nums.length <= 10^4
-104 <= nums[i] <= 10^4
-104 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

"""
My solution: Heap

Using a heap, the runtime of each add() call can be done in log(K) time.

Logic:
- init(): 
    1. convert nums to a heap
    2. if the size of the heap is larger than k, remove values from the heap until the length is k
- add():
    1. if the size of the heap is smaller than k, insert the value into the heap
    2. otherwise, if the inserted value is larger than the smallest value in the heap,
        pop from the heap and insert the new value
    3. otherwise, don't insert the new value
    4. in all cases, return the smallest value in the heap.
Runtime:
- init(): O(M log M) where M is the length of the initial nums list
- add(): O(logK) where K is the initial input integer k
    - add() can be called N times
Space: O(max(M, K))
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
