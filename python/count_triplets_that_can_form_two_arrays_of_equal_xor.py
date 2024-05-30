# leetcode problem # 1442. Count Triplets That Can Form Two Arrays of Equal XOR

"""
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10

Constraints:
1 <= arr.length <= 300
1 <= arr[i] <= 108
"""

"""
My solution: Find the prefix and suffix

Iterate through the array to find all the subarrays starting from and ending from each index,
and store the XOR of those subarrays in 2 lists of dictionaries

Then for every i where 0 <= i < N - 1
- Find all XOR results that ends at i that matches with the XOR results that start at i + 1
- Multiply the frequencies of the matched pairs, and add to the result
Return the result at the end

Runtime: O(N^2) where N is the length of arr
Space: O(N^2)
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        startings = [defaultdict(int) for _ in arr]
        endings = [defaultdict(int) for __ in arr]

        N = len(arr)

        for i in range(N):
            cur = arr[i]
            startings[i][cur] += 1
            endings[i][cur] += 1
            for k in range(i + 1, N):
                cur ^= arr[k]
                startings[i][cur] += 1
                endings[k][cur] += 1

        ans = 0

        for i in range(N - 1):
            for key, freq in endings[i].items():
                ans += freq * startings[i + 1][key]

        return ans


"""
Solutin From Editorial: One Pass Prefix XOR

countMap is the count of occurrences of each XOR value
totalMap is an empty map to store the sum of indices where each XOR value has occurred

Runtime: O(N)
Space: O(N)
"""


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        size = len(arr)
        count = 0
        prefix = 0

        # Dictionaries to store counts and totals of XOR values encountered
        count_map = defaultdict(int)
        count_map[0] = 1
        total_map = defaultdict(int)

        # Iterating through the array
        for i in range(size):
            # Calculating XOR prefix
            prefix ^= arr[i]

            # Calculating contribution of current element to the result
            count += count_map[prefix] * i - total_map[prefix]

            # Updating total count of current XOR value
            total_map[prefix] += i + 1
            count_map[prefix] += 1

        return count
