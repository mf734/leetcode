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
