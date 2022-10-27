# leetcode problem # 835. Image Overlap

"""
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 

Example 1:
https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.
https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg
The number of positions that have a 1 in both images is 3 (shown in red).
https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg

Example 2:
Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:
Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:
n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""

"""
Solution 1 from leetcode solutions: Shift and Count

Notes:
1. Shifting matrix A to the left is equivalent to shifting matrix B to the right
2. With no rotation, possible directions for shifting are: left, right, up, down.
3. Combining 1 and 2, the algorithm can first shift matrix A to the right and down and compare with original matrix B,
    then shift matrix B to the right and down and compare with original matrix A

To compare, the algorithm compares matrix A and matrix B (either could be shifted) cell by cell, and counting the number of
    cells that both contain 1.

Runtime: O(N^4)
Space: O(N^2)
"""


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def shift_and_count(x_shift, y_shift, M, R):
            """ 
                Shift the matrix M in up-left and up-right directions 
                  and count the ones in the overlapping zone.
                M: matrix to be moved
                R: matrix for reference

                moving one matrix up is equivalent to
                moving the other matrix down
            """
            left_shift_count, right_shift_count = 0, 0
            for r_row, m_row in enumerate(range(y_shift, dim)):
                for r_col, m_col in enumerate(range(x_shift, dim)):
                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        left_shift_count += 1
                    if M[m_row][r_col] == 1 and M[m_row][r_col] == R[r_row][m_col]:
                        right_shift_count += 1

            return max(left_shift_count, right_shift_count)

        max_overlaps = 0
        # move one of the matrice up and left and vice versa.
        # (equivalent to move the other matrix down and right)
        for y_shift in range(0, dim):
            for x_shift in range(0, dim):
                # move the matrix A to the up-right and up-left directions
                max_overlaps = max(
                    max_overlaps, shift_and_count(x_shift, y_shift, A, B))
                # move the matrix B to the up-right and up-left directions
                #  which is equivalent to moving A to the down-right and down-left directions
                max_overlaps = max(
                    max_overlaps, shift_and_count(x_shift, y_shift, B, A))

        return max_overlaps


"""
Solution 2 from leetcode solutions (inspired by TejPatel18 in the discussion forum): Linear Transformation

Instead of checking all possible combinations by shifting one matrix to all possible positions and comparing with
    the other matrix, this algorithm focuses on only the cells with non-zero values.
-> By checking all possible vectors by shifting every cell to match another cell, the program can find which vector
    provides the maximum number of matches.

Runtime: O(N^4) where N is the length of the matrices
- There are up to O(N^2) cells with non-zero values in each matrix
- Each non-zero value in matrix A is compared against every non-zero value in matrix B
    -> the number of cells are multiplied together, resulting in O(N^4) operations
Space: O(N^2) where N is the length of the matrices
"""


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        dim = len(A)

        def non_zero_cells(M):
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        ret.append((x, y))
            return ret

        transformation_count = defaultdict(int)
        max_overlaps = 0

        A_ones = non_zero_cells(A)
        B_ones = non_zero_cells(B)

        for (x_a, y_a) in A_ones:
            for (x_b, y_b) in B_ones:
                vec = (x_b - x_a, y_b - y_a)
                transformation_count[vec] += 1
                max_overlaps = max(max_overlaps, transformation_count[vec])

        return max_overlaps


"""
Solution 3 from leetcode solutions (inspired by HeroKillerEver in the discussion forum): Image Convolution

Convolution is performing a dot product of two matrices 
    (multipliying the value of matrix A with the value of matrix B in the corresponding index, then summing them)

"Usually, the image convolution is performed between an image and a specific kernel matrix, in order to obtain 
certain effects such as blurring or sharpening. In our case, we would perform the convolution between the matrix A 
and the shifted matrix B which serves as a kernel."

To build the kernal, matrix B is expanded to width and height of (2N - 1), with the original matrix B in the center and
    the outside padded with 0's

The logic is very similar to the shift and count strategy, but instead of counting, dot product is used.

Runtime: O(N^4)
Space: O(N^2)

"""


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim * 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps
