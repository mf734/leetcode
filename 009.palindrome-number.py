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
		return y == x or (y > x and y//10 == x)
	
	# Python way
	def isPalindrom2(self, x):
		return False if x < 0 else x == int(str(x)[::-1])