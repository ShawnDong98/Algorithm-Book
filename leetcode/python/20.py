class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for _ in s:
            if _ == '(' or _ == '[' or _ == '{':
                stack.append(_)

            if _ == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            if _ == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            if _ == '}':
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0: return True
        else: return False
