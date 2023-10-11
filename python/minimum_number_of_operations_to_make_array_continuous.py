# leetcode problem # 2009. Minimum Number of Operations to Make Array Continuous

"""
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.


Example 1:
Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.

Example 2:
Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

Example 3:
Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

"""
My attempt: Binary Search
Failed as it could not account for certain cases

Idea: Remove duplicates, then process with binary search
By removing duplicates, the logic can properly process the values; all duplicate values must be changed to another value
The removed values are treated as "wildcard" values, and the resulting range is continuous if the wildcard values can fill in the missing
values in the range

Runtime: O(N*logN) where N is the length of nums list
Space: O(N)
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        uniqueNums = list(set(nums))
        uniqueNums.sort()

        changes = len(nums) - len(uniqueNums)

        if uniqueNums[-1] - uniqueNums[0] == len(uniqueNums) - 1 or uniqueNums[-1] - uniqueNums[0] - changes == len(uniqueNums) - 1:
            return changes

        start = 0
        end = len(uniqueNums) - 1
        shrinking = True
        expandRight = True
        count = 0

        while start < end:
            count += 1
            if count > 100:
                break
            mid = (start + end) // 2

            if shrinking:
                left = uniqueNums[mid] - uniqueNums[start]
                right = uniqueNums[end] - uniqueNums[mid]
                if right > left:
                    changes += end - mid
                    if left > changes + mid - start:
                        end = mid
                    else:
                        start = mid
                        shrinking = False
                else:
                    changes += mid - start
                    if right > changes + end - mid:
                        start = mid
                    else:
                        end = mid
                        shrinking = False
                        expandRight = False
            else:
                adjustedRange = uniqueNums[mid] - uniqueNums[0]
                adjustedLength = mid - 0
                if not expandRight:
                    adjustedRange = uniqueNums[-1] - uniqueNums[mid]
                    adjustedLength = len(uniqueNums) - 1 - mid

                if adjustedRange > adjustedLength + changes:
                    if expandRight:
                        end = mid - 1
                    else:
                        start = mid + 1
                    shrinking = True
                else:
                    if expandRight:
                        changes -= mid - start
                        start = mid
                    else:
                        changes -= end - mid
                        end = mid
                

        
        return changes
    

"""
Solution by leetcode:
Approach 2: Sliding Window
Intuition
In the previous approach, we locked in an element newNums[i] as left, calculated right, then found the insertion index of right as j. We used an O(logn) binary search to find j, but we can do better using a sliding window.

Because newNums is sorted:

As i increases, so does left = newNums[i].
An increase in the lower bound left means an increase in the upper bound right as well.
As right increases, j either remains the same or increases.
Thus, as i increases, j will stay the same or increase.

We initialize j = 0 and follow the same process as in the last approach. Iterate i over the indices of newNums and treat each left = newNums[i] as the minimum element. This gives us right = newNums[i] + n - 1 as our maximum element.

How do we update j? Similar to the last approach, we have j as the index of the first element out of our range. Thus, we increment j until it points to an element out of our range. The condition for this is:

while (newNums[j] < newNums[i] + n)

Once this condition is broken, newNums[j] is out of our range [left, right] and correctly positioned. We can calculate the number of elements already in our range as j - i just like in the previous approach.

Because j starts at 0 and cannot exceed the length of newNums, it will only be incremented at most nnn times across the entire algorithm. This means it costs O(1) amortized to calculate j, an improvement from the O(logn) binary search.

Algorithm
Set n = nums.length and the answer ans = n.
Remove duplicates from nums and then sort it. We will call this new array newNums.
Initialize j = 0 and iterate i over the indices of newNums:
While newNums[j] is within our range (less than newNums[i] + n), increment j.
Calculate count = j - i, the number of elements already in our range.
Update ans with n - count if it is smaller.
Return ans.

Complexity Analysis
Time complexity: O(nlogn) where n is the length of nums list
Space complexity: O(n)
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))
        j = 0
        
        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1
            
            count = j - i
            ans = min(ans, n - count)

        return ans