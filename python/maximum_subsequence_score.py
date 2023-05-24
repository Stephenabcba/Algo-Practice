# leetcode problem # 2542. Maximum Subsequence Score

"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.


Example 1:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

Example 2:
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation: 
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.


Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[j] <= 10^5
1 <= k <= n
"""

"""
My solution: Sort and heap

Observations:
1. The numbers do not need to be processed in the given order
-> sorting may make the values easier to process
2. In the chosen subsequence, only 1 value from nums2 contribute to the score at any given time
-> only the the minimum value is multiplied with the sum
    - decreasing the multiplier would decrease the score, but the sum could be increased to result
    in a net increase in the score

Reason for sorting: By sorting the values from the largest num2 to the smallest num2, the multiplying
portion of the score only decreases when necessary

After sorting, the logic becomes checking whether the largest sum of k values up to the current index
multiplied by the current num2 results in a higher score

By using a heap, the program can maintain a sorted list of the values, such that the lowest value in the list
can be replaced by a higher value

Runtime: O(N * logN) where N is the length of the lists nums1 and nums2
Space: O(N)
"""


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combinedNums = [[nums1[idx], nums2[idx]] for idx in range(len(nums1))]

        combinedNums.sort(key=lambda x: (-x[1], -x[0]))

        selectedNums = []
        curSum = 0
        for idx in range(k):
            selectedNums.append(combinedNums[idx][0])
            curSum += combinedNums[idx][0]

        newSum = curSum
        multiplier = combinedNums[k - 1][1]

        heapq.heapify(selectedNums)

        for idx in range(k, len(nums1)):
            if combinedNums[idx][0] > selectedNums[0]:
                newSum = newSum + combinedNums[idx][0] - selectedNums[0]
                heapq.heapreplace(selectedNums, combinedNums[idx][0])
                if newSum * combinedNums[idx][1] > curSum * multiplier:
                    curSum = newSum
                    multiplier = combinedNums[idx][1]

        return curSum * multiplier
