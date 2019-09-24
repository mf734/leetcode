# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# back tracking + dfs
class Solution1(object):       
    def cop1(self, head):
        visit = {}
        def dfs(head):
            if not head:
                return None
            if head in visit:
                return visit[head]
            clone = Node(head.val, None, None)
            visit[head] = clone
            clone.next = dfs(head.next)
            clone.random = dfs(head.random)
            return clone
        return dfs(head)


class Solution2(object):
    def cop2(self, head):
        if not head:
            return None
        visit = {}
        node = head
        while node:
            visit[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            visit[node].next = visit.get(node.next)
            viist[node].random = visit.get(node.random)
            node = node.next
        return visit[head]

# 不用hashmap
class Solution3(object):
    if not head:
        return None
    
    p = head
    while p:
        clone = Node(p.val, None, None)
        # Inserting the cloned node just next to the original node.
        # If A->B->C is the original linked list,
        # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
        clone.next = p.next
        p.next = clone
        p = clone.next
    
    p = head
     # Now link the random pointers of the new nodes created.
    # Iterate the newly created list and use the original nodes random pointers,
    # to assign references to random pointers for cloned nodes.    
    while p:
        p.next.random = p.random.next if p.random else None
        p = p.next.next
    po = head
    pn = head.next
    old = head.next
    while po:
        po.next = po.next.next
        pn.next = pn.next.next if pn.next else None
        po = po.next
        pn = pn.next
    return old