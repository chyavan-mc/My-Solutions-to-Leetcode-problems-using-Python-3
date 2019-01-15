class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rlis = set()
        clis = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rlis = rlis | {i}
                    clis = clis | {j}

        for i in range(len(matrix)):
            if i in rlis:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for j in range(len(matrix[0])):
            if j in clis:
                for i in range(len(matrix)):
                    matrix[i][j] = 0