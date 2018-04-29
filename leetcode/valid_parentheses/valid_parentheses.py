# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {"{":"}", "[":"]", "(":")"}

        for c in s:
            if c in match.keys():
                stack.append(c)
            elif c in match.values():
                if len(stack) == 0 or match.get(stack[-1]) != c:
                    return False
                else:
                    stack.pop()

        return True if len(stack) == 0 else False
