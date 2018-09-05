class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        FinLis = []
        lis = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        for j in words:
            FinStr = ""
            for char in list(j):
                FinStr += str(lis[ord(char) - 97])
            FinLis += [FinStr]

        return len(set(FinLis))
