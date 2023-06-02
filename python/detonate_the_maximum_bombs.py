# leetcode problem # 2101. Detonate the Maximum Bombs

"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example 1:
https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-3.png
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example 2:
https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-2.png
Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

Example 3:
https://assets.leetcode.com/uploads/2021/11/07/desmos-eg1.png
Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.

Constraints:
1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 10^5
"""

"""
My solution: Build the edges dictionary then DFS

Using the distance formula sqrt((x_1 - x_2)^2 + (y_1 - y_2)^2), it can be determined whether
a bomb is able to detonate another bomb
Apply the formula to all combinations of bomb pairs and keep track of which bomb can detonate
another bomb, thereby building the edges of the graph

Using DFS, the logic can traverse the graph to find the number of bombs an initial bomb can detonate
in total

Initiate DFS on all bombs to find the maximum bombs detonated.

Runtime: O(N^3) where N is the number of bombs in total
Space: O(N^2)
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        reachable = {}
        for bomb in range(len(bombs)):
            reachable[bomb] = []
        for bomb1 in range(len(bombs)):
            for bomb2 in range(bomb1 + 1, len(bombs)):
                bomb1x, bomb1y, bomb1r = bombs[bomb1]
                bomb2x, bomb2y, bomb2r = bombs[bomb2]

                r = sqrt((bomb1x - bomb2x)** 2 + (bomb1y - bomb2y)**2)
                if r <= bomb1r:
                    reachable[bomb1].append(bomb2)
                if r <= bomb2r:
                    reachable[bomb2].append(bomb1)
        mostDetonated = 1
        memo = [False for _ in bombs]
        def detonate(detonateIdx):
            memo[detonateIdx] = True
            blastCount = 1
            for bomb in reachable[detonateIdx]:
                if not memo[bomb]:
                    blastCount += detonate(bomb)
            return blastCount
            
        for bomb in range(len(bombs)):
            memo = [False for _ in bombs]
            detonated = detonate(bomb)
            if detonated > mostDetonated:
                mostDetonated = detonated
        return mostDetonated