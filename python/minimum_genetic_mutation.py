# leetcode problem # 433. Minimum Genetic Mutation

"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.


Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:
0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

"""
Solution in leetcode solutions: BFS

Using a queue and a seen set, a BFS algorithm can be built exploring all possible routes from start to end,
with the mutation sequences in bank list as nodes.

Logic:
1. Initialize the queue and the seen set
2. Iterate through all items in the queue (the queue grows during this step)
    - If the item is the end str, the path has been found from start to end, return the number of steps taken
    - Otherwise, explore all possible mutations of the current item
        - if the item has been seen, there's no need to process it again
        - if the item is not in the bank, there's no need to process it
        - if both conditions above were not met, an unexplored node has been found
            - increment the steps from the current item and add the new node to the queue
3. If the queue is empty before the end is reached, there is no path from start to end. Return -1

Runtime: O(M) where M is the number of items in the bank list
- Gene length and the possible gene pieces are both constant
Space: O(1)
- Gene length and the possible gene pieces are both constant
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i + 1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1
