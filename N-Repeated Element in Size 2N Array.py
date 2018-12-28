class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i=0
        while i<int(len(A)/2)+1:
            if A.count(A[i])!=1:
                return A[i]
            else:
                i+=1