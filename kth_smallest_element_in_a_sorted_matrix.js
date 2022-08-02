// leetcode problem # 378. Kth Smallest Element in a Sorted Matrix

/*
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).


Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2


Follow up:
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
*/

/*
Solution by nitin23rathod in leetcode discussions: Binary Search (originally written in C++)
Utilize binary search in the answer space to find the value of the kth smallest element
A helper function is used to confirm the location (the xth smallest position) of the middle value every iteration of binary search
- if the middle value didn't exist in the matrix, the helper function returns the theorical position of where the value would be if it did.

Runtime: O(log(L) * N) where L is the range of values that matrix[i][j] can be, and N is the width of the matrix
- O(log(L)) is the number of times it takes to binary search to the correct value
- O(N) is the runtime of the helper solve function
- even though L can go up to 2 * 10 ^ 9, log(L) is about 30.

Space: O(1), solution memory useage does not scale with input
- this ignores the function call overhead.


*/
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (matrix, k) {
    // Solver function to find the position (theoretical) of the given mid value
    let solve = (matrix, mid) => {
        let count = 0
        let n = matrix.length
        let i = n - 1
        let j = 0
        while (i >= 0 && j < n) {
            if (matrix[i][j] > mid) {
                i--
            } else {
                count += (i + 1)
                j++
            }
        }
        return count
    }

    let n = matrix.length
    let i = matrix[0][0]
    let j = matrix[n - 1][n - 1]

    while (i < j) {
        let mid = Math.floor(i + (j - i) / 2)
        let posi = solve(matrix, mid)
        if (posi < k) {
            i = mid + 1
        } else {
            j = mid
        }
    }
    return i
};