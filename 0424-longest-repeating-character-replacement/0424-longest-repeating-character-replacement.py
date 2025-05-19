# We slide a window, each time i move the right ptr, i will calculate the maxFreq character of that window.
# Total char to repalce will be windowLen - maxFreq. If this is greater than k, then shrink the window to bring it below k.
# maxFreq as each time we slide right will be teh max of s[right] freq and current max freq (this is calculated because
#  in the beginning we add the first character to window whose count will be the maxFreq char)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqArray = [0] * 26
        maxWindow = 0

        left, right = 0, 0
        maxFreq = 0
        for right in range(len(s)):

            freqArray[ord(s[right]) - ord("A")] += 1

            maxFreq = max(maxFreq, freqArray[ord(s[right]) - ord("A")])

            windowLen = right - left + 1
            chars_to_replace = windowLen - maxFreq

            if chars_to_replace > k:
                freqArray[ord(s[left]) - ord("A")] -= 1
                left += 1

            windowLen = right - left + 1
            maxWindow = max(maxWindow, windowLen)
        return maxWindow
