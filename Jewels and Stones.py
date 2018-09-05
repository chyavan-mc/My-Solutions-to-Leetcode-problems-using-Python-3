class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c = 0
        for i in range(len(J)):
            c += S.count(J[i])
        return c