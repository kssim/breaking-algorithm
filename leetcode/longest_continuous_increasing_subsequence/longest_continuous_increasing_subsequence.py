# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums ==[]:
            return 0

        max_cnt = tmp_cnt = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                tmp_cnt +=1
                max_cnt = max_cnt if max_cnt > tmp_cnt else tmp_cnt
            else:
                tmp_cnt = 1
        return max_cnt
