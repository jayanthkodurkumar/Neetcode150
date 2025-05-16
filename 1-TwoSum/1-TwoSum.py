# Last updated: 5/16/2025, 1:15:57 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if(diff in hashmap):
                result.append(i)
                result.append(hashmap[diff])
                break
            else:
                hashmap[num] = i





        return result