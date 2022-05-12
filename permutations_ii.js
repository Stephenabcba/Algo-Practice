// leetcode problem #47. Permutations II

/*
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
*/

/*
My solution: recursion
Idea: remove numbers from the nums array and add to the current permutation array
until there are no more numbers to add, and then add the number back to the nums array.
Base case: nums array is empty, the current array is 1 permutation of the nums array -> add to answer
    - the array is copied before adding to answer, as the array is further modified in future recursion.

Recursive case: nums array is not empty
- iterate through all values remaining in the nums array
- for each value:
    - remove it from the nums array
    - add it to the current array
    - recursively process the modified arrays
    - remove the value from the current array
    - add the value to the back of the nums array (so the iteration goes through a different number each time)

**Problem: the program will include duplicate permutations in the answer
Fix: implementing a seen object
- create a new seen array before iterating
    - if a value has been processed in previous iterations (exists in the seen array):
        - do not recurse the value again
        - increment the iteration counter still
        - add the value to the back to the nums array
    - if a value has not been seen:
        - add it to the seen array
        - process it normally

Note: sorting the nums array first seems to make the algorithm faster.
    - it may be due to better performance of .includes() ?

*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function (nums) {
    const recurse = (nums, curArr, result) => {
        if (nums.length == 0) {
            result.push([...curArr])
        }
        let total = nums.length
        let index = 0
        let seen = []
        while (index < total) {
            let num = nums.shift()
            if (seen.includes(num)) { // skip duplicates
                index++
                nums.push(num)
                continue
            }
            seen.push(num)
            curArr.push(num)
            recurse(nums, curArr, result)
            curArr.pop(num)
            nums.push(num)
            index++
        }
    }
    nums.sort((a, b) => a - b)
    const result = []
    recurse(nums, [], result)
    return result
};

/*
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
*/


/*
Potential improvements from leetcode solutions:
in the Python solution, the algorithm uses a Counter object and iterates through the object, which seems to automatically skip duplicates

This approach could likely be adapted into the current solution by manually creating an object keeping track of the count of all numbers in the nums array.
This eliminates the need to keep a Seen array, and constantly using .shift() on the nums array, saving on space and runtime, respectively.
*/