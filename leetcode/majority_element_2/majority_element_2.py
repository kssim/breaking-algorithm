# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/majority-element-ii/description/

class Solution:
	    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        non_duplicated = list(set(nums))
        element_count = len(nums)/3
        ret = []

        for num in non_duplicated:
            if nums.count(num) > element_count:
                ret.append(num)

        return ret
