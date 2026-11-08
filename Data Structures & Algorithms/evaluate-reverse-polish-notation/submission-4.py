class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')

        for token in tokens:
        
            if token in operators:
                a = int(stack[-1])
                b = int(stack[-2])

                if token == '+':
                    ans = a + b

                elif token == '-':
                    ans = b - a

                elif token == '*':
                    ans = a * b

                elif token == '/':
                    ans = int(b / a)


                stack.pop()
                stack.pop()
                stack.append(str(ans))

            else:
                stack.append(token)

        return int(stack[-1])
