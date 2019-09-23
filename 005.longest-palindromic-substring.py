class Solution(object):
	def longestPalindrome(self, s):
		def helper(l, r):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			l -= 1
			r += 1
		return s[l+1:r]
		res = ''
		for i in range(len(s)):
			# 前者是奇数往外，后者是偶数往外
			res = max(helper(i, i), help(i, i+1), res, key=len)
		return res


class Solution2(object):
	left = right = 0
	n = len(s)
	for i in range(n - 1):
		if 2 * (n - i) + 1 < right - left + 1:
			break
		l = r = i
		while l >= 0 and r < n and s[l] == s[r]:
			l -= 1
			r += 1
		if r - l - 2 > right - left:
			left = l + 1
			right = r - 1
		l = i
		r = i + 1
		while l >= 0 and r < n and s[l] == s[r]:
			l -= 1
			r += 1
		if r - l - 2 > right - left:
			left = l + 1
			right = r - 1
	return s[left:right + 1]
'''
相似题目 516 647
这题是考察递归。我们通过找回文数的中心坐标来找.
回文数可以是奇数，也可以是偶数，所以要(i,i)和(i,i+1)
再通过一个找回文数的helper，即左右指针分别扩散
'''