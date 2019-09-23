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

'''
这一题有好几个重点要考：
1，符号处理：通过flag或者sign记录符号后，再将输入给abs
2，怎么处理digit。
   这一例中，同样用rx = rx*10 + x%10来处理个位，再用x//=10处理进位
3，怎么处理溢出
   这一例得处理两次溢出（输入一次，输出一次）
'''