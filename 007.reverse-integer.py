class Solution(object):
	def reverse(self, x):
		maxx = 2**31-1
		minn = -2**31
		if x < minn or x > maxx:
			return 0
		flag, rx = 1, 0
		if x < 0:
			flag = -1
			rx = -x
		while x:
			rx = rx*10 + x%10
			x //= 10
		if rx > -1 * minn:
			return 0
		return rx*flag

	def reverse2(self, x):
		maxInt = 2**31-1
		minInt = -1 * 2**31
		if x < 0:
			y = -1 * int(str(-x)[::-1]) ## [::-1] 倒叙复制string
		else:
			y = int(str(x)[::-1])
		if y > maxInt or y < minInt:
			return 0
		return y


