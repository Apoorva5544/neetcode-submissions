class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()
        max_l = 0

        for right in range(len(s)):
            while s[right]  in sett:
                sett.remove(s[left])
                left+= 1

            sett.add(s[right])
            max_l = max(max_l,right-left+1)

        return max_l