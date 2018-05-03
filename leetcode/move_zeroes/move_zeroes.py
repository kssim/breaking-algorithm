# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_cnt = nums.count(0)
        for _ in range(zero_cnt):
            nums.remove(0)
            nums.append(0)
