class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while(len(str(n))!=1):
            lis = list(str(n))
            sum=0
            for i in lis:
                sum += int(i)**2
            n=sum
        return n==1 or n==7