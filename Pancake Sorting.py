class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A)==0 or len(A)==1:
            return []
        
        if A[-1]==max(A):
            return self.pancakeSort(A[:-1])
        else:
            n = A.index(max(A))
            A = list(reversed(A[:n+1])) + A[n+1:]
            A = list(reversed(A))
            if n==0:
                return [len(A)] + self.pancakeSort(A[:-1])
            return [n+1,len(A)] + self.pancakeSort(A[:-1])