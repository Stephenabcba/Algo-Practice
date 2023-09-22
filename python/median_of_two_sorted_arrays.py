# leetcode problem # 4. Median of Two Sorted Arrays

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

"""
Solution by leetcode: Better Binary Search

https://leetcode.com/problems/median-of-two-sorted-arrays/Figures/4/2_0.png
https://leetcode.com/problems/median-of-two-sorted-arrays/Figures/4/2_1.png

Idea: Perform a Binary Search on the smaller array
- Always partition the larger array such that the overall partition is placed at the median
    - in other words, the total count of the left side of smaller array and the left side of the larger array
        equals (m + n + 1) / 2
- The binary search becomes checking if the partition is valid
    - the partition is valid if maxLeftA <= minRightB and maxLeftB <= minRightA
        - maxLeftA: the largest value of the left partition of the smaller array
        - maxLeftB: the largest value of the left partition of the larger array
        - minRightA: the smallest value of the right partition of the smaller array
        - minRightB: the smallest value of the right partition of the larger array
    - if the partition is valid, return the median
    - otherwise:
        - if maxLeftA > minRightB 
            - the left partition of the smaller array has values larger than the right partition of the larger array
            - the actual median has to be shifted to the right of the binary search guess
            -> set the upper boundary to the binary search guess - 1
        - otherwise: (implying maxLeftB > minRightA)
            - this case only occurs if the partition was not valid, and the case above was also not satisfied
            - the left partition of the larger array has values larger than the left partitin of the smaller array
            - the actual median has to be shifted to the left of the binary search guess
            -> set the lower boundary to the binary search guess + 1

Runtime: O(log(min(m,n))) where m and n are the lengths of the 2 arrays
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)


        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1