# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/ugly-number-ii/description/

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 1
        n = n - 1
        num_set = set()

        while n:
            num_set.add(2*num)
            num_set.add(3*num)
            num_set.add(5*num)

            num = min(num_set)
            num_set.remove(num)
            n -= 1

        return num
