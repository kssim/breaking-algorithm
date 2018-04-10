# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
    def __init__(self, x):
        self.val = x
        elf.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_sum = self.get_the_sum_of_listnode(l1)
        l2_sum = self.get_the_sum_of_listnode(l2)

        sum_of_values = self.convert_values_to_list(l1_sum + l2_sum)
        return sum_of_values

    def convert_values_to_list(self, value):
        ret = []
        while (True):
            ret.append(int(value%10))

            value = value // 10
            if value < 1:
                break
        return ret

    def get_the_sum_of_listnode(self, node, base_value=1, sum_of_node=0):
        sum_of_node = (node.val * base_value) + sum_of_node
        base_value = base_value * 10
        return sum_of_nodeurn if node.next is None else self.get_the_sum_of_listnode(node.next, base_value, sum_of_node)
