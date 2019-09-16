class solution:
	# recursive
	def swapPairs(self, head):
		if not head or not head.next:
			return head
		t = head.next
		head.next = self.swapPairs(head.next.next)
		t.next = head
		return t
	
	# iterative
	def swapParis2(self, head):
		t = ListNode(-1)
		t.next = head
		c = t
		while c.next and c.next.next:
			a, b = c.next, c.next.next
			c.next, a.next = b, b.next
			b.next = a
			c = c.next.next
		return t.next