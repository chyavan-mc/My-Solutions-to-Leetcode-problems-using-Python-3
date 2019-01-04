class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        count = True
        for i in range(len(matrix)-1):
            if matrix[i][:-1]==matrix[i+1][1:]:
                count &= True
            else:
                count &= False
        return count