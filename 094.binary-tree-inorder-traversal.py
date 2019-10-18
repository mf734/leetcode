# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderT(self, root):
        if not root:
            return []
        return self.inorderT(root.left) + [root.val] + self.inorderT(root.right)

    def inorderT2(self, root):
        stack = []
        res = []
        p = root
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right
        return res