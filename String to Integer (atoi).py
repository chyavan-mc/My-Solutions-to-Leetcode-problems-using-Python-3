class Solution:
    def myAtoi(self, sttr):
        self.stri = sttr
        self.lis = self.stri.split()
        self.i = 0
        self.sign = 1
        self.integ = 0
        self.New = ""
        if len(self.lis) == 0:
            return 0

        if self.lis[0][0] == "-":
            self.i += 1
            self.sign = -1
        if self.lis[0][0] == "+":
            self.i += 1
        while True:
            try:
                self.New += self.lis[0][self.i]
                self.integ = int(self.New)
                self.i += 1
            except:
                break
        if (self.integ >= 2 ** 31):
            return int(self.sign * 2147483648 - ((self.sign / 2) + 0.5))
        return self.integ * self.sign