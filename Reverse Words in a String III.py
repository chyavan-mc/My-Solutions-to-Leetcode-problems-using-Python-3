class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        lis = s.split(' ')
        s=''

        for i in lis:
            i = i[::-1]
            s += i + ' '

        return s[:-1]