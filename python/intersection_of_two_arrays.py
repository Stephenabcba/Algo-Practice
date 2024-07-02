# leetcode problem # 350. Intersection of Two Arrays II

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

"""
My solution: Store in dictionary then compare

Idea: Store all values of nums 1 in a dictionary, and compare the values in the dictionary to nums 2
- when a number in nums 2 is also in the dictionary, add it to the output
    - decrement the count stored in the dictionary

Runtime: O(N + M) where N is the length of nums 1 and M is the length of nums2
Space: O(N)

Follow up 1: If the given array is already sorted, a two-pointer approach could be taken
    - each list has a pointer initialized to the first value
    - if both values match, add the number to the output and increment both pointers
    - otherwise, increment the pointer that points to the lower value
    - Runtime remains the same, but space is reduced to O(1)
Follow up 2: Even if nums 1 is small, the algorithm suggested in follow up 1 would run in roughly the same runtime with
still better space complexity
Follow up 3: Both algorithms would work, but would require extra implementation to load nums2
    * assuming nums 1 and nums 2 are still sorted for the solution from follow up 1
    - load and process the first chunk from nums 2, then repeat for the remaining chunks of nums 2
        - for the 2-pointer approach, load new chunks when the pointer for nums 2 reaches the end of the current chunk
        - for the dictionary approach, load new chunks when all values have been iterated
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numDict = defaultdict(int)

        ans = []

        for num in nums1:
            numDict[num] += 1

        for num in nums2:
            if numDict.get(num, 0) > 0:
                ans.append(num)
                numDict[num] -= 1

        return ans
