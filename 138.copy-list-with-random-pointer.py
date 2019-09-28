# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         self.random = None


# back tracking + dfs
class Solution1(object):       
    def cop1(self, head):
        visit = {}
        def dfs(temp):
            if not temp:
                return None
            if temp in visit:
                return visit[temp]
            clone = Node(temp.val, None, None)
            visit[temp] = clone
            clone.next = dfs(temp.next)
            clone.random = dfs(temp.random)
            return clone
        return dfs(head)
'''
D用visit检查是否存在
一个当前点的val，将两个指针指成none，
将这个点放入visit，
将它的next和random一起传进dfs，
看看它们能不能在下一个dfs里面找到，
能找到，就返回值（同时这时候也都clone好了）。
注意的是，先创建clone，再放入visit，最后才递归
'''


# hashmap
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
'''
遍历链表并将node全部复制到visit里面，
再遍历一次，将刚刚存入的点的两个指针再找出来。
这时，所有的指针其实是相当于用map连接起来了。
'''


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
        # p.next就是克隆，p.random.next就是现在的p的random的克隆
        if p.random:
            p.next.random = p.random.next
        p = p.next.next
    po = head
    clone_head = head.next
    clone_p = clone_head
    while clone_p.next:
        po.next = po.next.next
        po = po.next
        clone_p.next = clone_p.next.next
        clone_p = clone_p.next
    po.next = clone_p.next
    clone_p.next = None
    return clone_head
'''
这一题是将原node的值和next复制到clone上去，
然后node.next改为指向clone
全部搞定以后，此时的clone们都已经有了值和next了，
再一次遍历链表，此时相当于在原来的链表的结点之间加了一个中间的传递结点clone，
再次过去，就再将原node的random附给clone
'''

'''
复制有两个pointer的结点的链表，一定得遍历两次。
'''