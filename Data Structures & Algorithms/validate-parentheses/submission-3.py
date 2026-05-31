class Solution:
    def isValid(self, s: str) -> bool:
        # Stack
        # mapping = {
        #     ")": "(", 
        #     "}": "{", 
        #     "]": "["
        # }
        # stack = []
        # for char in s:
        #     if char in mapping:
        #         if stack and stack[-1] == mapping[char]:
        #             stack.pop()
        #     else:
        #         stack.append(char)
        # return not stack

        # bruteforce
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')

        return s == ''