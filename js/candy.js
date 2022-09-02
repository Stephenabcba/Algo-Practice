// leetcode problem # 135. Candy

/*
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Additional test cases:
[1,2,3,4,5]
[5,4,3,2,1]
[1,2,3,4,5,6,5,4,3,2,1]
[1,3,45,2,4,5,1,2,3,4,5,6,4,2,1,2,34,5,64,31,2]
[5,6,5,4,3,2,1]
[1,3,2,2,1]

Constraints:

n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
*/

/*
My solution:
Idea:
3 main cases:
1. a value is larger than its previous value
2. a value is smaller than its previous value
3. a value is equal to its previous value

The patterns in the array are a combination of these 3 cases.

If values in the array keeps increasing (repitition of case 1), the number of candies required for the current child will keep increasing by 1
ex: if the array is [1,3,5,7,8], the number of candies for each child will be 1,2,3,4,5, respectively.
If values in the array keeps decreasing (repitition of case 2), the earlier children will receive more candies, with the last child receiving 1 candy
ex: if the array is [5,4,3,2,1], the number of candies for each child will be 5,4,3,2,1, respectively
- in implementation: the number of candies required for the previous children in the chain of decreasing rating will all increase by 1

If any value in the array is equal to its previous value, the chain could be decoupled at the respective indexes
ex: if the array is [1,3,5,5,7,9], the number of candies for each child will be 1,2,3,1,2,3, respectively
- there are no candy requirements between two ratings that are equal to each other, so the number of candies can be reset to 1.

Pseudocode:
Iterate through each child in the ratings array:
- the first child (index 0) has a default candy of 1
    - if the chain happens to be in decreasing order, the first child will receive more candies later.
- compare each child (except the first) to the previous child's rating
    - if the current child has a higher rating, give 1 more candy to the current child than the previous child.
    - if the current child has a lower rating, give the current child 1 candy for now
        - as the decreasing chain continues, give previous children in the chain 1 more candy each for each new child in the chain
    - if the current child has an equal rating as the previous child, give the current child 1 candy for now.
    ** edge case for a decreasing chain after an increasing chain
        - if the first child in the decreasing chain has more than 1 candies, extra logic is required.
        ex: if the array is [1,6,5,4,3,2,1], the number of candies for each child will be 1,6,5,4,3,2,1, respectively
            - with the previous logic, the children will be assigned 1,2,5,4,3,2,1
        ex2: if the array is [1,2,3,4,5,3], the number of candies for each child will be 1,2,3,4,5,1, respectively
        - fix: keep track of the highest number of candies before the decreasing chain.
            - if the decreasing chain is longer than the increasing chain before, increase the number of candies that the first child in the decreasing chain receives.

Runtime: O(N) where N is the length of the ratings array.
Space: O(1); the memory usage of the algorithm does not scale with input size.
*/


/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
    let total = 1
    let curCandy = 1
    let decreasingCount = 0
    let prevCandy

    for (let i = 1; i < ratings.length; i++) {
        if (ratings[i - 1] < ratings[i]) {
            curCandy += 1
            decreasingCount = 0
            prevCandy = 0
        } else if (ratings[i - 1] > ratings[i]) {
            if (curCandy == 1) {
                decreasingCount += 1
                if (prevCandy == decreasingCount + curCandy) {
                    prevCandy = 0
                    decreasingCount += 1
                }
            } else {
                prevCandy = curCandy
                decreasingCount = 0
            }

            curCandy = 1
        } else {
            curCandy = 1
            decreasingCount = 0
            prevCandy = 0
        }
        total += curCandy + decreasingCount
    }

    return total
};