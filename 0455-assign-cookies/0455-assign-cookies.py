class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n, m = len(g), len(s)
        g.sort()
        s.sort()
        l, r = 0, 0

        while l < m and r < n:
            if g[r] <= s[l]:
                l += 1
                r += 1
            else:
                l += 1

        return r
