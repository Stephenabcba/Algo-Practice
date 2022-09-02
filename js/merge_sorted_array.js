// leetcode problem # 88. Merge Sorted Array

/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 10^9
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
*/

/*
My solution: working backwards

Modified from a similar problem of merging sorted arrays, but returning a new array instead
- have two indeces, one for each array
- compare the values at each index, and push the smaller one to the answer array
    - increment the index of the array where the value was used
    - it doesn't matter which value is pushed first if the values at both arrays' indeces are equal

Implementation for this algorithm, where the solution array is a modified input array
- it's possible to move the values in nums1 in the back, but that requires extra time
- by iterating from back to front, the pre-processing is not required.
- if either array has no values left to add to the sorted array, use values from the remaining array
- if both arrays has values leftover, use the larger one as the value for the current index

*/

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
    for (let i = m + n - 1; i >= 0; i--) { // iterating from back to front
        // if either index reaches 0, use values from the other array
        if (m == 0) {
            n--
            nums1[i] = nums2[n]
        } else if (n == 0) { // might be a condition to exit loop early
            m--
            nums1[i] = nums1[m]
        } else if (nums1[m - 1] > nums2[n - 1]) { // compare and take the larger value if both arrays still has values leftover.
            m--
            nums1[i] = nums1[m]
        } else {
            n--
            nums1[i] = nums2[n]
        }
    }
};

/*
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1. (*styling removed when copied to js file)

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
*/