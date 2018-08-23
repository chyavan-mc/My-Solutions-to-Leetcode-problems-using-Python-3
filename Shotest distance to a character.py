class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        l = len(S)
        lis, s = [],[]

        for i in range(l):
            if S[i] == C:
                lis.append(i)

        for j in range(l):
            lis2 = [abs(j-lis[k]) for k in range(len(lis))]
            s+=[min(lis2)]

        return s