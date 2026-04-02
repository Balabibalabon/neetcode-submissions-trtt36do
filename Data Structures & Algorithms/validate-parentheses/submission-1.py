class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        stack = []
        co = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in left:
                stack.append(i)
            elif stack != []:
                if co[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
            print(stack)
        return stack == []