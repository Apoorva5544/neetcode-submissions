class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                stack.append(int(c))
            else:
                if(c == '+'):
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a+b)
                elif(c=='-'):
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(a-b)
                elif(c=='*'):
                    b = int(stack.pop())
                    a = int(stack.pop())
                    c = a*b
                    stack.append(c)
                else:
                    b = int(stack.pop())
                    a = int(stack.pop())
                    stack.append(int(a/b))
        return stack[0]
