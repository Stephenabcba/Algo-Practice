// leetcode problem # 630. Course Schedule III

/*
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.


Example 1:
Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Example 2:
Input: courses = [[1,2]]
Output: 1

Example 3:
Input: courses = [[3,2],[4,3]]
Output: 0

Constraints:
1 <= courses.length <= 10^4
1 <= durationi, lastDayi <= 10^4
*/

/*
My solution: Sort the courses and keep track of the enrolled courses, sorted based on the number of days it takes to complete.
Idea:
- Observation: a course with an earlier end date has to be taken first
    - if another course with a later end date is taken first, the current course might not be available as a choice.
    -> sort the courses based on their end dates
- take all courses that do not conflict with their own end dates.
- for courses that will exceed their own end dates:
    - if a longer course is currently taken, take the current course over the longer course
        - this assumes that the current course can be taken by replacing the longer course
        - by doing so, the total number of days used is reduced without decreasing the number of courses taken
    - if the current course is longer than the longest course currently taken, do nothing.
- to keep track of the longest course taken, use a heap structure
    - negative values are inserted into the min heap to implement a max heap.

Runtime: O(N * logN), where N is the number of courses
    - sorting most likely takes O(N * logN) time
    - heap operation takes up to O(logN) time each, repeated up to O(N) times
Space: O(N), where N is the number of courses
    - sorting could take up to O(N) space
    - the heap could take up to O(N) space
*/

/**
 * @param {number[][]} courses
 * @return {number}
 */
var scheduleCourse = function (courses) {
    // min heap implementation by Ankita Masand on medium / bits and pieces
    // https://blog.bitsrc.io/implementing-heaps-in-javascript-c3fbf1cb2e65
    class MinHeap {

        constructor() {
            /* Initialing the array heap and adding a dummy element at index 0 */
            this.heap = [null]
        }

        getMin() {
            /* Accessing the min element at index 1 in the heap array */
            return this.heap[1]
        }

        insert(node) {

            /* Inserting the new node at the end of the heap array */
            this.heap.push(node)

            /* Finding the correct position for the new node */

            if (this.heap.length > 1) {
                let current = this.heap.length - 1

                /* Traversing up the parent node until the current node (current) is greater than the parent (current/2)*/
                while (current > 1 && this.heap[Math.floor(current / 2)] > this.heap[current]) {

                    /* Swapping the two nodes by using the ES6 destructuring syntax*/
                    [this.heap[Math.floor(current / 2)], this.heap[current]] = [this.heap[current], this.heap[Math.floor(current / 2)]]
                    current = Math.floor(current / 2)
                }
            }
        }

        remove() {
            /* Smallest element is at the index 1 in the heap array */
            let smallest = this.heap[1]

            /* When there are more than two elements in the array, we put the right most element at the first position
                and start comparing nodes with the child nodes
            */
            if (this.heap.length > 2) {
                this.heap[1] = this.heap[this.heap.length - 1]
                this.heap.splice(this.heap.length - 1)

                if (this.heap.length === 3) {
                    if (this.heap[1] > this.heap[2]) {
                        [this.heap[1], this.heap[2]] = [this.heap[2], this.heap[1]]
                    }
                    return smallest
                }

                let current = 1
                let leftChildIndex = current * 2
                let rightChildIndex = current * 2 + 1

                while (this.heap[leftChildIndex] &&
                    this.heap[rightChildIndex] &&
                    (this.heap[current] > this.heap[leftChildIndex] ||
                        this.heap[current] > this.heap[rightChildIndex])) {
                    if (this.heap[leftChildIndex] < this.heap[rightChildIndex]) {
                        [this.heap[current], this.heap[leftChildIndex]] = [this.heap[leftChildIndex], this.heap[current]]
                        current = leftChildIndex
                    } else {
                        [this.heap[current], this.heap[rightChildIndex]] = [this.heap[rightChildIndex], this.heap[current]]
                        current = rightChildIndex
                    }

                    leftChildIndex = current * 2
                    rightChildIndex = current * 2 + 1
                }
            }

            /* If there are only two elements in the array, we directly splice out the first element */

            else if (this.heap.length === 2) {
                this.heap.splice(1, 1)
            } else {
                return null
            }

            return smallest
        }
    }

    // sort the courses based on end date
    courses.sort((a, b) => a[1] - b[1])

    // iterate through each course
    let days = 0
    let enrolledCourses = 0
    let minHeap = new MinHeap()
    for (let course of courses) {
        // if a course can be taken without exceeding the end date, take the course
        if (days + course[0] <= course[1]) {
            enrolledCourses += 1
            days += course[0]
            minHeap.insert(-course[0])
        } else if (minHeap.getMin() + days + course[0] <= course[1] && course[0] < -minHeap.getMin()) {
            // if a course cannot be taken without exceeding the end date:
            //      - if it can be taken instead of a longer course, take the course over the longer course
            //      - otherwise, do nothing.
            let removedCourse = -minHeap.remove()
            days -= removedCourse
            days += course[0]
            minHeap.insert(-course[0])
        }
    }
    return enrolledCourses
};