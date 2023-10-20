# leetcode problem # 341. Flatten Nested List Iterator

"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].
"""

"""
My solution: Preprocess with a stack

Using a stack, the program can unpack each list and its nested components
- the current item processed is always the top of the stack
- if the current list is all processed, pop it from the stack
- if the current item is a list, push the list to the stack and process its first item
    - if that first item is still a list, repeat until an empty list is reached or an integer is reached
- when the processed item is an integer, add it to the flattened list

When next() is called, return a value from the flattened list
When hasNext() is called, check if there's values remaining in the flattened list

Runtime: O(M+N) where N is the number of values in the iterator, and M is the number of nested lists
Space: O(M+N)
"""



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattenedList = []
        self.idx = 0
        stack = [[nestedList, 0]]

        while len(stack) > 0:
            cur = stack[-1][0][stack[-1][1]]
            while not cur.isInteger():
                newList = cur.getList()
                stack.append([newList, 0])
                if len(newList) > 0:
                    cur = newList[0]
                else:
                    break
            stack[-1][1] += 1
            while stack[-1][1] >= len(stack[-1][0]):
                stack.pop()
                if len(stack) > 0:
                    stack[-1][1] += 1
                else:
                    break
            if cur.isInteger():
                self.flattenedList.append(cur.getInteger())
    
    def next(self) -> int:
        cur = self.flattenedList[self.idx]
        self.idx += 1
        return cur
    
    def hasNext(self) -> bool:
        return self.idx < len(self.flattenedList)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())