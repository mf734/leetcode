class Solution(objecct):        
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

'''
类似题目还有415.两个string相加，043.两个string相乘
遇到两个链表相加，重点有两个：
1，如何遍历链表；2，如何处理进位
1，直接用while or if循环，只要链表中还有元素，就可以继续遍历
   配合carry，只要有进位，循环就会把最后的进位连接进链
2，carry%10就是个位的数字，直接记下来
   carry//=10就是十位的进位，准备下次用
'''