class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = Solution.reverse(A[i])
            Solution.invert(A[i])
        return A

    def invert(lis):
        for j in range(len(lis)):
            lis[j] = 1 - lis[j]

    def reverse(liss):
        li = tuple(liss)
        for i in range(len(li)):
            liss[len(li) - i - 1] = li[i]
        return liss
