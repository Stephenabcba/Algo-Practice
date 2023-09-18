# leetcode problem # 1337. The K Weakest Rows in a Matrix

"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.


Example 1:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].

Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""

"""
My solution: make count and insert into heap

Counting logic: The problem boundaries requires that the soldiers are placed before the civilians
in a row
-> for each row, only need to process up to the first 0, and the count of 1 is the number of soldiers in the row

Keeping track of the weakest rows:
- A heap can be used to quickly find the weakest row
- Sorting logic: 
    1. sort first by the number of soldiers in the row
    2. if two rows have the same number of soldiers, the smaller row index is the weaker row

Overall logic
1. iterate over each row
    i. count the number of soldiers
    ii. add the number of soldiers, along with the row index, to the heap
2. remove k items from the heap, adding the index of the removed item to the answer list
3. return the answer list

Runtime: O(M*N + M*logM) where M is the number of rows, and N is the number of columns
Space: O(M)
"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for row in range(len(mat)):
            soldierCount = 0
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    soldierCount += 1
                else:
                    break
            heapq.heappush(heap,[soldierCount, row])
        
        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans