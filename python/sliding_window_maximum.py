# leetcode problem # 239. Sliding Window Maximum

"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

"""
My solution: Heap with backlog

Logic:
- Use a heap to quickly find the maximum in the window
- If the removed value is the highest in the heap, remove it from the heap
    - otherwise, add the removed value to the backlog until it becomes the highest in the heap
- Add all new values into the heap

Values can be removed from the heap at most N times, and values are added to the heap
exactly N times.

Runtime: O(N * logN) where N is the length of nums
Space: O(N)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        removeDict = {}
        heap = []
        for idx in range(k):
            heap.append(-nums[idx])
        
        heapq.heapify(heap)

        ans.append(-heap[0])

        for idx in range(len(nums) - k):
            removeVal = nums[idx]
            addedVal = nums[idx + k]
            if removeVal == -heap[0]:
                heapq.heapreplace(heap,-addedVal)
            else:
                heapq.heappush(heap, -addedVal)
                removeDict[removeVal] = removeDict.get(removeVal, 0)
                removeDict[removeVal] += 1

            while removeDict.get(-heap[0], 0) > 0:
                removeDict[-heap[0]] -= 1
                heapq.heappop(heap)

            ans.append(-heap[0])

        return ans


"""
Solution: Monotonic Deque

All values smaller than X that comes before X can never be the maximum
- ex:  given a window [2,3,4,5,1]
    - 2, 3, 4 can never be the maximum in the window, since they are smaller than 5 and
    are removed first.
    - however, the last 1 may be the maximum after 5 is removed
- In general, when X is added to the window, all values smaller than X are removed
-> The remaining values are in decreasing order, and maintains their relative order from
nums
    - ex: given a window[2,3,5,1,4]
        - after removing values, the window becomes [5,4]
        - 5 > 4, and 5 comes before 4 in the window

As mentioned by leetcode:
"A monotonic data structure is one where the elements are always sorted. In our case, we want a monotonic decreasing queue, 
which means that the elements in the queue are always sorted descending. When we want to add a new element x, we maintain
the monotonic property by removing all elements less than x before adding x."

When iterating:
1. The first value in the reduced window is the maximum in the window
2. When the maximum is removed, the next value becomes the maximum
3. Remove all values smaller than the new value as mentioned above

Runtime: O(N) where N is length of nums list
Space: O(k), where k is integer k
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])

        return res