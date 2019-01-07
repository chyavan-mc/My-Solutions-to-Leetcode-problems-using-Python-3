class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        lis = list(str(num))
        while(len(lis)!=1):
            summ = 0
            for item in lis:
                summ += int(item)
            lis = list(str(summ))
        return int(lis[0])