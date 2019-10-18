# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        self.isBalanced = True
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if not self.isBalanced or abs(left - right) > 1:
                self.isBalanced = False
            return max(left, right) + 1

        dfs(root)
        return self.isBalanced



# basic
class Solution2(object):
    def isBala(self, root):
        def height(self, node):
            if not node:
                return 0
            return 1 + max(height(node.right), height(node.left))
        if not root:
            return True
        return abs(self.height(root.right)-self.height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)