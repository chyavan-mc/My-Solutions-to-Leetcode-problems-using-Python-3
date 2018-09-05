class Solution:
    def countAndSay(self, n):
        numb = 1
        w = 1
        while n > 1:
            w = Solution.CountSay(numb)
            numb = w
            n -= 1
        return str(w)

    def CountSay(no):
        tnumb = str(no)
        x = tnumb[0]
        count = 1
        strr = ""
        for i in range(1, len(tnumb) + 1):
            if i == len(tnumb):
                strr += str(count) + str(x)
                break
            if tnumb[i] == x:
                count += 1
            else:
                strr += str(count) + str(x)
                x = tnumb[i]
                count = 1

        return int(strr)
