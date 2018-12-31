class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for item in sorted(letters):
            if  item > target:
                return item
        return sorted(letters)[0]