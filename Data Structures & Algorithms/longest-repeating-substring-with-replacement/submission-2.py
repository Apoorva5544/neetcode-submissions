class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count = {}
        max_f = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1

            max_f = max(max_f,count[s[right]])

            while (right-left+1)-max_f >k:
                count[s[left]] -= 1
                left +=1

            result = max(result,right-left+1)

        return result