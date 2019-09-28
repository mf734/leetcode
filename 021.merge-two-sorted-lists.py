class Solution(object):
	def mergeTwoLists(self, l1, l2):
		p = dummy = ListNode(-1)
		while l1 and l2:
			if l1.val < l2.val:
				p.next = l1
				l1 = l1.next
			else:
				p.next = l2
				l2 = l2.next
			p = p.next
		if l1:
			p.next = l1
		if l2:
			p.next = l2
		return dummy.next
	
'''
iteration是最简单也是最容易理解的方法，无非就是：
要同时有有l1、l2，然后让p往它身上连
然后剩下有谁，就把p接它身上去
需要注意的是，一定要有dummy
'''


	def recurMer(self, a, b):
		if a and b:
			if a.val > b.val:
				a, b = b, a
			a.next = self.recurMer(a.next, b)
		return a or b

'''
自我recur理解了以后会很好用，就是不断地保证a是最小的，
把剩下的交给recur去处理，跳出条件就是a and b不成立了（一个遍历完了）
'''


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

'''
inplace是我认为最manual的，和iterative思路一样，
但是相比用新链表去存储，inplace是交换位置
这里注意的就是，要用手画图，每次断链（每次换next的指向）时
都要考虑它原来的next我还用不用
如果不用，其实就是删除节点
如果要用，就得提前将它保存
相关提醒24
'''