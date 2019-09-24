# iterative
class Solution(object):
    def lca2(self, root, p, q):
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return None

# recursive
class Solution1(object):
    def lca1(self, root, p, q):
    if not root or not p or not q:
        return None
    if max(p.val, q.val) < root.val:
        return self.lca1(root.left, p, q)
    elif min(p.val, q.val) > root.val:
        return self.lca1(root.right, p, q)
    else:
        return root