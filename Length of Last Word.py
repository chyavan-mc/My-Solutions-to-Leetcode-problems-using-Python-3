class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        lis = s.split(' ')
        for i in range(1,len(lis)+1):
            if len(lis[-i])!=0:
                return len(lis[-i])
        if len(lis)==1:
            return len(lis[0])
        else:
            return 0