# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    same_value_index = -1
    for i, value in enumerate(nums):
        diff_value = target - value
        if diff_value == value:
            if same_value_index != -1:
                return [same_value_index, i]

            same_value_index = i
            continue

        if diff_value in nums:
            return [i, nums.index(diff_value)]
