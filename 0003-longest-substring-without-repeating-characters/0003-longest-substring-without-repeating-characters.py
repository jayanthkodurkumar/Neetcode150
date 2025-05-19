# so the core idea here is :

# "abcabcbb"

# at idx 3 -> ch = 'a'
# but a is already a part of our window. our goal is to remove all the characters until including
# the duplicating 'a' before ch. instead of using a freq map, if i know the last idx where i saw this 'a' ,
# i can just move my left ptr to that idx + 1. The intuititon here is based on the rule that in a 
# substring window all the chars occur maximum once.

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
