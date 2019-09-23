class Solution(object):
	def romanToInt(self, s):
		has = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		total = 0
		for i in range(len(s) - 1):
			cur = has[s[i]]
			nex = has[s[i+1]]
			if cur < nex:
				total -= cur
			else:
				total += cur
		total += has[s[-1]]
		return total
'''
这里也是字典的活用，重点是罗马数字的特点（比如4，比如9等这些数字）
'''