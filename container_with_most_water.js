// leetcode problem # 11. Container With Most Water

/*
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
*/


// solution 1 : brute force
// failed because of O(N^2) runtime
// idea: check every possible container combination to find the max area
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    let maxArea = 0
    for (let i = 0; i < height.length - 1; i++) {
        for (let j = i + 1; j < height.length; j++) {
            let containerHeight = height[i]
            if (height[j] < height[i]) {
                containerHeight = height[j]
            }
            let curArea = (j - i) * containerHeight
            if (curArea > maxArea) {
                maxArea = curArea
            }
        }
    }
    return maxArea
};


/*
Solution 2: Greedy pointers
Idea:
- Essentially, the amount of water in a container is a rectangle
    - the width is the difference in index of the walls chosen
    - the height is the lower of the two wall heights (min height)
    - the area is width * height
- Observation: If the two walls are initialized at the frond and back of the array:
    - by moving the walls "inwards", the width of the container decreases
        - if the min height does not increase, the area of the container decreases
- Greedy selection:
    - move the shorter container wall inwards in hopes of increasing the min height
        - ex: if the left wall has height 1 and right wall has height 10,
            moving the left wall is the only way of increasing the min height of the container
        - increasing the min height may or may not increase the maximum area
            - only update the max area if the current container area is higher
    - if both walls are the same height, either wall can be moved inwards
        - if min height were to be increased, both walls will be moved eventually
            - ex: if the left and right walls both have height of 5, 
                only moving the left wall to a higher height (e.g. 10)
                will still result in a min height of 5 (since the right side is still 5)

Runtime: O(N): there is only one loop moving linearly
Space: O(1): there are no variables that scale with N
*/
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea2 = function (height) {
    let leftWall = 0
    let rightWall = height.length - 1
    let maxArea = 0

    while (leftWall < rightWall) {
        let containerWidth = (rightWall - leftWall)

        // find the minimum height of the container (for area)
        // the shorter wall is also moved inwards here
        let containerHeight = height[leftWall]
        if (height[rightWall] < height[leftWall]) {
            containerHeight = height[rightWall]
            rightWall--
        } else {
            leftWall++
        }

        // calculate the area of the current container. update max area if necessary
        let curArea = containerWidth * containerHeight
        if (curArea > maxArea) {
            maxArea = curArea
        }
    }
    return maxArea
};

/*
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
*/