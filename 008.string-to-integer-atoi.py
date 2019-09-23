class Solution(object):
	def myAtoi(self, s):
		# 去除空格
		s = s.strip()
		sign = 1
		if not s:
			return 0
		if s[0] in ["+", "-"]:
			if s[0] == "-":
				sign = -1
			s = s[1:]
		ans = 0
		for c in s:
			if c.isdigit():
				ans = ans * 10 + int(c)
			else:
				break
		ans *= sign
		if ans > 2**31-1:
			return 2**3-1
		if ans < -2**31:
			return -2**31
		return ans

'''
先用strip去空格，再用sign记录符号
这里也是处理digit，但是不用进位（因为没有运算）
所以直接ans = ans*10 + c就行
'''