class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == '(' and c != ')':
                    return False
                elif stack[-1] == '{' and c != '}':
                    return False
                elif stack[-1] == '[' and c != ']':
                    return False
                stack.pop()
        
        return len(stack) == 0