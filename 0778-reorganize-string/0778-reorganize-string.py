class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = [0] * 26

        # Create a freq map
        for i in range(n):
            ch = s[i]
            chrIdx = ord(ch) - ord("a")
            freq[chrIdx] += 1

        # determine max freq and the corresponding character
        maxFreq = 0
        letter = 0
        for i in range(26):
            if freq[i] > maxFreq:
                maxFreq = freq[i]
                letter = i

        # if our maxFreq is more than half of the string length, it is impossible to reorganize
        if maxFreq > math.ceil(n / 2):
            return ""

        res = [""] * n
        idx = 0  # idx will tell us the position to put a letter in the result string

        # fill alternate places with maxFreq letter.
        asciiVal = ord("a") + letter
        freqChar = chr(asciiVal)

        while freq[letter] > 0:
            res[idx] = freqChar
            freq[letter] -= 1
            idx += 2

        # next we continue to fill the remaining spots with other letters in alternate fashion
        for i in range(26):
            ascii_val = ord("a") + i
            char = chr(ascii_val)
            while freq[i] > 0:
                # if idx is out of bounds, set it to 1, this scenario will happen only once because this loop will run through the res string only once
                if idx >= n:
                    idx = 1

                res[idx] = char
                freq[i] -= 1
                idx += 2

        ans = "".join(res)
        return ans
