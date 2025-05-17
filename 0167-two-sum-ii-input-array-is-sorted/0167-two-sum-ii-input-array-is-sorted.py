class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        res = []
        for i in range(len(numbers)):
            key = numbers[i]
            diff = target - key
            if diff in map:
                idx_1 = min(i + 1, map[diff])
                idx_2 = max(i + 1, map[diff])
                res.append(idx_1)
                res.append(idx_2)
                break
            map[key] = i + 1

        return res
