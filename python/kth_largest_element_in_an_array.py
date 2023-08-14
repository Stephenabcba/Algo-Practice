# leetcode problem # 215. Kth Largest Element in an Array

"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""


"""
My solution: minheap

Idea: keep track of the top k values while going through nums, and return the kth
value at the end
- to maintain relative order, a heap can be used where the kth largest value can be accessed in O(1) time

Implementation:
- Keep a heap of max size k
- Iterate through each num in nums
    - if the heap has not reached the max size, add it to the heap
    - if the heap has reached the max size:
        - if the num is smaller than the smallest value in the heap, move on
        - otherwise, replace the smallest value in the heap with num
            - keep the heap in the correct order
- At the end, return the smallest value in the heap

Runtime: O(N * logK) where N is the length of nums and K is the input k
Space: O(K)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappushpop(heap, num)

        return heap[0]