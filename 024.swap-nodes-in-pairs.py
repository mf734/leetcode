class solution:
	# recursive
	def swapPairs(self, head):
		# 只剩一位或空的时候 直接输出head
		if not head or not head.next:
			return head
		# head和head.next记下来，剩下的放到下一个recursion中去
		# 记住，recursion就是不管你下一个recur中发生了啥，只要连接好了就直接搞
		t = head.next
		head.next = self.swapPairs(head.next.next)
		t.next = head
		return t
	
	# iterative
	def swapParis2(self, head):
		p, p.next = self, head
		while p.next and p.next.next:
			a, b = p.next, p.next.next
			p.next, b.next, a.next = b, a, b.next
			p = p.next.next
		return self.next