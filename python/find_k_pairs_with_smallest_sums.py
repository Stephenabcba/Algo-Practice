# leetcode problem # 373. Find K Pairs with Smallest Sums

"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Constraints:
1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 10^4
"""

"""
My solution: Heap

The brute force solution is to find every single pair and sort them based on their sums.
    - the runtime becomes O(M * N * log(M * N)), which is too large given the problem boundaries
    - the memory usage is O(M * N), which is also very large

By making use of the fact that both lists are sorted, only N items need to be compared at any given time
- nums1[x] + nums2[y] is always smaller than nums1[x] + nums2[y + 1] or nums1[x + 1] + nums2[y]
-> Start by comparing the pairs of all values of nums1 paired with nums2[0]
    - replace with [nums1[x], nums2[y+1]] when the pair is taken as the smallest pair

Using a heap, the smallest pair can be found in O(logN) time every iteration
- add a sum to the values saved in the heap to facilitate with the heap's sorting process

Runtime: O(N + K logN) where K is the number of pairs to find and N is the length of nums1
Space: O(N)
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []

        heap = []

        for num1Idx in range(len(nums1)):
            heapq.heappush(heap, [nums1[num1Idx] + nums2[0], num1Idx, 0])


        for idx in range(k):
            if len(heap) == 0:
                break
            curSum, num1Idx, num2Idx = heap[0]
            if num2Idx < len(nums2) - 1:
                heapq.heapreplace(heap, [nums1[num1Idx] + nums2[num2Idx + 1], num1Idx, num2Idx + 1])
            else:
                heapq.heappop(heap)
            ans.append([nums1[num1Idx], nums2[num2Idx]])
        
        return ans

"""
Solution by leetcode: incorporate a set with the heap

By including the set, the heap can begin with a single value and grow up to N values

Runtime: O(min(k⋅logk,m⋅n⋅log(m⋅n)))O(\min(k \cdot \log k, m \cdot n \cdot \log (m \cdot n)))O(min(k⋅logk,m⋅n⋅log(m⋅n)))
Space: O(min(k,m⋅n))
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        m = len(nums1)
        n = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        while k > 0 and minHeap:
            val, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < n and (i, j + 1) not in visited:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1
        
        return ans