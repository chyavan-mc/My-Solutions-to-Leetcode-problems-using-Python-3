class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for item in matrix:
            if len(item) == 0:
                continue
            if item[-1]==target or item[0]==target:
                return True
            if item[0]<target and item[-1]>target:
                if target in item:
                    return True
                else:
                    return False
        return False