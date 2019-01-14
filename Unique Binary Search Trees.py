class Solution:
    dict = {0:1, 1:1}
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in self.dict.keys():
            return self.dict[n]

        summ=0
        for i in range(1,n+1):
            summ += self.numTrees(i-1) * self.numTrees(n-i)
        self.dict[n]=summ
        return summ