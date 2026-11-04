class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if ("-" in token) and len(token) > 1:
                if token[1:].isdigit():
                    stack.append(int(token))
            elif token.isdigit():
                stack.append(int(token))
            elif token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(num1 / num2))
        return stack.pop()