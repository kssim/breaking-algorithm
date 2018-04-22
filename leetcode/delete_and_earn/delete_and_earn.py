# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/delete-and-earn/description/

class Solution:
	def deleteAndEarn(self, nums):
        count = collections.Counter(nums)
        previous_element = None
        avoid = using = 0

        for element in sorted(count):
            using_value = max(avoid, using) if element-1 != previous_element else avoid

            avoid = max(avoid, using)
            using = element * count[element] + using_value

            previous_element = element

 		return max(avoid, using)
