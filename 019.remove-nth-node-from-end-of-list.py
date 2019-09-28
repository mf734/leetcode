# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(-1)
		dummy.next = head
		# 快慢指针
		fast = slow = dummy

		# 将快指针和慢指针隔开n+1个距离
		for i in range(n+1):
			fast = fast.next
		# 当快指针到底的时候，慢指针就会到倒数第n+1个
		while fast:
			fast = fast.next
			slow = slow.next
		# 再直接把倒数第n+1的next，也就是第n个，跳过就好了
		slow.next = slow.next.next
		# dummy就是处理空链表的。
		return dummy.next

'''
快慢指针拉开距离了以后，当快指针到底时，满指针就在倒数的位置
这种in place的删除，比如给了index，或者给了value的
非常适合用快慢指针来找准删除的位置，然后将它给精准删除
'''