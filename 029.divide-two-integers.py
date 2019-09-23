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