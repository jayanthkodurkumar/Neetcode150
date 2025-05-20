class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low = 0
        high = (rows * cols) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            midElement = matrix[mid // cols][mid % cols]
            print(midElement)
            if midElement == target:
                return True
            elif midElement < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
