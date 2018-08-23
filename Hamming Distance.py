class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        z = x^y                     #Bitwise XOR can be used to identify how many bits are different
        zz = str(bin(z)).split('b')
        retval = 0
        for i in zz[1]:
            retval += int(i)        #Adding the number of ones after XORing the two numbers gives the hamming distance
        return retval