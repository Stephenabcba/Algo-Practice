# leetcode problem # 823. Binary Trees With Factors

"""
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:
1 <= arr.length <= 1000
2 <= arr[i] <= 109
All the values of arr are unique.
"""

"""
My solution: Dynamic programming

After sorting arr, any product that equals x must have indeces lower than that of x
If y and z make up x, and there are multiple ways to arrange y and/or z, the ways to make up
    x are:
    1. ways[y] * ways[z] * 2 if y and z are not the same value
        - y could be placed on the left side or the right side, creating 2 different ways
    2. ways[y] ^ 2 if y == z
Use binary search to find if z exists given x and y
    - iteratively go through every x and y

The final answer is the sum of all ways for every number in arr
- use modulo as needed

Runtime: O(N^2 * logN) where N is the length of the arr list
Space: O(N)
"""

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = [-1 for _ in arr]

        arr.sort()

        for idx, num in enumerate(arr):
            ways = 1
            for leaf1 in range(idx):
                low = leaf1
                high = idx
                if arr[leaf1] * arr[low] > num:
                    break
                while low <= high:
                    mid = (low + high) // 2
                    product = arr[mid] * arr[leaf1]
                    if product == num:
                        if leaf1 == mid:
                            ways += dp[leaf1] ** 2
                        else:
                            ways += dp[leaf1] * dp[mid] * 2
                        break
                    elif product > num:
                        high = mid - 1
                    else:
                        low = mid + 1

            dp[idx] = ways % 1000000007
        ans = 0
        for num in dp:
            ans = (ans + num) % 1000000007

        return ans