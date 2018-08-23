class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        lis = [*s]
        s = ''

        for i in lis:
            s = i+s

        return s