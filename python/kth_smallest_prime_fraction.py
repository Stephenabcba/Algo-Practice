# leetcode problem # 786. K-th Smallest Prime Fraction

"""
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:
Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:
2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 10^4
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2

Follow up: Can you solve the problem with better than O(n^2) complexity?
"""

"""
My solution: heap

Use a heap to find the smallest fraction up the the kth lowest
- add the 2 fractions to the heap
    - same numerator, smaller denominator
    - larger numerator, same denominator
    * these two fraction are two new fractions that may be the next smallest fraction
    * do not add a fraction again if it has already been added

To check whether a certain fraction has been added, a set is used


Runtime: O(N + M * logM) where N is the size of arr, and M is the input k
Space: O(M)
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        heap.append((arr[0] / arr[-1], 0, -1))

        added = set()

        numOutcome = 0
        denOutcome = 0

        while k > 0:
            lowest, numOutcome, denOutcome = heapq.heappop(heap)
            if numOutcome < n and (numOutcome + 1, denOutcome) not in added:
                heapq.heappush(
                    heap, (arr[numOutcome + 1] / arr[denOutcome], numOutcome + 1, denOutcome))
                added.add((numOutcome + 1, denOutcome))
            if denOutcome > -n - 1 and (numOutcome, denOutcome - 1) not in added:
                heapq.heappush(
                    heap, (arr[numOutcome] / arr[denOutcome - 1], numOutcome, denOutcome - 1))
                added.add((numOutcome, denOutcome - 1))
            k -= 1

        return [arr[numOutcome], arr[denOutcome]]


"""
Updated Solution: Improved runtime and reduced memory usage
Code derived from observing other submissions

- By adding all the other numerators divided by the largest denominator at the start,
the need for the set is eliminated

Same runtime and memory complexity, but the set added a massive amount of runtime and space overhead
"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for idx, num in enumerate(arr[:-1]):
            heapq.heappush(heap, ((arr[idx] / arr[-1], idx, -1)))

        numOutcome = 0
        denOutcome = 0

        while k > 0:
            lowest, numOutcome, denOutcome = heapq.heappop(heap)
            if denOutcome > -n - 1:
                heapq.heappush(
                    heap, (arr[numOutcome] / arr[denOutcome - 1], numOutcome, denOutcome - 1))
            k -= 1

        return [arr[numOutcome], arr[denOutcome]]
