class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        count = 0
        while count<len(tokens):
            if tokens[count] not in ["+", "-", "*", "/"]:
                stack.append(tokens[count])
            else:
                numt = int(stack.pop())
                numb = int(stack.pop())
                if tokens[count] == "+":
                    stack.append(numb + numt)
                elif tokens[count] == "-":
                    stack.append(numb - numt)
                elif tokens[count] == "*":
                    stack.append(numb * numt)
                elif tokens[count] == "/":
                    stack.append(numb / numt)
            count+=1
        return int(stack.pop())