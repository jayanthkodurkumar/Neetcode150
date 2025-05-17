class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        
        ss = list(s)
        tt = list(t)

        ss.sort()
        tt.sort()


        ss = ''.join(ss)
        tt = ''.join(tt)
        print(ss)
        print(tt)


        for ch in s:
            if ch in sMap:
                sMap[ch] = sMap[ch] + 1
            else:
                sMap[ch] = 1
        
        for ch in t:
            if ch in tMap:
                tMap[ch] = tMap[ch] + 1
            else:
                tMap[ch] = 1

        return sMap == tMap