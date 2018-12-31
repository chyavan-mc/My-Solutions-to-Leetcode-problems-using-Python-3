class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while bits.count(1)!=0:
            d = bits.index(1)
            del bits[d]
            if d == len(bits)-1:
                return False
            del bits[d]
        return True