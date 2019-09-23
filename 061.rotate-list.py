# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def rotateRight(self, head, k):
		if not head or not head.next:
			return head
		n = 1
		old_tail = head
		while old_tail.next:
			old_tail = old_tail.next
			n += 1
		old_tail.next = head

		# new tail: (n- k%n - 1)
		# new head: (n-k%n)
		
		new_tail = head
		for i in range(n-k%n-1):
			new_tail = new_tail.next
		new_head = new_tail.next
		new_tail.next = None
		return new_head