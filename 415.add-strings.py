class Solution(object):
	# 002是两个链表相加，可以去看
	# 043是两个字符串相乘，可以去看
	def addStrings(self, num1, num2):
		res = ''
		i, j, carry = len(num1)-1, len(num2)-1, 0
		while i >= 0 or j >= 0:
			n1 = int(num1[i]) if i >= 0 else 0
			n2 = int(num2[j]) if j >= 0 else 0
			carry += n1 + n2
			res = str(carry%10) + res
			carry //= 10
			i -= 1
			j -= 1
		return '1' + res if carry else res