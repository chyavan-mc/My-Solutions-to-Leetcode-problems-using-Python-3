class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return[]
        
        lis=[]
        lis.append([1])
        for i in range(1,numRows):
            lis.append([1,1])
            for j in range(i-1):
                lis[i].insert(j+1,lis[i-1][j]+lis[i-1][j+1])
        return lis