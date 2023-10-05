# leetcode problem # 229. Majority Element II

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
"""

"""
My solution: Dictionary

Use a dictionary to count the number of occurrences of each element
Check if any of the elements have counts more than n/3

Runtime: O(N) where N is the length of nums list
Space: O(N)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        target = len(nums) / 3

        seenNums = defaultdict(int)

        for num in nums:
            seenNums[num] += 1

        for num in seenNums:
            if seenNums[num] > target:
                ans.append(num)

        return ans

"""
Solution by leetcode user MohamedMamdouh20: Boyer-Moore Majority Voting Solution
https://leetcode.com/problems/majority-element-ii/solutions/4131226/99-7-hashmap-boyer-moore-majority-voting-explained-intuition/?envType=daily-question&envId=2023-10-05

Observation: There can be at most 2 values that have more than n/3 occurrences

Logic: 2 linear passes to complete the analysis
1. Pass 1: Find the potential candidates
    - if the counted votes for any candidate is 0, the next value found is a new potential candidate
        - the potential candidates cannot be identical
    - for any number found that matches a candidate, increment the counted vote for that candidate by 1
    - if both candidates have at least 1 vote AND the encountered value is neither of the candidates, decrement
        the vote count of both candidates by 1
2. Pass 2: Count the votes for each potential candidate
    - only count the votes for the potential candidates found in pass 1
3. Checking
    - if a potential candidate has more votes than the threshold, add it to the answer

Runtime: O(N) where N is the length of nums list
Space: O(1), memory usage does not depend on input
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Counters for the potential majority elements
        count1 = count2 = 0     
        # Potential majority element candidates
        candidate1 = candidate2 = 0

        # First pass to find potential majority elements.
        for num in nums:
            # If count1 is 0 and the current number is not equal to candidate2, update candidate1.
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num

            # If count2 is 0 and the current number is not equal to candidate1, update candidate2.
            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num
            
            # Update counts for candidate1 and candidate2.
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

            # If the current number is different from both candidates, decrement their counts.
            else:
                count1 -= 1
                count2 -= 1

        result = []
        threshold = len(nums) // 3  # Threshold for majority element

        # Second pass to count occurrences of the potential majority elements.
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        # Check if the counts of potential majority elements are greater than n/3 and add them to the result.
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result