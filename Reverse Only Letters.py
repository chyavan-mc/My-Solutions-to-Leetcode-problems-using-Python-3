class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # ord(char) gives the decimal value of character
        # chr(int) gives the ascii symbol of number
        strlis = []
        charlis = []
        count = [*range(65,91)] + [*range(97,123)]
        for item in S:
            if ord(item) in count:
                charlis.append(item)  
        charlis = list(reversed(charlis))
        i=0
        for item in range(len(S)):
            if ord(S[item]) in count:
                strlis.append(charlis[i])
                i+=1
            else:
                strlis.append(S[item])
        return ''.join(strlis)