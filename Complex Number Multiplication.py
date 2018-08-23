class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        lisa = a.split('+')
        lisb = b.split('+')

        a1 = int(lisa[0])
        b1 = int(lisa[1][:-1])
        a2 = int(lisb[0])
        b2 = int(lisb[1][:-1])

        return str((a1*a2)-(b1*b2))+"+"+str((a1*b2)+(a2*b1))+"i"