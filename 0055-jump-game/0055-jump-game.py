class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdxReach = 0

        for i in range(len(nums)):

            if maxIdxReach < i:
                return False

            maxIdxReach = max(maxIdxReach, i + nums[i])

        return True
