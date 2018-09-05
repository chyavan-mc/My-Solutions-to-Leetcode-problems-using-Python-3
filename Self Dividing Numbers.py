class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lis = []
        for i in range(left, right+1):
            count = 1
            for j in str(i):
                if int(j)==0:
                    count = 0
                    break
                if i%int(j) != 0:
                    count = 0
            if count == 1:
                lis+= [i]
        return lis