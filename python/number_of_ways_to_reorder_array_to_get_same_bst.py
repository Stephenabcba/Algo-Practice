# leetcode problem # 1569. Number of Ways to Reorder Array to Get Same BST


"""
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
https://assets.leetcode.com/uploads/2020/08/12/bb.png
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

Example 2:
https://assets.leetcode.com/uploads/2020/08/12/ex1.png
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

Example 3:
https://assets.leetcode.com/uploads/2020/08/12/ex4.png
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
"""

"""
My attempt: DP
Failed due to runtime exceeding at 45 values in nums

Runtime: O(N^3) where N is length of nums
Space: O(N)
"""


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        bigPrime = int(1e9 + 7)
        

        class TreeNode:
            def __init__(self, nodeVal):
                self.val = nodeVal
                self.left = None
                self.right = None

        root = None
        for num in nums:
            if root:
                cur = root
                placed = False
                while not placed:
                    if num < cur.val:
                        if cur.left:
                            cur = cur.left
                        else:
                            cur.left = TreeNode(num)
                            placed = True
                    else:
                        if cur.right:
                            cur = cur.right
                        else:
                            cur.right = TreeNode(num)
                            placed = True
            else:
                root = TreeNode(num)
        
        self.ways = 0
        dp = {}
        
        def traverse(node):
            included[node.val] = True
            includedTup = tuple(included)

            if includedTup in dp:
                included[node.val] = False
                self.ways += dp[includedTup] % bigPrime
                return dp[includedTup]

            available.remove(node)

            hasLeft = False
            hasRight = False
            
            if node.left:
                hasLeft = True
                available.add(node.left)
            if node.right:
                hasRight = True
                available.add(node.right)

            if len(available) == 0:
                included[node.val] = False
                available.add(node)
                self.ways += 1
                return 1

            curWays = 0

            for chosenNode in list(available):
                curWays += traverse(chosenNode)

            if hasLeft:
                available.remove(node.left)
            if hasRight:
                available.remove(node.right)
            dp[includedTup] = curWays
            available.add(node)
            included[node.val] = False
            return curWays

        available = {root}
        included = [False for _ in range(len(nums) + 1)]

        traverse(root)

        return (self.ways - 1) % bigPrime

"""
Solution from Leetcode: DFS with permutation formula

The total number of ways to get the same BST can be found with the following:
Total Ways = left subtree ways * right subtree ways * P
where:
    - left subtree ways is the number of arrays that create the left subtree
    - right subtree ways is the number of arrays that create the right subtree
    - P is the number of ways that the left (or right) subtree can populate the overall array
        1. the root of the tree must remain in the first position
        2. the relative order within the left subtree must remain the same
        3. the relative order within the right subtree must remain the same
        * 2 and 3 only applies at the current level; as sublevels traverse, the order might be able to change.
        -> P is the permutation of choosing len(left nodes) out of M - 1 possible locations

The total ways equation can be recursively applied to the left subtree and the right subtree
to find their values
- if there are fewer than 2 nodes in the tree/subtree, there's only 1 way to arrange the array to create the BST

Runtime: O(N^2) where N is the length of nums
Space: O(N^2)
"""

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m < 3: 
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod
        
        return (dfs(nums) - 1) % mod

