# leetcode problem # 2336. Smallest Number in Infinite Set

"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Example 1:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""

"""
My solution: use heap and set

Intuition:
- If the class only has popSmallest() method, the class can just keep track of 1 integer, incrementing and returning the value
every call
- the values added back should be unique and sorted
    -> this can be done with keeping a set and a heap of the values added back

Logic:
- Init: initialize the heap, the set, and the integer to return
- popSmallest:
    - if the heap is empty: increment and return the integer value
    - if the heap is not empty: pop the smallest value in the heap, and remove the value from the set
- addBack:
    - if the value is larger than the integer or the value is in the addback set, there's no need to add it back
    - otherwise, add the value to the heap and set

* According to leetcode, the duplicate data structures can be combined into 1 sorted set.

Runtime:
- Initialization: O(1)
- popSmallest(): O(logN) where N is the number of operations done
- addBack(): O(logN)

Space: O(N) where N is the number of operations done
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.addBackHeap = []
        self.addBackSet = set()
        self.nextSequentialNum = 1

    def popSmallest(self) -> int:
        if len(self.addBackHeap) == 0:
            val = self.nextSequentialNum
            self.nextSequentialNum += 1
            return val
        else:
            val = heapq.heappop(self.addBackHeap)
            self.addBackSet.remove(val)
            return val

    def addBack(self, num: int) -> None:
        if num < self.nextSequentialNum and num not in self.addBackSet:
            self.addBackSet.add(num)
            heapq.heappush(self.addBackHeap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
