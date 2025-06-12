class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, sum = float("-inf"), 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum > maxi:
                maxi = max(sum, maxi)

            if sum < 0:
                sum = 0

        return maxi
