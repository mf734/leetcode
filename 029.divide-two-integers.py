class Solution(object):
	def divide(self, dividend, divisor):
		# sign = (dividend > 0) ^ (divisor > 0)
		sign = (dividend < 0) == (divisor < 0)
		dividend = abs(dividend)
		divisor = abs(divisor)
		result = 0
		while dividend >= divisor:
			x = 0
			# divisor*(2^x) is just >= dividend
			while dividend >= divisor << (x+1):
				x += 1
			result += 1 << x
			dividend -= divisor << x
		return min(result if sign else -result, 2**31-1)

'''
这道题做除法的思路来源于，除法的本身其实就是减法，
结果就是可以减多少次。
简单做法就是不停地减，然后减出来的count数就是结果。
然而这里也可以加快减的过程，那就是一次减多个divisor。
用位移实现*2，加快减的次数。
'''