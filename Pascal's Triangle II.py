class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lis=[[1],[1,1]]
        if(rowIndex==0):
            return lis[0]
        for i in range(1,rowIndex+1):
            del lis[0]
            lis.append([1,1])
            for j in range(i-1):
                lis[1].insert(j+1,lis[0][j]+lis[0][j+1])
        return lis[1]