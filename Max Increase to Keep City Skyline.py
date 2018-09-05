class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = len(grid)
        y = len(grid[0])
        i = {}
        j = {}
        for itr in range(x):
            i["grid[" + str(itr) + "]"] = Solution.maxx(grid[itr])
            for itr2 in range(y):
                j["grid[" + str(itr) + "][" + str(itr2) + "]"] = i["grid[" + str(itr) + "]"] - grid[itr][itr2]

        lis = [[]]
        for itr3 in range(y):
            lis.append([])
            for itr4 in range(x):
                lis[itr3].append(grid[itr4][itr3])

        for itr5 in range(y):
            i["lis[" + str(itr5) + "]"] = Solution.maxx(lis[itr5])
            for itr6 in range(x):
                if ((j["grid[" + str(itr6) + "][" + str(itr5) + "]"]) > (
                        i["lis[" + str(itr5) + "]"] - lis[itr5][itr6])) and (
                        (j["grid[" + str(itr6) + "][" + str(itr5) + "]"]) != 0):
                    j["lis[" + str(itr5) + "][" + str(itr6) + "]"] = i["lis[" + str(itr5) + "]"] - lis[itr5][itr6]
                else:
                    j["lis[" + str(itr5) + "][" + str(itr6) + "]"] = j["grid[" + str(itr6) + "][" + str(itr5) + "]"]

        sum = 0
        for itr7 in range(y):
            for itr8 in range(x):
                sum += j["lis[" + str(itr7) + "][" + str(itr8) + "]"]

        return sum

    def maxx(liss):
        maxim = liss[0]
        for it in range(1, len(liss)):
            if maxim < liss[it]:
                maxim = liss[it]
        return maxim
