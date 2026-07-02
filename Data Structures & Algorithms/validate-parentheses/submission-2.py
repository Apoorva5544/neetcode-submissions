class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if(c=='(' or c=='{' or c=='['):
                stack.append(c)
            elif(c==')'or c=='}'or c==']'):
                if not stack:
                    return False
                top = stack.pop()

                if((c==')' and top!='(')or(c=='}' and top!='{')or(c==']' and top!='[')):
                    return False
            else:
                return False
                
        return len(stack)==0

        