# -*- encode: utf-8 -*-
#!/usr/bin/python3
# Problem : https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.get_binary_path(root)

    def get_binary_path(self, root):
        path = []
        if root is None:
            return path

        if root.left is None and root.right is None:
            path.append(str(root.val))
            return path

        path += ["%s->%s" % (root.val, p) for p in self.get_binary_path(root.left)]
        path += ["%s->%s" % (root.val, p) for p in self.get_binary_path(root.right)]
        return path
