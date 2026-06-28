class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(s:str,i:int,j:int) -> bool:
            while(i<j):
                if(s[i]!=s[j]):
                    return False
                i += 1
                j -= 1
            return True
        i = 0
        j = len(s) -1
        while(i<j):
            if (s[i] == s[j]):
                i += 1
                j -= 1
            else:
                return (check_palindrome(s,i+1,j) or check_palindrome(s,i,j-1))
        return True