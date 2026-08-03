class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0 or abs(ord(i) - ord(stack[len(stack) - 1])) > 2:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0