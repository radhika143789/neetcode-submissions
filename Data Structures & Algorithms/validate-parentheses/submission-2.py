class Solution:
    def isValid(self, s: str) -> bool:
        m = {'{' : '}', '[' : ']', '(' : ')'}
        stack = []
        for c in s:
            if c in m:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if m[prev] != c:
                    return False
        return not stack