# leetcode problem # 1700. Number of Students Unable to Eat Lunch

"""
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the jth student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.


Example 1:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Example 2:
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

Constraints:
1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.
"""

"""
My solution: Count the students

Observation: The order that the students are in do not matter
- although the students move in a queue until a student gets the matching sandwich, the order that
the students get the sandwich do not affect the end result
- for each sandwich, there are 2 possible outcomes
    - a student who prefers the sandwich takes it
        - the number of hungry students of that type reduces by 1
        - the next sandwich gets processed
    - there are no more hungry students who prefer this type of sandwich
        - the line is stuck, and no more progress can be made
        - return the number of sandwiches/students left over
- if all students get a sandwich, return 0

Runtime: O(N) where N is the number of students (or sandwiches)
Space: O(1), memory usage does not depend on input
"""


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        oneCount = 0
        zeroCount = 0
        for student in students:
            if student == 1:
                oneCount += 1
            else:
                zeroCount += 1

        idx = 0

        while idx < len(sandwiches):
            if sandwiches[idx] == 0:
                if zeroCount == 0:
                    return len(sandwiches) - idx
                zeroCount -= 1
            else:
                if oneCount == 0:
                    return len(sandwiches) - idx
                oneCount -= 1

            idx += 1

        return 0
