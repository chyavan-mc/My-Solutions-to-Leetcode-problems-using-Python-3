class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return str(bin(n))[2:].count('1')==1 and int(n/abs(n))==1