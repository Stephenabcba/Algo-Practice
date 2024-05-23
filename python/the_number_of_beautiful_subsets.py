# leetcode problem # 2597. The Number of Beautiful Subsets
"""
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:
1 <= nums.length <= 20
1 <= nums[i], k <= 1000
"""

"""
My solution: Build all subsets

Brute force and build all subsets, making sure that every subset is beautiful

Runtime: O(2^N * logN)
Space: O(2^N * N)
"""


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def findNum(num, arr):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] == num:
                    return True
                elif arr[mid] > num:
                    high = mid
                else:
                    low = mid + 1
            return False

        nums.sort()
        beautifulSets = [[]]
        for num in nums:
            prevCount = len(beautifulSets)
            for idx in range(prevCount):
                prevSet = beautifulSets[idx]
                if not findNum(num + k, prevSet) and not findNum(num - k, prevSet):
                    newSet = prevSet[:]
                    newSet.append(num)
                    beautifulSets.append(newSet)
        return len(beautifulSets) - 1


"""
Solution In Editorial: Dynamic Programming - Optimized Iterative

Group the numbers based on their remainder values after dividing the number by k
- numbers with identical values are stored together, marked by higher frequency
    - including identical values can never make a subset not beautiful
    - there are (2 ^ x) - 1 ways to arrange a value with frequency x such that every way has at least 1 value
- numbers in the same group could make a subset not beautiful
    - when sorted, each value has a difference of y * k from the previous and the next value
        - y is any positive integer
        - only values with exactly k difference will make a subset not beautiful
            - this can only happen with consecutive values after sorting
            -> if the current value cannot be placed with the previous value, then the value before the previous value is used
                - 2 instances of previous values need to be stored:
                    1. the previous value
                    2. the value before the previous value
- numbers from different groups can never make a subset not beautiful
    -> the beautiful subsets from different groups can freely mix without creating subsets that are not
    beautiful

* The total number of beautiful subsets includes the empty set, which should be removed before returning the value

Runtime: O(N*logN)
Space: O(N)
"""


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1
        freq_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            freq_map[num % k][num] = freq_map[num % k].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in freq_map.values():
            prev_num, curr, prev1, prev2 = -k, 1, 1, 0

            # Iterate through each number in the current remainder group
            for num, freq in sorted(fr.items()):
                # Count of subsets skipping the current number
                skip = prev1

                # Count of subsets including the current number
                # Check if the current number and the previous number
                # form a beautiful pair
                if num - prev_num == k:
                    take = ((1 << freq) - 1) * prev2
                else:
                    take = ((1 << freq) - 1) * prev1

                # Store the total count for the current number
                curr = skip + take
                prev2, prev1 = prev1, curr
                prev_num = num
            total_count *= curr
        return total_count - 1
