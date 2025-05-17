class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = -1

        i = 0
        j = len(height) - 1

        while i < j:
            l = min(height[i], height[j])
            b = j - i

            currentArea = l * b
            ans = max(currentArea,ans)

            if height[i] < height[j]:
                i+=1
            else:
                j-=1

        return ans
