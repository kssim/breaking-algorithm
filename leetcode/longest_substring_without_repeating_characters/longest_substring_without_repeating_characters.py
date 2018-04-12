# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start_pos = max_len = 0

        for i, c in enumerate(s):
            if c in dic and dic[c] >= start_pos:
                start_pos = dic[c]+1
            else:
                t = i - start_pos
                max_len = max_len if max_len > t else t

            dic[c] = i

        return 0 if len(s) == 0 else max_len+1
