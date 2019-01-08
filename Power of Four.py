class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        n = str(bin(num)).split('b')[1]
        if n.count('1')!=1:
            return False
        if list(reversed(n)).index('1')%2==1:
            return False
        return True