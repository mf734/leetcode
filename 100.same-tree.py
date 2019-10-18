# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# basic recursion
class Solution(object):
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# fast recursion
class Solution2(object):
	def isSame2(self, p, q):
		if not p and not q:
			return True
		if not p or not q:
			return False
		if p.val != q.val:
			return False
		return self.isSame2(p.right, q.right) and self.isSame2(p.left, q.left)


# DFS
def isSame(self, p, q):
	stack = [(p, q)]
	while stack:
		node1, node2 = stack.pop()
		if not node1 and not node2:
			continue
		elif None in [node1, node2]:
			return False
		else:
			if node1.val != node2.val:
				return False
			stack.append((node1.right, node2.right))
			stack.append((node1.left, node2.left))
	return True

# BFS
def isSame2(self, p, q):
	queue = [(p, q)]
	while queue:
		node1, node2 = queue.pop(0)
		if not node1 and not node2:
			continue
		elif None in [node1, node2]:
			return False
		else:
			if node1.val != node2.val:
				return False
			queue.append((node1.left, node2.left))
			queue.append((node1.right, node2.right))
	return True