class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = 0
        end, currentEnd, maxReach = len(nums) - 1, 0, 0

        for i in range(end):
            currentReach = i + nums[i]
            maxReach = max(currentReach, maxReach)

            if i == currentEnd:
                currentEnd = maxReach
                minJumps += 1

                if maxReach >= end:
                    return minJumps
        return minJumps
