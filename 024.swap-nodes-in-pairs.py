class solution:
	# recursive
	def swapPairs(self, head):
		# 只剩一位或空的时候 直接输出head
		if not head or not head.next:
			return head
		p = head.next
		head.next = self.swapPairs(head.next.next)
		p.next = head
		return p
'''
参照21的recur和inplace的概念：
1，recur的“我不管”概念
2，需要记录next的时候要记录
因为基本case就是把head和head.next对换
所以用p记录原来的head.next
把新的head.next指向swap(recur)过的链表
recur就负责把传进去的head.next.next和剩下链表做同样的操作，
并且将swap好了的p（也就是最新的头）return上去
最后就将原来的head.next指回head即可
'''
	

	# iterative
	def swapParis2(self, head):
		p, p.next = self, head
		while p.next and p.next.next:
			a, b = p.next, p.next.next
			p.next = b
			a.next = b.next
			b.next = a
			p = a #p = p.next.next
			# while循环以后的以上所有可简化为
			# p.next, b.next, a.next, p = b, a, b.next, a
		return self.next
'''
iter也是一样的，重点就是将p和p.next互换，
因为p和p.next的next都要变
所以断它们的next之前，
要将p的next和p.next的next给记下来，即为a，b
a b记下来后，将二者互换，就是
b.next指向a，a.next指向b.next（完成a，b互换）
再将p的next指向p.next.next（即为b），因为b已经成为互换后的前者了
最后将p往后跳两个
最后注明一点，a,b = b,a这种写法有一个特点
不管是a, b还是b,a，都会提前存储变量，然后直接赋值，不用担心谁先谁后
'''