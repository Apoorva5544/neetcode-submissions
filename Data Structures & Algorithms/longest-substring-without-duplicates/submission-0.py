class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left  = 0
        max_len = 0
        last_index = {}

        for i in range(len(s)):
            if s[i] in last_index:
                left = max(left,last_index[s[i]]+1)

            last_index[s[i]] = i
            max_len = max(max_len,i-left+1)

        return max_len
