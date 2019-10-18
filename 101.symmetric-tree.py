# recuresive
class Solution(object):
    def isSymmetric(self, root):
        def isMirror(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return isMirror(p.left, q.right) and isMirror(p.right, q.left)
            else:
                return False
        if not root:    
            return True
        else:
            return isMirror(root.left, root.right)
        

# iterative
class Solution(object):
    def isSym(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while len(stack) > 0:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
