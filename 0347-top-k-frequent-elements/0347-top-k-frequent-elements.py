import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        heap = []

        for key in freqMap:
            counts = freqMap[key]
            heapq.heappush(heap, (-counts, key))
        # print(heap)
        res = []
        idx = 0
        while idx < k:
            res.append(heapq.heappop(heap)[1])
            idx += 1

        return res
