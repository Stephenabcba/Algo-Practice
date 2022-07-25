// leetcode problem # 4. Median of Two Sorted Arrays

/*
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

Additional Test Cases:
[1,3,5,7,9]
[2,4,6,8,10]

[1,2,3,4]
[3,4,5,6]

[1]
[]

[1,2,3,4,5]
[2]

[1,3]
[2]

[1,2]
[3,4]

[1,2,3,4,5,6,7,8,9,10]
[11,12,13,14,15,16,17,18,19,20]

[]
[1]

[]
[1,2,3,4]

[1,5]
[2,3,4,6]

[1,5]
[2,3,4]

[2,3]
[1,4,5]

[1,2,5]
[3,4,6,7]

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    const m = nums1.length
    const n = nums2.length

    let median = (nums, startIdx, endIdx) => {
        if ((endIdx - startIdx) % 2 == 0) {
            return nums[(startIdx + endIdx) / 2]
        } else {
            let mid1 = Math.floor((startIdx + endIdx) / 2)
            return (nums[mid1] + nums[mid1 + 1]) / 2
        }
    }

    if (nums1.length == 0) {
        return median(nums2, 0, n - 1)
    }

    if (nums2.length == 0) {
        return median(nums1, 0, m - 1)
    }

    let cutTarget = Math.ceil((m + n) / 2) - 1

    let evenMedian = ((m + n) % 2) == 0

    let nums1Start = 0
    let nums1End = m - 1
    let nums2Start = 0
    let nums2End = n - 1
    let cutLeft = 0
    let cutRight = 0

    let nums1Median
    let nums2Median

    while (cutLeft < cutTarget && cutRight < cutTarget) {
        nums1Median = median(nums1, nums1Start, nums1End)
        nums2Median = median(nums2, nums2Start, nums2End)
        if (nums1Median == nums2Median) {
            return nums1Median
        } else if (nums1Median > nums2Median) {
            nums1End = Math.floor((nums1End + nums1Start) / 2)
            nums2Start = Math.ceil((nums2End + nums2Start) / 2)
        } else {
            nums1Start = Math.ceil((nums1End + nums1Start) / 2)
            nums2End = Math.floor((nums2End + nums2Start) / 2)
        }

        cutLeft = nums1Start + nums2Start
        cutRight = (m + n) - (nums1End + nums2End + 2)
        if (cutLeft >= cutTarget) {
            if (nums1Start - 1 >= 0 && nums1[nums1Start - 1] > nums2[nums2Start]) {
                nums1Start -= 1
            }

            if (nums2Start - 1 >= 0 && nums2[nums2Start - 1] > nums1[nums1Start]) {
                nums2Start -= 1
            }
            cutLeft = nums1Start + nums2Start
        }
        if (cutRight >= cutTarget) {
            if (nums1End + 1 < m && nums1[nums1End + 1] < nums2[nums2End]) {
                nums1End += 1
            }
            if (nums2End + 1 < n && nums2[nums2End + 1] < nums1[nums1End]) {
                nums2End += 1
            }
            cutRight = (m + n) - (nums1End + nums2End + 2)
        }
    }

    let medianVal = 0
    if (cutLeft == cutTarget) {
        let calcLower = () => {
            if (nums2Start >= n || nums1Start < m && (nums1[nums1Start] < nums2[nums2Start])) {
                return nums1[nums1Start++]
            } else {
                return nums2[nums2Start++]
            }
        }

        medianVal = calcLower()
        if (evenMedian) {
            medianVal = (medianVal + calcLower()) / 2
        }
    } else {
        let calcUpper = () => {
            if (nums2End < 0 || nums1End >= 0 && (nums1[nums1End] > nums2[nums2End])) {
                return nums1[nums1End--]
            } else {
                return nums2[nums2End--]
            }
        }

        medianVal = calcUpper()
        if (evenMedian) {
            medianVal = (medianVal + calcUpper()) / 2
        }
    }

    return medianVal
};