class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                # int(a / b) truncates toward zero (e.g., int(-3 / 2) == -1)
                stack.append(int(a / b))
            else:
                # Convert numeric string token (including negatives like "-11") to int
                stack.append(int(token))

        return stack[0]