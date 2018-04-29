# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/maximum-swap/description/

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        sorted_list = list(str_num)
        sorted_list.sort()

        for i, n in enumerate(str_num):
            max_num = sorted_list.pop()
            if max_num == n:
                continue
            else:
                index = (len(str_num) - 1) - str_num[::-1].index(max_num)
                ret = list(str_num)

                ret[i] = max_num
                ret[index] = n
                return int("".join(ret))
        return num
