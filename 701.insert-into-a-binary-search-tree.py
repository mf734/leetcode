class Soution(objects):
	def inseIntoBST(self, root, val):
		if not root:
			return TreeNode(val)
		if root.val < val:
			root.right = self.inseIntoBST(root.right, val)
		else:
			root.left = self.inseIntoBST(root.left, val)
		return root
