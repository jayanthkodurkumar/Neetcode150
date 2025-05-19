class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        left, right = 0, 0
        lastSeenIdx = {}
        maxLen = 0
        for right in range(n):
            ch = s[right]
            if ch in lastSeenIdx and lastSeenIdx[ch] >= left:
                left = lastSeenIdx[ch] + 1

            lastSeenIdx[ch] = right
            currentLen = right - left + 1
            maxLen = max(currentLen, maxLen)

        return maxLen
