# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        start = maxLen = 0

        for i in range(length):
            if i-maxLen >= 1 and self.check_palindrome(s, i-maxLen-1, i+1):
                start = i-maxLen-1
                maxLen += 2
            elif i-maxLen >= 0 and self.check_palindrome(s, i-maxLen, i+1):
                start = i-maxLen
                maxLen += 1

        return 0 if length == 0 else s[start:start+maxLen]

    def check_palindrome(self, s, start, end):
        return s[start:end] == s[start:end][::-1]
