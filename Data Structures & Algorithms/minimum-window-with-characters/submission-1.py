class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        window = Counter()

        left = 0 
        have = 0 
        result = ""

        required = len(need)

        for right in range(len(s)):
            window[s[right]] +=1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == required:
                if (right-left+1) < len(result) or result == "":
                    result = s[left:right+1]
                
                if (s[left] in need and window[s[left]] == need[s[left]]):
                    have -= 1

                window[s[left]] -= 1
                left += 1

        return result 
