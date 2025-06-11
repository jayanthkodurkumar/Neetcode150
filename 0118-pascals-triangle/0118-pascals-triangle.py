class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[0] * (i + 1) for i in range(numRows)]
        # print(res)
        for i in range(len(res)):
            res[i][0], res[i][len(res[i]) - 1] = 1, 1

        for i in range(2, numRows):
            for j in range(len(res[i])):
                if j != 0 and j != len(res[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res
