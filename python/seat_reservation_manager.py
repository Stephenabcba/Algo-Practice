# leetcode problem # 1845. Seat Reservation Manager

"""
Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

Example 1:
Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

Constraints:
1 <= n <= 10^5
1 <= seatNumber <= n
For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
For each call to unreserve, it is guaranteed that seatNumber will be reserved.
At most 10^5 calls in total will be made to reserve and unreserve.
"""

"""
My solution: heap of unreserved seats

Problem analysis:
Case 1: only reserve()
    - If only init() and reserve() are called, the seats will be filled sequentially from 1 to N
Case 2: no reserve() after unreserve()
    part 1: same as case 1, the seats fill up sequentially
    part 2: unreserve() calls will leave "holes" in the reservations
Case 3: General case, reserve() and unreserved() can be called as problem dictates
    - as seen in case 2, unreserve() will leave empty seats that should be filled first
    - if all unreserved seats are filled, fill the seats sequentially

Solution: Keep a highest reserved seat and a heap of unreserved seats
- the highest reserved seat is incremented if the heap is empty
    -> the seats are being filled sequentially
- if a seat is removed, add it to the heap
- if reserve() is called when the heap has values, remove and return the smallest value in the heap

* A heap is used to constantly maintain relative order in the collection of unreserved seats

Runtime:
- init(): O(1)
- reserve(): O(logN) where N is the number of calls made
- unreserve(): O(logN)
Space: O(N) where N is the number of calls made
"""


class SeatManager:

    def __init__(self, n: int):
        self.reserved = 0
        self.freeSlots = []

    def reserve(self) -> int:
        if len(self.freeSlots) > 0:
            return heapq.heappop(self.freeSlots)
        else:
            self.reserved += 1
            return self.reserved

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.freeSlots, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
