class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # left = 0
        if len(nums) == 0:
            return 0
        nums.sort()
        currentLength = 1
        maxLength = 1
        # print(nums)
        for right in range(1,len(nums)):
            diff = nums[right] - nums[right - 1]
            print(diff)
            if diff == 0:
                continue
            elif diff == 1:
                currentLength+=1
                maxLength = max(currentLength,maxLength)
            else:
                maxLength = max(currentLength,maxLength)
                currentLength = 1



        return maxLength
        