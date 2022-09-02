// leetcode problem # 729. My Calendar I

/*
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Example 1:
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:
0 <= start < end <= 10^9
At most 1000 calls will be made to book.
*/

/*
My solution after looking at hint and related topics
Leetcode hint 1:
Store the events as a sorted list of intervals. If none of the events conflict, then the new event can be added.

Leetcode related topics: BinarySearch, Design, Segment Tree, Ordered Set

The events are stored in an array, where the array is kept sorted at all times based on event start time.
Whenever book() is called, the solution binary searches for the location to insert the new event at
- if there are no conflicts, insert the event; return true
- if there are conflicts, return false

Runtime: O(N^2), where N is the number of events added
- Each book() call is O(N) runtime due to splice()
Space: O(N) total where N is the number of events added

Leetcode also includes a solution utilizing binary trees
- the events are stored in a binary tree
- insert becomes O(logN) time every call.
*/
var MyCalendar = function () {
    this.calendar = []
};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function (start, end) {
    if (this.calendar.length === 0) {
        this.calendar.push([start, end])
        return true
    }
    let binStart = 0
    let binEnd = this.calendar.length - 1
    let middle = Math.floor((binStart + binEnd) / 2)
    while (binStart <= binEnd) {
        if (this.calendar[middle][0] <= start) {
            if (this.calendar[middle][1] > start) {
                return false
            }
            binStart = middle + 1
        } else {
            if (this.calendar[middle][0] < end) {
                return false
            }
            binEnd = middle - 1
        }
        middle = Math.floor((binStart + binEnd) / 2)
    }
    this.calendar.splice(binStart, 0, [start, end])
    return true
};

/** 
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */