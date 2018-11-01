class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        n = len(matrix)
        if n < 2: return
        
        if n == 2:
            matrix[0][0], matrix[0][1], matrix[1][1], matrix[1][0] = \
                matrix[1][0], matrix[0][0], matrix[0][1], matrix[1][1]
        else:
            for c in range(n-1, 1, -1):
                for r in range(c - (n - 1 - c)):
                    matrix[n - 1 - c][(n - 1 - c) + r], matrix[(n - 1 - c) + r][c], matrix[c][c - r], matrix[c - r][n - 1 - c] =\
                    matrix[c - r][n - 1 - c], matrix[n - 1 - c][(n - 1 - c) + r], matrix[(n - 1 - c) + r][c], matrix[c][c - r]