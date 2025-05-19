class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(s1)):
            charIdx = ord(s1[i]) - ord("a")
            freq1[charIdx] += 1

        # print(freq1)

        left = 0
        right = len(s1) - 1

        # print(left, right)

        for i in range(0, right + 1, 1):
            charIdx = ord(s2[i]) - ord("a")
            freq2[charIdx] += 1

        # print(freq2)

        if freq1 == freq2:
            return True

        for i in range(right + 1, len(s2)):
            charIdx = ord(s2[i]) - ord("a")
            # remove left
            freq2[ord(s2[left]) - ord("a")] -= 1

            # add right
            freq2[ord(s2[i]) - ord("a")] += 1

            # check if set1 and set2 are same
            if freq1 == freq2:
                return True
                # if not slide the window
            left += 1
            right += 1

        return False
