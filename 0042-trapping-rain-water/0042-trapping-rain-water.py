class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0

        left = 0
        right = 0
        tall = 0

        for i in range(0, len(height) - 1):
            if height[i] > height[i + 1]:
                left = i
                break

        for i in range(len(height) - 1, 0, -1):
            if height[i] > height[i - 1]:
                right = i
                break

        for i in range(left, right + 1):
            if height[i] > height[tall]:
                tall = i

        water = 0
        print(tall, left, right)
        j = left + 1
        while left + 1 < tall:
            if height[j] < height[left]:
                water += height[left] - height[j]
            else:
                left = j
            j += 1

        k = right
        while right - 1 > tall:
            if height[k] < height[right]:
                water += height[right] - height[k]
            else:
                right = k
            k -= 1

        return water
