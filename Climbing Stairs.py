class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ = 0
        for i in range(int(n/2)+1):
            summ += self.comb(n-i,i)
        return int(summ)
    
    def comb(self,n,r):
        prod=1
        for i in range(0,r):
            prod*=(n-i)
        for i in range(1,r+1):
            prod/=i
        return prod