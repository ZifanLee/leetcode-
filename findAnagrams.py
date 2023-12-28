from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        ptr, index = 0, 0
        dic = {}
        length = len(s)
        for char in p:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        while index < length and s[index] not in dic:
            index += 1
        if index == length:
            return ans
        ptr = index
        dic[s[index]] -= 1
        if len(p) == 1:
            ans.append(ptr)
        index += 1
        while index < length:
            if s[index] not in dic:
                while ptr < index:
                    dic[s[ptr]] += 1
                    ptr += 1
                while index < length and s[index] not in dic:
                    index += 1
                if index == length:
                    return ans
                ptr = index
                dic[s[index]] -= 1
                if len(p) == 1:
                    ans.append(ptr)
                index += 1
            elif dic[s[index]] < 1:
                while s[ptr] != s[index]:
                    dic[s[ptr]] += 1
                    ptr += 1
                ptr += 1
                if len(p) == index - ptr + 1:
                    ans.append(ptr)
                index += 1
            elif dic[s[index]] >= 1:
                dic[s[index]] -= 1
                if len(p) == index - ptr + 1:
                    ans.append(ptr)
                index += 1
        return ans


s = "aaaaa"
p = "a"
solutin = Solution()
print(solutin.findAnagrams(s, p))
