class Solution(objecct):        
	# 415是两个string相加，可以去看
	def addTwo(self, l1, l2):
		dummp = p =ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			# 为什么没有if carry呢？因为carry是0的话就不能判断了
			# 比如l1 l2都是0的时候，循环进去了，但是carry是0，不能成node
			p.next = ListNode(carry%10)
			p = p.next
			carry //= 10
		return dummy.next

	def addTwo2(self, l1, l2):
		dummy = head = ListNode(0)
		carry = 0
		while l1 or l2:
			num1 = l1.val if l1 else 0
			num2 = l2.val if l2 else 0
			tmp = num1 + num2 + carry
			carry = 1 if tmp >= 10 else 0
			head.next = ListNode(tmp % 10)
			head = head.next
			if l1: l1 = l1.next
			if l2: l2 = l2.next
		if carry: head.next = ListNode(1)
		return dummy.next