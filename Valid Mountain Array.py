class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return False
        i=0
        while A[i+1]>A[i]:
            i+=1
            if i==len(A)-1:
                return False
        if i==0:
            return False
        
        while i<len(A)-1:
            if A[i]>A[i+1]:
                i+=1
            else:
                return False
        return True