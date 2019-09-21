class Solution(object):
	def mergeTwoLists(self, l1, l2):
		head = dummy = ListNode(-1)
		while l1 and l2:
			if l1.val < l2.val:
				head.next = l1
				l1 = l1.next
			else:
				head.next = l2
				l2 = l2.next
			head = head.next
		if l1:
			head.next = l1
		if l2:
			head.next = l2
		return dummy.next
	
	def recurMer(self, a, b):
		if a and b:
			if a.val > b.val:
				a, b = b, a
			a.next = self.recurMer(a.next, b)
		return a or b

	def inPlace(self, l1, l2):
		if not l1 or not l2:
			return l1 or l2
		p = dummy = ListNode(-1)
		dummy.next = l1
		while l1 and l2:
			if l1.val < l2.val:
				l1 = l1.next
			else:
				nxt = p.next
				p.next = l2
				tmp = l2.next
				l2.next = nxt
				l2 = tmp
			p = p.next
		p.next = l1 or l2
		return dummy.next