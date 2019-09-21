class Solution(object):
	def another(self, x):
		if x == 0:
			return True
		if x < 0 or x % 10 == 0:
			return False
		y = 0
		while x > y:
			y = y*10 + x%10
			x = x//10
		# return y == x or (y > x and y//10 == x)
		return x == y or x == y//10

	# map, lambda
    def isPalindrome(self, x: int) -> bool:
        r = list(map(lambda i: int(10**-i * x % 10), range(int(math.log10(x)), -1, -1))) if x > 0 else [0, x]
        return r == r[::-1]

	# Pathonic
	def isPalindrom3(self, x):
		return str(x) == str(x)[::-1]
