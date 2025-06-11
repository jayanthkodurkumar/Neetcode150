class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        if n <=1:
            return n
        window_set = set()
        max_window = 0
        curr_window = 0

        for right in range(0, n):
            curr_ch = s[right]
            # print(curr_ch, right)
            while curr_ch in window_set:
                window_set.remove(s[left])
                left += 1

            window_set.add(curr_ch)
            curr_window = right - left + 1
            max_window = max(curr_window, max_window)

        return max_window
