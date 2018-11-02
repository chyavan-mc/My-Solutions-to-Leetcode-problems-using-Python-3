class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('L')-moves.count('R') == 0) and (moves.count('U')-moves.count('D') == 0)