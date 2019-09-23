# back tracking
# 只有保证有效才添加括号，所以可以跟踪左括号和右括号的数目
class Solution3(object):
	def generateParenthesis(self, n):
		ans = []
		def backtrack(s='', left=0, right=0):
			if len(s) == 2*n:
				ans.append(s)
				return
			if left < n:
				backtrack(s+'(', left+1, right)
			if right < left:
				backtrack(s+')', left, right+1)
		backtrack()
		return ans
		

# Dynamic Programming
# 考虑i=n时相比n-1组括号增加的那一组括号的位置
# 剩下的括号，要么在新增的括号内部，要么在右侧
# "("+【i=p时所有括号的排列组合】+')'+ 【i=q时所有括号的排列组合】
# 且p+q=n-1，p从0到n-1，q从n-1到0
class Solution3(object):
	def generateParenthesis3(self, n):
		if n==0:
			return []
		tot = []
		tot.append([None]) # n=0
		tot.append(['()']) # n=1
		for i in range(2, n+1):
			res = []
			for j in range(i):
				now1 = tot[j] # p的括号组合
				now2 = tot[i-1-j] # q的括号组合
				for k1 in now1:
					for k2 in now2:
						if not k1:
							k1 = ''
						if not k2:
							k2 = ''
						el = '(' + k1 + ')' + k2
						res.append(el) # 把所有valid的情况添加进去
			tot.append(res) # 这就是i组括号的所有可能情况，再来看i+1的
		return tot[n]


# brute force
# 生成2^(2n)个由“（”和“）”构成的序列，然后检查是否有效
# 时间复杂度：O(2^{2n}*n)
# 对于2^{2n}个序列中的每一个
# 我们用于建立和验证该序列的复杂度为O(n)。
# 空间复杂度：O(2^{2n}n)
# 每个序列都视作是有效的。
class Solution2(object):
	def generateParenthesis2(self, n):
		def generate(A=[]):
			if len(A) == 2*n:
				if valid(A):
					ans.append(''.join(A))
			else:
				A.append('(')
				generate(A)
				A.pop()
				A.append(')')
				generate(A)
				A.pop()
		def valid(A):
			bal = 0
			for c in A:
				if c == '(':
					bal += 1
				else:
					bal -= 1
				if bal < 0:
					return False
			return bal == 0
		ans = []
		generate()
		return ans

# 闭合数
class Solution4(object):
	def generateParenthesis4(self, n):
		if N == 0:
			return [' ']
		ans = []
		for c in range(n):
			for left in self.generateParenthesis4(c):
				for right in self.generateParenthesis4(n-1-c):
					ans.append('({}){}'.format(left, right))
		return ans