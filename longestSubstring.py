class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxlength = 0
        currentlength = 0
        ptr = 0
        for index, char in enumerate(s):
            if char not in dic:
                dic[char] = index
                currentlength += 1
                maxlength = max(maxlength, currentlength)
            else:
                currentlength = index - dic[char]
                while ptr < dic[char]:
                    dic.pop(s[ptr])
                    ptr += 1
                ptr += 1
                dic[char] = index
        return maxlength
