class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(i + 1, cols):
                if i == j:
                    continue
                else:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            row = matrix[i]
            left, right = 0, len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
