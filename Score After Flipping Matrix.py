class Solution:

    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        retval = True

        while retval:
            for inc in range(len(A)):
                retval = Solution.fliphorizontal(A[inc])

            for j in range(len(A[0])):
                retval = Solution.flipvertical(A, j)

        return Solution.summo(A)


    def nstrin(listEl):
        st = ''
        for fg in listEl:
            st += str(1 - fg)
        return st


    def strin(listEl):
        st = ''
        for fg in listEl:
            st += str(fg)
        return st


    def fliphorizontal(lisFH):
        if int(Solution.strin(lisFH), 2) < int(Solution.nstrin(lisFH), 2):
            for hj in range(len(lisFH)):
                lisFH[hj] = 1 - lisFH[hj]
            return True
        return False


    def flipvertical(lislis, numb):
        listo = []
        for cc in lislis:
            listo.append(cc[numb])
        if listo.count(1) < listo.count(0):
            for dd in range(len(lislis)):
                lislis[dd][numb] = 1 - lislis[dd][numb]
            return True


    def summo(listolist):
        summ = 0
        for zz in listolist:
            st = ''
            for qq in zz:
                st += str(qq)
            summ += int(st, 2)
        return summ