class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        sum=0
        while(n/(5**i)!=0):
            sum+=int(n/(5**i))
            i+=1
        return sum