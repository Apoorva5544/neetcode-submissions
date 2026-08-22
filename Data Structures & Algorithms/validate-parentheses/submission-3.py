class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i =='{' or i =='(' or i == '[':
                stack.append(i)
            elif i =='}' or i == ')' or i ==']':
                if not stack :
                    return False
                top = stack.pop()

                if (i ==')' and top != '(') or (i=='}'and top != '{') or (i==']' and top != '['):
                    return False
            else:
                return False

        return len(stack)==0
