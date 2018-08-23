class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        lis = []

        while len(S)>0:
            m=0
            p=0

            for i in range(len(S)):
                n = p
                while n!=-1:
                    m=n
                    n = S.find(S[i], n+1)
                if m == i:
                    break
                if m>p:
                    p=m
            lis.append(S[0:i+1])
            S = S[i+1:]

        for itr in range(len(lis)):
            lis[itr] = len(lis[itr])

        return lis