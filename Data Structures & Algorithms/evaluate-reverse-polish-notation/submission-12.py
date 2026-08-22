class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in {'+','-','*','/'}:
                stack.append(int(i))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                value = 0
                if i == '+':
                    value = int(a+b)
                elif i == '-':
                    value = int(a-b)
                elif i == '*':
                    value = int(b*a)
                else:
                    value = int(a/b)

                stack.append(value)
        return stack[0]