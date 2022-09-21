# leetcode problem # 985. Sum of Even Numbers After Queries

"""
You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.


Example 1:
Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

Example 2:
Input: nums = [1], queries = [[4,0]]
Output: [0]

Constraints:

1 <= nums.length <= 10^4
-104 <= nums[i] <= 10^4
1 <= queries.length <= 10^4
-104 <= val_i <= 10^4
0 <= index_i < nums.length
"""


"""
My solution: Keep a running total of even values

Observation: For each query, only one value is changed.
- The sum changes depending on the initial and changed value
    - if the initial value was even:
        - if the changed value is even, the difference between changed and initial value is added to sum
        - if the changed value is odd, the initial value is subtracted from the sum
    - if the inital value is odd:
        - if the changed value is even, the changed value is added to sum
        - if the changed value is odd, sum remains the same

Logic:
1. Find the initial sum of all even values in the nums array
2. Process each query
    - for each query, change the sum according to the logic above in Observation
    - change the value in the nums array
    - record the updated sum to the answers array
3. Return the answers array

Runtime: O(N + M) where N is the length of the nums array, and M is the length of the queries array
- The logic finds an initial sum first (O(N))
- For every query, only one value is effected (O(M) total iterations)
Space: O(M) where M is the length of the queries array
- Main memory usage is answer array, which grows for every query
"""


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        curSum = 0

        for num in nums:
            if num % 2 == 0:
                curSum += num

        for query in queries:
            if nums[query[1]] % 2 == 0:
                if query[0] % 2 == 0:
                    curSum += query[0]
                else:
                    curSum -= nums[query[1]]
            else:
                if query[0] % 2 != 0:
                    curSum += nums[query[1]] + query[0]

            nums[query[1]] += query[0]
            ans.append(curSum)

        return ans
