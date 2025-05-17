class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):

            if i > 0 and (nums[i] == nums[i - 1]):
                continue

            j = i + 1
            k = n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                elif sum == 0:
                    list = [nums[i], nums[j], nums[k]]
                    res.append(list)
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1

        return res
