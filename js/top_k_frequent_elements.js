// leetcode problem # 347. Top K Frequent Elements
/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:

1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*/


/*
My solution:
Find count of each value
Sort from largest frequency to smallest frequency
Return the first k elements
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    // Find the number of occurances for each value
    const numCount = {}
    for (let num of nums) {
        if (!numCount.hasOwnProperty(num)) {
            numCount[num] = 1
        } else {
            numCount[num]++
        }
    }

    // Convert the object to array and sort from largest to smallest based on frequency
    const countArr = [...Object.entries(numCount)]
    countArr.sort((a, b) => b[1] - a[1])

    // Add the first k elements to the answer array
    const ansArr = []
    for (let i = 0; i < k; i++) {
        ansArr.push(countArr[i][0])
    }
    return ansArr
};

/*
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
*/

/*
Solution from leetcode: use a heap instead of sorting
- Build a heap of size K and convert to array
Improvements:
- the heap operation takes O(N * log k) time instead of O(N * log N) for sorting
* can also check if k == nums.length

in python, the heapq library has a heapq.nlargest(n,array,key) method

in Python, this is the solution:
from collections import Counter
count = Counter(nums)
return heapq.nlargest(k, count.keys(), key=count.get)

*/