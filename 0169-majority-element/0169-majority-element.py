class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = floor(len(nums) / 2)

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

            if dict[nums[i]] > n:
                return nums[i]

        return -1
