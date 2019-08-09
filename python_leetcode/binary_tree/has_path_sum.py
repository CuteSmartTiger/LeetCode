#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 22:56
# @Author  : liuhu
# @Site    : 
# @File    : has_path_sum.py
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:                                           #当前节点为空，返回Fasle
            return False
        if not root.left and not root.right and root.val==sum: #当前节点符合条件，返回True
            return True
        if root.left:
            root.left.val = root.val+root.left.val             #左节点值等于累计和
        if root.right:
            root.right.val = root.val+root.right.val           #右节点值等于累计和
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        # 递归左右子节点

# 不改变原有二叉树
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        elif root.left is not None and root.right is None:
            return self.hasPathSum(root.left, sum-root.val)
        elif root.left is None and root.right is not None:
            return self.hasPathSum(root.right, sum-root.val)
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
