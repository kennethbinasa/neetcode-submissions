class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = ('(', '{', '[')
        closing_brackets = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            
            if char in closing_brackets: 
                if stack and stack[-1] == closing_brackets[char]:
                    stack.pop()

                else:
                    return False

        if not stack:
            return True

        return False