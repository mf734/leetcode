# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSubtree(self, s, t):
		if not t:
			return True
		if not s:
			return False

		def isSame(p,q):
			if not p and not q:
				return True
			if not p or not q:
				return False
			return p.val==q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
			
		return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

class Solution2(object):
	def isSubtree2(self, s, t):
		def inorder(root):
			if not root:
				return '#'
			return '*' + str(root.val)+inorder(root.left)+inorder(root.right)
		ss = inorder(s)
		tt = inorder(t)
		return tt in ss
