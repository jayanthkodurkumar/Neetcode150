class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []

        for string in strs:
            freqKey = self.getFrequency(string)

            if freqKey in hashmap:
                hashmap[freqKey].append(string)
            else:
                hashmap[freqKey] = []
                hashmap[freqKey].append(string)

        for key in hashmap:
            ans.append(hashmap[key])
        # print(hashmap)
        return ans

    def getFrequency(self, string: str) -> str:
        freqString = ""
        freqArray = []

        for i in range(0, 26):
            freqArray.append(0)

        for i in range(len(string)):
            ch = string[i]
            idx = ord(ch) - ord("a")
            freqArray[idx] += 1
        # print(freqArray)
        for i in range(len(freqArray)):
            character = ch = chr(ord("a") + i)
            characterCountString = str(freqArray[i])
            freqString += str(character) + characterCountString

        return freqString
